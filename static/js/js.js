$(".product-carousel").owlCarousel({
    center: true,
    loop: true,
    margin: 30,
    autoplay: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1,
        },
        600: {
            items: 2,
        },
        1000: {
            items: 3,
        },
        1300: {
            items: 5,
        },
    },
});
$(".blog-carousel").owlCarousel({
    loop: true,
    margin: 30,
    nav: true,
    autoplay: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1,
        },
        600: {
            items: 2,
        },
        1000: {
            items: 2,
        },
        1300: {
            items: 3,
        },
    },
});
$(".testimonials-carousel").owlCarousel({
    loop: true,
    nav: false,
    dots: true,
    items: 1,
});
document.addEventListener("DOMContentLoaded", () => {
    if ($(".sub-menu").hasClass("active")) {
        $(".sub-menu.active").children("ul").slideToggle("100");
        $(".sub-menu.active").find(".right").toggleClass("fa-chevron-down");
    }
});
$(".sub-menu ul").hide();
$(".sub-menu a").click(function () {
    $(this).parent(".sub-menu").children("ul").slideToggle("100");
    $(this).find(".right").toggleClass("fa-chevron-down");
});

$(".con-switch")
    .find("input")
    .click(function () {
        $(this).parent(".con-switch").toggleClass("checked");
        if ($(".con-switch").hasClass("checked")) {
            $(".wholesale").removeClass("checked");
            $(".retail").addClass("checked");
            $('.con-switch #check').attr('checked', true);
            $('#product_check_input').val('weight');
        } else {
            $(".retail").removeClass("checked");
            $(".wholesale").addClass("checked");
            $('.con-switch #check').attr('checked', false);
            $('#product_check_input').val('qty');
        }
        if ($(".product-add-cart.retail").hasClass("checked")) {
            $(".retail").removeClass("checked");
            $(".wholesale").addClass("checked");
        } else {
            $(".wholesale").removeClass("checked");
            $(".retail").addClass("checked");
        }
    });

function openTab(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function (event) {
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


$(".header-open").click(function () {
    $("header").toggleClass("active");
});

$(".header-close").click(function () {
    $("header").toggleClass("active");
});

let addOrSubtract = (element, price) => {
    return element.text('$'.concat(String(Math.round((Number(element.text().replace('$', '')) + Number(price)) * 100) / 100)))
}


$(document).ready(function () {
    const minus = $('.quantity__minus');
    const plus = $('.quantity__plus');

    minus.click(function (e) {
        const amount = $('.checked .cost span.cost-default').text().replace('$', '');
        const input = $('.checked .quantity__input');
        let cost = $('.checked .cost span.cost-changing');

        e.preventDefault();
        var value = input.val();
        if (value > 1) {
            value--;
            input.val(value);
            $('#product_total_input').val(value)
            addOrSubtract(cost, -amount)
            $('#product_amount_input').val($('.checked .cost span.cost-changing').text().replace('$', ''))
        }
    });

    plus.click(function (e) {
        const amount = $('.checked .cost span.cost-default').text().replace('$', '');
        const input = $('.checked .quantity__input');
        let cost = $('.checked .cost span.cost-changing');

        e.preventDefault();
        var value = input.val();
        value++;
        input.val(value);
        $('#product_total_input').val(value)
        addOrSubtract(cost, +amount)
        $('#product_amount_input').val($('.checked .cost span.cost-changing').text().replace('$', ''))
    })

});


let addOrSubtractPrice = (id, plus = true) => {
    let input = $(`#cart-item-${id} .quantity__input`);
    let price = $(`#cart-item-${id} .product-price`).text().replace('$', '');
    let product_total = $(`#cart-item-${id} .product-total`);
    let subtotal = $('.subtotal p span');
    let total = $('.total p span');

    if (plus) {
        let value = input.val();
        value++;
        input.val(value);
        addOrSubtract(product_total, price);
        addOrSubtract(subtotal, price);
        addOrSubtract(total, price)
    } else {
        let value = input.val();
        if (value > 1) {
            value--;
            input.val(value);
            addOrSubtract(product_total, -price);
            addOrSubtract(subtotal, -price);
            addOrSubtract(total, -price)
        }
    }
}

$(".product-carousel").owlCarousel({
  center: true,
  loop: true,
  margin: 30,
  autoplay: true,
  autoplayTimeout: 3000,
  autoplayHoverPause: true,
  responsive: {
    0: {
      items: 1,
    },
    600: {
      items: 2,
    },
    1000: {
      items: 3,
    },
    1200: {
      items: 3,
    },
    1300: {
      items: 4,
    },
  },
});
