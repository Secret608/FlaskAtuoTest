//运行
$(function () {
    $(".demo>.btn-success").click(function () {
        var Name = $(this).attr("id");
        var tip = $("#tip");
        $.ajax({
            async: false,//同步，异步
            url: "/index/run", //请求的服务端地址
            data: {
                "name": Name
            },
            type: "post",
            dataType: "text",
            success: function (data) {
                //成功之后的处理，返回的数据就是 data
                tip.attr("class","alter_a");
                tip.text("开启运行");
                // $.parser.parse(tip);
                setTimeout(function () {tip.attr("class","alter_0");}, 1000);
                // $.parser.parse(tip);
            },
            error: function () {

                tip.attr("class","alter_b");
                tip.text("运行异常");
                // $.parser.parse(tip);
                setTimeout(function () {tip.attr("class","alter_0");}, 1000);
                // $.parser.parse(tip);
            }
        });
    });
});

//先关闭接口
$(function () {
    $(".demo>.badge-light, .demo>.btn-danger, .card-header div .btn-danger , .card-header div .btn-success ").click(function () {
        alert('对不起，您没有相应权限，请联系管理员（xiaofeng.zhang@163.com）'); //错误的处理
    });
});

//报告跳转
$(function () {
    $(".demo>.btn-info").click(function () {
        window.open("/static/Report/Demo.html");
    });
});


