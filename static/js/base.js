let nav = document.querySelector('.navbar');

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.baseURL = 'http://127.0.0.1:8000/';

toastr.options.closeButton = true;
toastr.options.closeMethod = 'fadeOut';
toastr.options.closeDuration = 150;
toastr.options.closeEasing = 'swing';


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
function changeCartItemsNumber (newItemsNumber) {
    $('.cart-items-number').text(newItemsNumber);
}
function changeFavoritesItemsNumber (newItemsNumber) {
    $('.favorites-items-number').text(newItemsNumber)
}

$(document).ready(function () {
    $("#id_phone_number").mask("+7 (999) 99 9999");

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

    $('.favorite_btn').on('click', function (event) {
        event.preventDefault();
        const target = $(this);
        const productId = target.attr('data-product-id');
        axios.post('favorites/toggle-item/', {id: productId})
            .then(response => {
                toastr.success(response.data.text);
                if (response.data.status === 200) {
                    target.addClass('main-color');
                    target.removeClass('color-grey60 hover-main-color');
                } else {
                    target.removeClass('main-color');
                    target.addClass('color-grey60 hover-main-color');
                }
            })
            .catch(error => {
                toastr.error('При добавлении товара в избранное произошла ошибка.')
            })
    });

    $('.remove_favorite').on('click', function(event) {
        event.preventDefault();
        const productId = $(this).attr('data-product-id');
        axios.post('favorites/toggle-item/', {id: productId})
            .then(response => {
                debugger;
                toastr.success(response.data.text);
                if (response.data.status === 201) {
                    const product = $(this).closest('.col');
                    product.addClass('d-none');
                };
            })
            .catch(error => {
                toastr.error('При добавлении товара в избранное произошла ошибка.')
            })
    })
});
