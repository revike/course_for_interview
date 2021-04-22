window.onload = function () {
    $('.js-create-good').on('click', function () {
        $.get("/goods/create/", function (data) {
            // Меняю всю таблицу через outerHTML
            // тут в data приходит HTML с формой добавления нового товара
            document.querySelector('#table').outerHTML = data;
            console.log("create");

            // Переместил подписку на событие клика для элемента save сюда (раньше она была ниже),
            // так как он появляется на странице только после того как мы на 4 строке
            // его добавим. Изначально его нет и этот код не будет отрабатывать.
            $('#save').on('click', function () {
                // Тут я добавил сериализацию формы, то есть это просто получение всех полей из нее
                // чтобы их все отправить в джанго
                $.post("/goods/create/", $("#newItemForm").serialize(), function (data) {
                    // Тут в data приходит таблица товаров
                    document.querySelector('#newItemForm').outerHTML = data;
                    console.log("save");
                })
            })

        })
    })
}
