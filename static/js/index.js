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
                tip.attr("class", "alter_a");
                tip.text("开启运行");
                // $.parser.parse(tip);
                setTimeout(function () {
                    tip.attr("class", "alter_0");
                }, 1000);
                // $.parser.parse(tip);
            },
            error: function () {

                tip.attr("class", "alter_b");
                tip.text("运行异常");
                // $.parser.parse(tip);
                setTimeout(function () {
                    tip.attr("class", "alter_0");
                }, 1000);
                // $.parser.parse(tip);
            }
        });
    });
});

//先关闭接口
$(function () {
    $(".demo>.badge-light,.card-header div .btn-danger ").click(function () {
        alert('对不起，您没有相应权限，请联系管理员（xiaofeng.zhang@163.com）'); //错误的处理
    });
    $("#btn_add").click(function () {
        $("#myModalLabel").text("新增");
        $('#myModal').modal();
    });
    $("#btn_submit").click(function () {

        console.log("Hello Runoob!");
        $.ajax({
            async: false,//同步，异步
            url: "/index/save", //请求的服务端地址
            data: {
                "now": $("#txt_departmentname").val(),
                "future":$("#txt_departmentlevel").val(),
                "name":$("#txt_statu").val()
            },
            type: "post",
            dataType: "text",
            success: function (data) {
                //成功之后的处理，返回的数据就是 data

                // $.parser.parse(tip);
                console.log("申请成功");
                window.location='/index';
            },
            error: function () {

                // $.parser.parse(tip);
                console.log("申请失败");
                window.location='/index';
            }
        });

        $('#myModal').modal();
    });
});

//报告跳转
$(function () {
    $(".demo>.btn-info").click(function () {
        window.open("/static/Report/Demo.html");
    });
});

//删除
$(".card-body>.demo:nth-child(2)>.btn").click(function (){

        $.ajax({
            async: false,//同步，异步
            url: "/index/del", //请求的服务端地址
            data: {
                "id":$(this).attr("id")
            },
            type: "post",
            dataType: "text",
            success: function (data) {
                //成功之后的处理，返回的数据就是 data
                // $.parser.parse(tip);
                console.log("申请成功");
                window.location='/index';
            },
            error: function () {

                // $.parser.parse(tip);
                console.log("申请失败");
                window.location='/index';
            }
        });

    });




