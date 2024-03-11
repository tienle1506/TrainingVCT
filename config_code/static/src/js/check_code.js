function applyPromoCode() {
    var promoCodeInput = document.getElementById("promo_code_input");
    var promoCode = promoCodeInput.value;

    if (promoCode) {
        // Gọi hàm kiểm tra mã khuyến mãi ở phía server
        openerp.jsonRpc('/check_promo_code', 'call', {'promo_code': promoCode}).then(function (result) {
            if (result) {
                alert("Áp dụng mã khuyến mãi thành công");
            } else {
                alert("Mã khuyến mãi không thoả mãn");
            }
        });
    } else {
        alert("Vui lòng nhập mã khuyến mãi");
    }
}
