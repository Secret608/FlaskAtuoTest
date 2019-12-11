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

    $(".demo>.badge-light,.card-header div .btn-danger,.nav-item").not(".btn.badge-light,.nav-item.active,.btn.btn-danger ").click(function () {
        
        alert('对不起，您没有相应权限，如需查看，请联系管理员（qi.zhang@163.com）', function(){

            window.location='/index';
            // 
        }); 
    
    });

    $("#btn_add").click(function () {
        $("#myModalLabel").text("新增");
        $('#myModal').modal();
    });

    $("#btn_submit").click(function () {

        console.log("Hello Runoob!");
        var a = $("#myModalLabel").text();
        var b = "";
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

//权限控制
$(".nav-item").click(function(){

    ;

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

//下载
$("#look").click(function (){

         window.open("/index/down");
         // window.open ("/index/down", "newwindow2", "height=1000, width=1000, top=500, left=500,toolbar=no, menubar=no, scrollbars=no, resizable=no, location=no, status=no")
    });

$("#down").click(function(){

        var link = document.createElement('a');
        //设置下载的文件名
        link.download = 'hh.md';
        link.style.display = 'none';
        //设置下载路径
        link.href = "/index/down";
        //触发点击
        document.body.appendChild(link);
        link.click();
        //移除节点
        document.body.removeChild(link);

});

//修改
// $(".card-body > .demo>.btn.badge-light").click(function(){
//
//         var i = "."+$(this).attr("id");
//         console.log(i);
//         $("#myModalLabel").text("修改");
//         $('#myModal').modal();
//         $("#txt_departmentname").val($(i).text());
//         $("#txt_departmentlevel").val($(i).next().text());
//         $("#txt_statu").val($(i).next().next().text());
// });
