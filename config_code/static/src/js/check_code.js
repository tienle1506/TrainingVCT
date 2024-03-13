$(document).ready(function(){
        $('#apply_promo_btn').click(function(event){
            event.preventDefault();
            var self = this;
            // Thực hiện gọi hàm RPC
            return self._rpc({
                model: 'res.partner',
                method: 'check_code_in_website_sale',
                args: [],
                context: self.initialState.context,
            }).then(function(result) {
                self.do_action(result);
            });
        });
    });