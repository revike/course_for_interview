import sys

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

import mainWindow
from PyQt5 import QtWidgets, QtCore

from view_db import tables


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.dialog = QtWidgets.QFileDialog(self)

        self.ui.pushButton.clicked.connect(self.open_file)
        self.ui.pushButton_2.clicked.connect(self.save_data)
        self.ui.pushButton_3.clicked.connect(self.add_data)
        self.ui.pushButton_4.clicked.connect(self.delete_data)

    def open_file(self):
        filters = "DB files (*.sqlite3 *.sqlite *.db)"
        self.path = self.dialog.getOpenFileName(
            self, 'Выберите файл базы данных', filter=filters)[0]
        self.ui.textEdit.setText(self.path)

        self.tables = tables(self.path)
        self.ui.comboBox.clear()
        for table in self.tables:
            self.ui.comboBox.addItem(table)

        self.ui.comboBox.view().pressed.connect(self.handle_item_pressed)

    def handle_item_pressed(self, index):
        item = self.ui.comboBox.model().itemFromIndex(index)
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(self.path)
        self.db.open()

        model = QSqlTableModel(self)
        model.setTable(item.text())
        model.select()

        self.ui.tableView.setModel(model)

    @QtCore.pyqtSlot()
    def save_data(self):
        button = self.sender().text()
        print(button)

    @QtCore.pyqtSlot()
    def add_data(self):
        button = self.sender().text()
        print(button)
        rowPosition = self.ui.tableView.rowCount()
        self.ui.tableView.insertRow(rowPosition)

    @QtCore.pyqtSlot()
    def delete_data(self):
        button = self.sender().text()
        print(button)


def application():
    app = QtWidgets.QApplication(sys.argv)
    window_obj = MyApp()

    window_obj.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
