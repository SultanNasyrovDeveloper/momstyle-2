$(document).ready(function () {
    // variables
    const like = $('.like');

    // navigation color handling
     window.addEventListener('scroll', function (e) {
        let nav = document.querySelector('.navigation');
        if (document.documentElement.scrollTop || document.body.scrollTop > window.innerHeight) {
                TweenMax.to(nav, 1, {backgroundColor: '#191919'})
            } else {
                TweenMax.to(nav, 1, {backgroundColor: 'transparent'})
            }
    });

     // like handling
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
                if (response['answer'] === 1) {
                    likes_number.text(response['likes'])
                } else {
                    alert('Лайк можно поставить только 1 раз')
                }
            },
            error: function () {
                console.log('Error');
            }
        });
    })
});