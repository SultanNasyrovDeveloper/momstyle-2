$(document).ready(function () {

    window.addEventListener('scroll', function (e) {
        let nav = document.querySelector('.navigation');
        if (document.documentElement.scrollTop || document.body.scrollTop > window.innerHeight) {
                TweenMax.to(nav, 1, {backgroundColor: '#7d7d7d'})
            } else {
                TweenMax.to(nav, 1, {backgroundColor: 'transparent'})
            }
    });
    
    const post = $('.post');
    const like = $('.like');

    function cutLongText() {
        let elem, size, text;
        elem = document.querySelector('.post p')
        text = elem.innerHTML;
        size = 150;
        if (text.length > size) {
            text = text.slice(0, size);
        }
        elem.innerHTML = text + '...';
    }
    cutLongText();

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

    post.mouseenter(function () {
        cardMouseEnter($(this));
    });
    post.mouseleave(function () {
        cardMouseLeave($(this));
    });
    
    like.click(function (e) {
        e.preventDefault();
        let url = $(this).attr('href');
        let likes_number = $(this).find('.likes-number');
        let postId = $(this).attr('post-id')
        let data = {'post_id': postId};
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (response) {
                console.log("success");
                if (response['answer'] === 1){
                    likes_number.text(response['likes'])
                }else{
                    alert('Лайк можно поставить только 1 раз')
                }
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});