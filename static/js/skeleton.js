setTimeout(function() {
    $('#common-navbar').slideUp(500);
    $('#nav_bar_appear_button').slideDown(500);
}, 3000);

function changeVisibility() {
    $('#nav_bar_appear_button').slideUp('fast');
    $('#common-navbar').slideDown('fast');
}