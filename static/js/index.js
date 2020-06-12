$(document).ready(function () {
    // navigation panel color handling function
    activateNavbarColorChanger();
    $(function() { $('.slide').slide(); });

    axios.post('http://127.0.0.1:8000/cart/add-item/', {})
        .then(response => console.log('Success'));

    const catalogBtn = $('.catalog-btn');
    catalogBtn.mouseenter(function () {
        TweenMax.to($(this), 0.5, {backgroundColor: 'rgba(0, 0, 0, 0.6)'});
    });
    catalogBtn.mouseleave(function () {
        TweenMax.to($(this), 0.5, {backgroundColor: 'rgba(0, 0, 0, 0.3)'});
    });


});