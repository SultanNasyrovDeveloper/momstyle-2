$(document).ready(function () {
    window.addEventListener('scroll', function (e) {
        let nav = document.querySelector('.navigation');
        if (document.documentElement.scrollTop || document.body.scrollTop > window.innerHeight) {
                TweenMax.to(nav, 1, {backgroundColor: '#7d7d7d'})
            } else {
                TweenMax.to(nav, 1, {backgroundColor: 'transparent'})
            }
    });


});