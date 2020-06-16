$(document).ready(function () {
    $('.checkbox-container > input').on('change', function() {
        $('.checkbox-container > input').not(this).prop('checked', false)
    })
})