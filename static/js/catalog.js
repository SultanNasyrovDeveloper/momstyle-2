$(document).ready(function () {
    // variables
    const product = $('.product');

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

    // handling product card hover effect
    product.mouseenter(function () {
        cardMouseEnter($(this));
    });
    product.mouseleave(function () {
        cardMouseLeave($(this))
    });


});