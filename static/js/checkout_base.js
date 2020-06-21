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

var validNavigation = false;


async function activateWindowCloseEventHandler () {
    $(window).on('mouseover', (function () {
        window.onbeforeunload = null;
    }));
    $(window).on('mouseout', (function () {
        window.onbeforeunload = ConfirmLeave;
    }));
    function ConfirmLeave() {
        axios.post('order/incomplete')
    }
    var prevKey="";
    $(document).keydown(function (e) {
        if (e.key=="F5") {
            window.onbeforeunload = ConfirmLeave;
        }
        else if (e.key.toUpperCase() == "W" && prevKey == "CONTROL") {
            window.onbeforeunload = ConfirmLeave;
        }
        else if (e.key.toUpperCase() == "R" && prevKey == "CONTROL") {
            window.onbeforeunload = ConfirmLeave;
        }
        else if (e.key.toUpperCase() == "F4" && (prevKey == "ALT" || prevKey == "CONTROL")) {
            window.onbeforeunload = ConfirmLeave;
        }
        prevKey = e.key.toUpperCase();
    });
}


$(document).ready(function() {
    $('.disabled_tab').click(event => event.preventDefault());
})