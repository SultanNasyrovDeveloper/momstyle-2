$(document).ready(function () {
    activateNavbarColorChanger();
    $('.partners-slider').slick({
        infinite: true,
        dots: true,
        slidesToShow: 5,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
    });
});