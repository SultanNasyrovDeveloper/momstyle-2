$(document).ready(function () {
    // variables
    const burger = $('.toggle-btn');
    const toggleContainer = $('.toggle-content');
    const toggleClose = $('.close-toggle');

    // handle toggle content
    burger.click(function () {
        toggleContainer.css('display', 'flex');
    });
    toggleClose.click(function () {
        toggleContainer.css('display', 'none')
    });

    // contact us form phone input field mask
    $(".contact-phone").mask("+7 (999) 999-9999");

    // handle contact us form
    $('.contact-us').submit(function (e) {
        e.preventDefault();

        // prepare data
        let name = $('.contact-name').val();
        let phone = $('.contact-phone').val();
        let url = $(this).attr('action');
        let data = {'name': name, 'phone': phone};

        // make ajax call
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (response) {
                console.log("success");
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    // handle up button work
    $('.up').click(function () {
        TweenMax.to(window, 0.5, {scrollTo: 0})
    });

});