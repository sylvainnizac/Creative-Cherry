function changeVisibility() {
    $('#nav_bar_appear_button').slideUp('fast');
    $('#common-navbar').slideDown('fast');
    AutoHide(5000);
}

function AutoHide(dtime) {
    setTimeout(function() {
        $('#common-navbar').slideUp(500);
        $('#nav_bar_appear_button').slideDown(500);
    }, dtime);
}

AutoHide(3000);
