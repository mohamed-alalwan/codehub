$(document).ready(function () {
    $('.sidenav').sidenav();
    $('#desktop-links').children('li').clone().each(function () {
        $('#mobile-links').append(this);
    });
});