$(function () {
    $(".demo>.btn-success").click(function () {
        var Name = $(this).attr("id");

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
                $(this).text("运行中");
                alert('success');
            },
            error: function () {
                alert('error'); //错误的处理
            }
        });
    });
});

$(function () {
    $(".demo>.badge-light").click(function () {
        alert('对不起，您没有相应权限，请联系管理员（xiaofeng.zhang@163.com）'); //错误的处理
    });
});

$(function () {
    $(".demo>.btn-danger").click(function () {
        alert('对不起，您没有相应权限，请联系管理员（xiaofeng.zhang@163.com）'); //错误的处理
    });
});