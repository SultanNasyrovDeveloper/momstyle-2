$(document).ready(function () {

    // variables
    const sizeButton = $('.size');
    const product = $('.product');
    const sizesLayout = $('.sizes-table-layout');

    // launch product image zoom/galery plugin
    $('.sp-wrap').smoothproducts();

    // card hover effect functions
    function cardMouseEnter(card) {
        let imageCaption = card.find('.image-caption');
        let image = card.find('.main-img');
        TweenMax.to(imageCaption, 0.5, {opacity: 1});
        TweenMax.to(image, 3, {scale: 1.3});
    }

    function cardMouseLeave(card) {
        let imageCaption = card.find('.image-caption');
        let image = card.find('img');
        TweenMax.to(imageCaption, 0.5, {opacity: 0});
        TweenMax.to(image, 3, {scale: 1});
    }

    // handling product size selecting
    sizeButton.click(function () {
        $(this).toggleClass('chosen');
        $(this).siblings().removeClass('chosen');
    });

    // adding to cart
    $('.add-item').click(function (e) {
        e.preventDefault();
        let size = $('.chosen');

        if (size.length === 0) {
            alert('Выберите размер');
            return ;
        }

        let data = {};
        data['product_id'] = $(this).attr('product_id');
        data['size'] = size.text();
        data['quantity'] = $('.quantity-option:selected').attr('value');

        let url = $(this).attr('href');
        console.log(url);

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (response) {
                console.log("Success");
                $('.cart-items-number').text(response['items']);
                sizeButton.removeClass('chosen');
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    // recommendation product cards hover effect handling
    product.mouseenter(function () {
        cardMouseEnter($(this));
    });
    product.mouseleave(function () {
        cardMouseLeave($(this))
    });

    // handling size table
    $('.sizes-table-link').click(function (e) {
        e.preventDefault();
        sizesLayout.css('display', 'block');
    });

    $('.close').click(function () {
        sizesLayout.css('display', 'none');
    });

});