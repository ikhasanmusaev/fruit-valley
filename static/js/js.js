$('.product-carousel').owlCarousel({
    center: true,
    loop: true,
    margin: 30,
    autoplay: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 4
        },
        1000: {
            items: 4
        },
        1300: {
            items: 5
        }
    }
})
$('.blog-carousel').owlCarousel({
    loop: true,
    margin: 30,
    nav: true,
    autoplay: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 3
        },
        1300: {
            items: 3
        }
    }
})
$('.testimonials-carousel').owlCarousel({
    loop: true,
    nav: false,
    dots: true,
    items: 1
})

$('.sub-menu ul').hide();
$(".sub-menu a").click(function () {
    $(this).parent(".sub-menu").children("ul").slideToggle("100");
    $(this).find(".right").toggleClass("fa-chevron-down");

});

$('.con-switch').find('input').click(function () {
    $(this).parent(".con-switch").toggleClass('checked')
    if ($('.con-switch').hasClass('checked')) {
        $('.retail').removeClass('checked')
        $('.wholesale').addClass('checked')
    } else {
        $('.wholesale').removeClass('checked')
        $('.retail').addClass('checked')
    }
    if ($('.product-add-cart.retail').hasClass('checked')) {
        $('.retail').removeClass('checked')
        $('.wholesale').addClass('checked')
    } else {
        $('.wholesale').removeClass('checked')
        $('.retail').addClass('checked')
    }

})

// function openTab(evt, cityName) {
//     var i, tabcontent, tablinks;
//     tabcontent = document.getElementsByClassName("tabcontent");
//     for (i = 0; i < tabcontent.length; i++) {
//         tabcontent[i].style.display = "none";
//     }
//     tablinks = document.getElementsByClassName("tablinks");
//     for (i = 0; i < tablinks.length; i++) {
//         tablinks[i].className = tablinks[i].className.replace(" active", "");
//     }
//     document.getElementById(cityName).style.display = "block";
//     evt.currentTarget.className += " active";
// }

function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}