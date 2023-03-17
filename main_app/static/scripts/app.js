$(document).ready(function () {
    //nav bar
    $('.sidenav').sidenav();
    $('#desktop-links').children('li').clone().each(function () {
        $(this).children('a').each(function () {
            if ($(this).hasClass('dropdown-trigger'))
                $(this).data('target', 'profile-mobile')
        });
        $('#mobile-links').append(this);
    });
    //collapsible
    $('.collapsible').collapsible();
    //carousel
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
      });
    //dropdown
    $(".dropdown-trigger").dropdown();
});