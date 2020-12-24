let product_list = $('.p-products');
let csrf_token = $('#csrf_token').val();

function product_item(id, img, name, price, rating, sale = null) {
    return `
            <div class="product">
                <a href="/product/${id}" class="p-img">
                    <img src="http://localhost:8000${img}" alt="">
                </a>
                <div class="p-text">
                    <h3 class="p-title">
                        <a href="/product/${id}">${name}</a>
                    </h3>
                    <p class="cost">
            `.concat(sale != price ?
        `<span>${sale}</span>
             <span class="p-discount">${price}</span>
            ` :
        `
            <span>${price}</span>
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
                            Add card
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
        url: `/by_category/${id}`,
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

function add_to_favourite(product_id) {
    $.ajax({
        type: "POST",
        url: `/add_to_favorite`,
        data: {
            product_id: product_id,
            csrfmiddlewaretoken: csrf_token
        },
        dataType: 'json',
        success: (response) => {
            if ($(`#product-${product_id}`).length) {
                if (response['created']) {
                    $(`#product-${product_id}`).find('.add-favourite').find('i.far').toggleClass('liked');
                } else {
                    $(`#product-${product_id}`).find('.add-favourite').find('i.far').toggleClass('liked');
                }
            }
            if (response['created']) {
                $(`.product-img .add-favourite`).find('i').toggleClass('liked');
            } else {
                $(`.product-img .add-favourite`).find('i').toggleClass('liked');
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
}

check_list()

function remove_favourite(product_id) {
    $.ajax({
        type: "POST",
        url: `/add_to_favorite`,
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

let send_form = $('.send-mail');

send_form.submit((event) => {
    let full_name = send_form.find('input[name=full_name]').val();
    let email = send_form.find('input[name=email]').val();
    let phone = send_form.find('input[name=phone]').val();
    let content = send_form.find('textarea[name=content]').val();
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: "/send_email",
        data: {
            full_name: full_name,
            email: email,
            phone: phone,
            content: content,
            csrfmiddlewaretoken: csrf_token
        },
        dataType: 'json',
        success: (response) => {

        },
        error: (xhr, error, status) => {

        }
    })
})