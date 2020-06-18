function setCurrentTab (number) {
    $('#tab-' + number).addClass('active_tab');
    let previous = number - 1;
    while (previous > 0){
        $('#tab-' + previous).addClass('previous_tab');
        previous --;
    }
    let next = number + 1;
    while (next < 5) {
        $('#tab-' + next).addClass('disabled_tab');
        next ++;
    }
}

$(document).ready(function() {
    $('.disabled_tab').click(event => event.preventDefault());
})