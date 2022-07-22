$(document).ready(function () {
    HideCurrentPageFromNavbar();

    // CLICK HAMBURGER
    $("header .hamburger").on("click", function () {
        $(this).toggleClass("active");
        $("header .dropdown").slideToggle();
    });

    // HIDE CURRENT PAGE FROM NAVBAR
    function HideCurrentPageFromNavbar() {
        var currentPage = $("#pageLocation").html();

        $("header .dropdown a").each(function () {
            if ($(this).html() == currentPage) {
                $(this).hide();
                $("#pageName").html($(this).html());
            }
        });
    }

    $(".wallpaper.owl-carousel").owlCarousel({
        items: 1,
        loop: true
        // autoplay: true
    });

    $(".wallpaper .imgHolder").each(function(){
        $(this).css("background-image", "url(" + $(this).data("image") + ")");
    });

    $(".event.owl-carousel").owlCarousel({
        items:1,
        loop: true,
        autoplay: true,
        margin: 30,
        dots: false,
        responsive: {
            0 : {items: 1},
            768 : {items: 2},
            992: {
                items: 3,
                autoplay: false
            }
        }
    });

    // F A D E   I N   L I G H T B O X
    $("#educationevent .inner a").each(function(){
        var url = $(this).data("url");
        $(this).on("click", function(e){
            e.preventDefault();
            $("#lightbox iframe").attr("src", url);
            $("#lightbox").fadeIn();
        });
    });

    // F A D E   O U T   L I G H T B O X
    $("#lightbox .layout, #lightbox img").on("click", function(){
        $("#lightbox").fadeOut();
    });

    // F O O T E R   Y E A R
    $("footer span").html((new Date()).getFullYear());

    $(".cities.owl-carousel").owlCarousel({
        items:1,
        loop: true,
        autoplay: true,
        margin: 50,
        dots: false,
        responsive: {
            0 : {items: 1},
            768 : {items: 2},
            992: {items: 3}
        }
    });

    $(".partner.owl-carousel").owlCarousel({
        items:1,
        loop: true,
        // autoplay: true,
        nav:true,
        navText: ['<img src="img/left-chevron.png">', '<img src="img/right-chevron.png">'],
        dots: false,
        responsive: {
            0 : {items: 1},
            768 : {items: 2},
            992: {items: 3}
        }
    });
});