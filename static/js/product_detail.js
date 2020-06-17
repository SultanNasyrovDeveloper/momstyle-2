
async function addItemToCart (event, productId) {
    event.preventDefault();
    const size = $('.chosen').text();;
    if (!size) {
        toastr.error('Укажите размер.');
        return
    }
    const quantity = $('.quantity-option:selected').attr('value');
    axios.post('cart/add-item/', {product_id: productId, size: size, quantity: quantity})
        .then(response => {
            const data = response.data;
            changeCartItemsNumber(data.items_number);
            toastr.success(data.text);
            $('#add-to-cart').addClass('d-none');
            $('#go-to-cart').removeClass('d-none');
        })
        .catch(error => {
            toastr.error('При добавлении товара в корзину произошла ошибка.')
        })

}



$(document).ready(function () {

    darkenNavbar();
    $('.sp-wrap').smoothproducts();

    // variables
    const sizeButton = $('.size');
    const product = $('.product');
    const sizesLayout = $('.sizes-table-layout');

    // launch product image zoom/galery plugin


    // handling product size selecting
    sizeButton.click(function () {
        $(this).toggleClass('chosen');
        $(this).siblings().removeClass('chosen');
        $('#add-to-cart').removeClass('d-none');
        $('#go-to-cart').addClass('d-none');
    });

});