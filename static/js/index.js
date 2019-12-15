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

        alert('对不起，您没有相应权限，如需查看，请联系管理员（qi.zhang@163.com）', function () {

            window.location = '/index';
            // 
        });

    });

    $("#btn_add").click(function () {
        $("#myModalLabel").text("新增");
        $('#myModal').modal();
    });

    //保存
    $("#btn_submit").click(function () {

        // console.log("Hello Runoob!");
        $("tbody").empty();
        var a = $("#queryDevice").prop('selectedIndex');
        $.ajax({
            async: false,//同步，异步
            url: "/index/save", //请求的服务端地址
            data: {
                "num":a,
                "now": $("#txt_departmentname").val(),
                "future": $("#txt_departmentlevel").val(),
                "name": $("#txt_statu").val()
            },
            type: "post",
            dataType: "json",
            success: function (data) {
                $.each(data, function (idx, obj) {
                $("tbody").append("<tr><td>"+obj[0]+"</td><td>"+obj[1]+"</td><td>"+obj[2]+"</td><td>"+obj[3]+"<td><div class=\"card-body\" style=\"display: inline-flex\"><p class=\"demo\"><button class=\"btn badge-light\">修改</button></p><p class=\"demo\"><button class=\"btn btn-danger\" id="+idx +">删除</button></p></div></td></tr>");
                // $("#province").append("<option value=" + value + ">" + obj.name + "</option>");
            });

            },
            error: function () {
                // $.parser.parse(tip);
                console.log("申请失败");
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
$(".nav-item").click(function () {

    ;

});

//删除
$(document).on('click','.card-body>.demo:nth-child(2)>.btn',function(){
    var a = $("#queryDevice").prop('selectedIndex');
    $.ajax({
        async: false,//同步，异步
        url: "/index/del", //请求的服务端地址
        data: {
            "num": a,
            "id": $(this).attr("id")
        },
        type: "post",
        dataType: "json",
        success: function (data) {
            //成功之后的处理，返回的数据就是 data
            // $.parser.parse(tip);
            $("tbody").empty();
            $.each(data, function (idx, obj) {
                $("tbody").append("<tr><td>"+obj[0]+"</td><td>"+obj[1]+"</td><td>"+obj[2]+"</td><td>"+obj[3]+"<td><div class=\"card-body\" style=\"display: inline-flex\"><p class=\"demo\"><button class=\"btn badge-light\">修改</button></p><p class=\"demo\"><button class=\"btn btn-danger\" id="+idx +">删除</button></p></div></td></tr>");
                // $("#province").append("<option value=" + value + ">" + obj.name + "</option>");
                // $("#"+idx).on("click", "#demo", function(){});
            });
        },
        error: function () {

            // $.parser.parse(tip);
            console.log("申请失败");
            window.location = '/index';
        }
    });

});

//下载
$("#look").click(function () {

    window.open("/index/down");
    // window.open ("/index/down", "newwindow2", "height=1000, width=1000, top=500, left=500,toolbar=no, menubar=no, scrollbars=no, resizable=no, location=no, status=no")
});

$("#down").click(function () {

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

//选项
$("#queryDevice").change(function () {

    var a = $(this).prop('selectedIndex');
    $("tbody").empty();
    $.ajax({
        async: false,//同步，异步
        url: "/index/change", //请求的服务端地址
        data: {
            "num": a
        },
        type: "post",
        dataType: "json",
        success: function (data) {
            //成功之后的处理，返回的数据就是 data
            // $.parser.parse(tip);
            $.each(data, function (idx, obj) {
                $("tbody").append("<tr><td>"+obj[0]+"</td><td>"+obj[1]+"</td><td>"+obj[2]+"</td><td>"+obj[3]+"<td><div class=\"card-body\" style=\"display: inline-flex\"><p class=\"demo\"><button class=\"btn badge-light\">修改</button></p><p class=\"demo\"><button class=\"btn btn-danger\" id="+idx +">删除</button></p></div></td></tr>");
                // $("#province").append("<option value=" + value + ">" + obj.name + "</option>");
            });


            console.log("申请成功");
        },
        error: function () {

            // $.parser.parse(tip);
            console.log("申请失败");
            window.location = '/index';
        }

    });

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
