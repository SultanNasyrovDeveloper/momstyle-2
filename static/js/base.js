let nav = document.querySelector('.navbar');

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

function darkenNavbar () {
    TweenMax.to(nav, 1, {backgroundColor: '#808080'})
}

function lightenNavbar () {
    TweenMax.to(nav, 1, {backgroundColor: 'transparent'})
}

function activateNavbarColorChanger() {
    if (document.documentElement.scrollTop || document.body.scrollTop > window.innerHeight) darkenNavbar();

    window.addEventListener('scroll', function (event) {
        if (document.documentElement.scrollTop || document.body.scrollTop > window.innerHeight) {
            darkenNavbar();
        } else {
            lightenNavbar()
        }
    });
}

$(document).ready(function () {
    const card = $('.product-card');

    card.mouseenter(function cardMouseEnter() {
        let imageCaption = $(this).find('.image-caption');
        let image = $(this).find('.main-img');

        TweenMax.to(imageCaption, 0.5, {opacity: 1});
        TweenMax.to(image, 3, {scale: 1.3});
    });
    card.mouseleave(function cardMouseLeave() {
        let imageCaption = $(this).find('.image-caption');
        let image = $(this).find('img');

        TweenMax.to(imageCaption, 0.5, {opacity: 0});
        TweenMax.to(image, 3, {scale: 1});
    });

    const productCardBtn = card.find('.btn');
});
