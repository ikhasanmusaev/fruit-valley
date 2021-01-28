let product_list = $('.p-products');
const language_code = window.location.pathname.split('/')[1]
let modalSuccess = $('.success-modal');
let modalError = $('.error-modal');


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function hidden(delay1, variable) {
    await sleep(delay1);
    variable.css({
        'top': '-40%'
    });
    await sleep(900);
    variable.css({
        'top': '0',
        'left': '-100%',
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrf_token = getCookie('csrftoken');

function product_item(id, img, name, price, rating, sale = null) {
    return `
            <div class="product">
                <a href="/product/${id}" class="p-img">
                    <img src="${location.protocol}//${location.host}${img}" alt="">
                </a>
                <div class="p-text">
                    <h3 class="p-title">
                        <a href="/product/${id}">${name}</a>
                    </h3>
                    <p class="cost">
            `.concat(sale != price ?
        `<span>$${sale}</span>
             <span class="p-discount">$${price}</span>
            ` :
        `
            <span>$${price}</span>
            `,
        `
                    </p>
                    <ul class="rating">
                        ${rating}
                    </ul>
                    <div class="add-to-card">
                        <a href="javascript:void(0);" class="add-favourite" onclick="add_to_favourite(${id})">
                            <i class="far fa-heart"></i>
                        </a>
                        <a href="/product/${id}" class="add-card">
                            Read more..
                        </a>
                        <a href="#" class="open">
                            <i class="far fa-heart"></i>
                        </a>
                    </div>
                </div>
            </div>
        `)
}

function by_category(id) {
    if (id === 0) {
        $('li').children($('a.active')).removeClass('active');
        $('#category-0').toggleClass('active');
    } else {
        $('li').children($('a.active')).removeClass('active');
        $(`#category-${id}`).toggleClass('active');
    }
    $.ajax({
        type: "GET",
        url: `/${language_code}/by_category/${id}`,
        dataType: 'json',
        success: (response) => {
            product_list.empty()
            response['data'].forEach((element) => {
                product_list.append(
                    product_item(
                        element['id'],
                        element['image'],
                        element['name'],
                        element['price'],
                        element['rating_stars'],
                        element['sale'] ? element['sale'] : null,
                    )
                )
            })
        },
        error: (xhr, error, status) => {
            console.log(error);
            console.log(status);
        }
    });
}

let addToCart = (product_id) => {
    const amount = $('.checked .cost').children('span').text().replace('$', '');
    let total = $('.quantity__input').val();
    let checked = $('.con-switch #check').is(':checked')
    console.log(checked)
    $.ajax({
        type: 'POST',
        url: `/${language_code}/orders/cart/`,
        dataType: 'json',
        data: {
            product_id: product_id,
            csrfmiddlewaretoken: csrf_token,
            type_of_selling: checked, // weight or qty
            total: total, // weight or qty
            amount: Number(amount) * Number(total),
        },
        beforeSend: (() => {
            $('.sb').show();
        }),
        success: (data) => {
            $('.sb').hide();
            modalSuccess.css({
                'left': '20%',
            });
            hidden(5000, modalSuccess).then();
        },
        error: (e) => {
            $('.sb').hide();
            modalError.css({
                'left': '20%',
            });
            hidden(5000, modalError).then();
        }

        // success: (response) => {
        //     location.reload(true);
        // },
        // error: (xhr, error, status) => {
        //     console.log(error);
        //     console.log(status);
        // }
    })
}

$('.success-modal sup').on('click', (e) => {
    hidden(200, modalSuccess).then();
});

$('.error-modal sup').on('click', (e) => {
    hidden(200, modalError).then();
})

function submitForm(element) {
    element.submit()
}


let removeCart = (cart_id) => {
    let cart = $(`#cart-item-${cart_id}`);

    $.ajax({
        type: "POST",
        url: `/${language_code}/orders/cart/`,
        data: {
            csrfmiddlewaretoken: csrf_token,
            delete: cart_id,
        },
        success: (response, status) => {
            cart.remove()
            location.reload(true);
        },
        error: (xhr, error, status) => {
            console.log(error);
            console.log(status);
        }
    })
}

let removeOrder = (order_id) => {
    $.ajax({
        type: "POST",
        url: `/${language_code}/orders/remove-order/${order_id}`,
        data: {
            csrfmiddlewaretoken: csrf_token,
        },
        success: (response, status) => {
            location.reload(true);
        },
        error: (xhr, error, status) => {
            console.log(error);
            console.log(status);
        }
    })
}

function add_to_favourite(product_id) {
    $.ajax({
        type: "POST",
        url: `/${language_code}/add_to_favorite`,
        data: {
            product_id: product_id,
            csrfmiddlewaretoken: csrf_token
        },
        dataType: 'json',
        success: (response) => {
            if ($(`#product-${product_id}`).length) {
                if (response['created']) {
                    $(`#product-${product_id}`).find('.add-favourite').find('i.far').toggleClass('liked fas');
                } else {
                    $(`#product-${product_id}`).find('.add-favourite').find('i.far').toggleClass('liked fas');
                }
            }
            if (response['created']) {
                $(`.product-img .add-favourite`).find('i').toggleClass('liked fas');
            } else {
                $(`.product-img .add-favourite`).find('i').toggleClass('liked fas');
            }
        },
        error: (xhr, error, status) => {
            console.log(error);
            console.log(status);
        }
    });
}

let check_list = () => {
    if (!$('tbody.wishlist').children().length) {
        $('tbody.wishlist').append(`
                <tr>
                    <td></td>
                    <td></td>
                    <td>Not Favourite Products! To <a href="/">Home</a></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
        `)
    }
    if (!$('tbody').children().length) {
        $('tbody').append(`
                <tr>
                    <td></td>
                    <td></td>
                    <td>Products not exists! To <a href="/">Home</a></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
        `)
    }
}

check_list()

function remove_favourite(product_id) {
    $.ajax({
        type: "POST",
        url: `/${language_code}/add_to_favorite`,
        data: {
            product_id: product_id,
            csrfmiddlewaretoken: csrf_token
        },
        dataType: 'json',
        success: (response) => {
            if (!response['created']) {
                $(`#favourite-product-${product_id}`).remove()
                check_list()
            }
        }
        ,
        error: (xhr, error, status) => {
            console.log(error);
        }
    });
}

// let send_form = $('.send-mail');
//
// send_form.submit((event) => {
//
//     let full_name = send_form.find('input[name=full_name]').val();
//     let email = send_form.find('input[name=email]').val();
//     let phone = send_form.find('input[name=phone]').val();
//     let content = send_form.find('textarea[name=content]').val();
//     event.preventDefault();
//     $.ajax({
//         type: "POST",
//         url: `/${language_code}/send_email`,
//         data: {
//             full_name: full_name,
//             email: email,
//             phone: phone,
//             content: content,
//             csrfmiddlewaretoken: csrf_token
//         },
//         dataType: 'json',
//         success: (response) => {
//
//         },
//         error: (xhr, error, status) => {
//
//         }
//     })
// })
