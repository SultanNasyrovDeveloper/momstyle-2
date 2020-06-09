$(document).ready(function () {

    // variables
    const category = $('.category');
    const product = $('.product');
    const look = $('.look');
    const catalogBtn = $('.catalog-btn');

    // card animation functions
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

     // navigation panel color handling function
    window.addEventListener('scroll', function (e) {
        let nav = document.querySelector('.navigation');
        if (document.documentElement.scrollTop || document.body.scrollTop > window.innerHeight) {
                TweenMax.to(nav, 1, {backgroundColor: '#7d7d7d'})
            } else {
                TweenMax.to(nav, 1, {backgroundColor: 'transparent'})
            }
    });

    // carousel launch
    $(function() { $('.slide').slide(); });

    // carousel card hover effect handling
    category.mouseenter(function () {
        cardMouseEnter($(this));
    });
    category.mouseleave(function () {
        cardMouseLeave($(this));
    });

    // product card hover effect handling
    product.mouseenter(function () {
        cardMouseEnter($(this));
    });
    product.mouseleave(function () {
        cardMouseLeave($(this))
    });

    // look card hover effect handling
    look.mouseenter(function () {
        cardMouseEnter($(this))
    });
    look.mouseleave(function () {
        cardMouseLeave($(this))
    });

    // catalog btn hover effect handling
    catalogBtn.mouseenter(function () {
        TweenMax.to($(this), 0.5, {backgroundColor: 'rgba(0, 0, 0, 0.6)'});
    });

    catalogBtn.mouseleave(function () {
        TweenMax.to($(this), 0.5, {backgroundColor: 'rgba(0, 0, 0, 0.3)'});
    });
});