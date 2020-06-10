let nav = document.querySelector('.navbar');

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
    const card = $('.card');

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

    //
    //
    // // contact us form phone input field mask
    // $(".contact-phone").mask("+7 (999) 999-9999");
    //
    // // handle contact us form
    // $('.contact-us').submit(function (e) {
    //     e.preventDefault();
    //
    //     // prepare data
    //     let name = $('.contact-name').val();
    //     let phone = $('.contact-phone').val();
    //     let url = $(this).attr('action');
    //     let data = {'name': name, 'phone': phone};
    //
    //     // make ajax call
    //     $.ajax({
    //         url: url,
    //         type: 'POST',
    //         data: data,
    //         dataType: 'json',
    //         success: function (response) {
    //             console.log("success");
    //         },
    //         error: function () {
    //             console.log('Error');
    //         }
    //     });
    // });
    //
    // // handle up button work
    // $('.up').click(function () {
    //     console.log('Clicked')
    //     TweenMax.to(window, 0.5, {scrollTo: 0})
    // });
    //
// });