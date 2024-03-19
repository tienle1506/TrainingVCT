odoo.define('vct_weather.ClickButtonDay', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    $(document).ready(function () {
        $("#dateForm button").click(function (event) {
            event.preventDefault();
            var day = $(this).val();
            console.log('Ngày được chọn: ', day);
            $.ajax({
                    url: '/api/weather?',
                    method: 'GET',
                    dataType: 'json',
                    data: { 'day': day },
                    success: function (response) {
                    console.log(response)
                    $("#content").empty();
                    response.forEach(function(item) {
                        var newRow = $("<tr>");
                        newRow.append("<td>" + item.day_item + "</td>");
                        newRow.append("<td>" + item.date_item + "</td>");
                        newRow.append("<td>" + item.temp_hi + "</td>");
                        newRow.append("<td>" + item.temp_lo + "</td>");
                        newRow.append("<td>" + item.no_wrap1 + "</td>");
                        newRow.append("<td>" + item.no_wrap2 + "</td>");
                        newRow.append("<td>" + item.precip_content + "</td>");
                        // Thêm hàng mới vào bảng
                        $("#content").append(newRow);
                    });
                },
                })
        });
    });
});