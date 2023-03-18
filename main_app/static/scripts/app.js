$(document).ready(function () {
    //nav bar
    $('.sidenav').sidenav();
    $('#desktop-links').children('li').clone().each(function () {
        $('#mobile-links').append(this);
    });
    //collapsible
    $('.collapsible').collapsible();
    //carousel
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
    });
});