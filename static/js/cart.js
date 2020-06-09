$(document).ready(function () {

    // variables
    const total = $('.total');
    const itemsNumber = $('.cart-items-number');
    const select = $('.quantity-select');
    const itemsContainer = $('.cart-items-container');
    const orderLayout = $('.order-form-layout');
    const orderButton = $('.make-order');

    function make_item_key(element){
        let name = element.siblings('.name').text();
        let size = element.siblings('.size').text();
        return name + ' (' + size + ')';
    }

    // handle item quantity number
    select.each(function () {
        let value = $(this).attr('value');
        $(this).val(value);
    });


    // delete item
    $('.delete-item').click(function (e) {
        e.preventDefault();

        let item = $(this).parent();
        let key = make_item_key($(this));
        let data = {'key': key};
        let url = $(this).attr('href');

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (response) {
                console.log("success");
                item.remove();
                itemsNumber.text(response['items']);
                total.text(response['total']);
                console.log(response['total']);
            },
            error: function () {
                console.log('Error');
            }
        });

    });

    // quantity change
    select.change(function () {
        let key = make_item_key($(this));
        let quantity = $(this).find('option:selected').attr('value');
        let subtotal = $(this).siblings('.subtotal');
        let url = $(this).attr('change-url');
        let data = {'key': key, 'quantity': quantity};

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (response) {
                console.log("success");
                total.text(response['total']);
                subtotal.text(response['subtotal']);
            },
            error: function () {
                console.log('Error');
            }
        });

    });

    // clean cart
    $('.clean').click(function (e) {
        e.preventDefault();
        let url = $(this).attr('href');
        $.ajax({
            url: url,
            type: 'GET',
            success: function (response) {
                console.log("success");
                total.text(0);
                itemsNumber.text(0);
                itemsContainer.empty();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    // open order layout
    $('.open-order-form').click(function (e) {
        e.preventDefault();
        orderLayout.css('display', 'flex');
    });

    // close order layout
    $('.close').click(function () {
        orderLayout.css('display', 'none');
    });

    // phone input mask
    $(".phone-input").mask("+7 (999) 999-9999");

    // make order button click
    orderButton.click(function (e) {
        e.preventDefault();
        let name = $('.name-input').val();
        let phone = $('.phone-input').val();
        let url = $(this).attr('href');
        let data = {'name': name, 'phone_number': phone}
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (response) {
                console.log("success");
                itemsContainer.empty();
                total.text(0);
                itemsNumber.text(0);
                orderLayout.css('display', 'none');
            },
            error: function () {
                console.log('Error');
            }
        });
    });
});