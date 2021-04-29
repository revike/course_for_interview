from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


class Database:
    """База данных"""
    Base = declarative_base()

    class Categories(Base):
        """Категории товаров"""
        __tablename__ = 'categories'
        category_name = Column(String, primary_key=True, unique=True)
        category_description = Column(String)

        def __init__(self, category_name, category_description):
            self.category_name = category_name
            self.category_description = category_description

    class Units(Base):
        """Единицы измерения товаров"""
        __tablename__ = 'units'
        unit = Column(String, primary_key=True)

        def __init__(self, unit):
            self.unit = unit

    class Positions(Base):
        """Должности сотрудников"""
        __tablename__ = 'positions'
        position = Column(String, primary_key=True, unique=True)

        def __init__(self, position):
            self.position = position

    class Goods(Base):
        """Товары"""
        __tablename__ = 'goods'
        good_id = Column(Integer, primary_key=True)
        good_name = Column(String)
        good_unit = Column(ForeignKey('units.unit'))
        good_cat = Column(ForeignKey('categories.category_name'))

        def __init__(self, good_name, good_unit, good_cat):
            self.good_name = good_name
            self.good_unit = good_unit
            self.good_cat = good_cat

    class Employees (Base):
        """Таблица Сотрудники"""
        __tablename__ = 'employees'
        employee_id = Column(Integer, primary_key=True)
        employee_fio = Column(String)
        employee_position = Column(ForeignKey('positions.position'))

        def __init__(self, employee_fio, employee_position):
            self.employee_fio = employee_fio
            self.employee_position = employee_position

    class Vendors(Base):
        """Таблица поставщики"""
        __tablename__ = 'vendors'
        vendor_id = Column(Integer, primary_key=True)
        vendor_name = Column(String)
        vendor_owner_chip_form = Column(String)
        vendor_address = Column(String)
        vendor_phone = Column(String)
        vendor_email = Column(String)

        def __init__(
                self, vendor_name, vendor_owner_chip_form,
                vendor_address, vendor_phone, vendor_email
        ):
            self.vendor_name = vendor_name
            self.vendor_owner_chip_form = vendor_owner_chip_form
            self.vendor_address = vendor_address
            self.vendor_phone = vendor_phone
            self.vendor_email = vendor_email

    def __init__(self, db_path):
        self.engine = create_engine(f'sqlite:///{db_path}', echo=False)
        self.Base.metadata.create_all(self.engine)
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def categories_all(self):
        """Возвращает категории"""
        return self.session.query(self.Categories.category_name).all()


if __name__ == '__main__':
    db = Database('db.sqlite3')
    print(db.categories_all())
    cat = db.Categories('phone', 'qwerty')
    db.session.add(cat)
    db.session.commit()
    print(db.categories_all())
