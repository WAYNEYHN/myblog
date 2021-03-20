$(function () {
    //分页点击
    $('.pages a').click(function () {
        $('.pages a').eq($(this).index()).addClass('active').siblings().removeClass('active');
    });
     
//    var colorList = ['#F65087','#329768','#FB8052','#3693CA','#68C999','#109691'];
	var colorList = ['#100719','#045FB4','#610B4B','#BDBDBD','#FBFBEF','#173B0B'];
    $('.sort li').each(function (i) {
        $(this).css({background:colorList[i%5]});
    });
});


function AjaxSend() {
$.ajax({
    url:'/user/publish',
    type:'POST',
    data:{'title': $("#title").val(),
           "csrfmiddlewaretoken": $("[name = 'csrfmiddlewaretoken']").val()},
    dataType:"JSON",
    success:function (arg) {
        //当服务端处理完成后，返回数据时，该函数自动调用
        //data=服务端返回的值
        if(arg.status){
// {#                    alert("添加成功")#}
// {#                    window.location.reload()#}
//                     location.href="/classes/"
            location.reload()
        }
        else{
            alert(arg.message)
            // $("#errormsg").text(arg.message)
        }
    }
})
}

function signout() {
$.ajax({
    url:'/user/signout',
    type:'GET',
    dataType:"JSON",
    success:function (arg) {
        //当服务端处理完成后，返回数据时，该函数自动调用
        //data=服务端返回的值
        if(arg.status){
// {#                    alert("添加成功")#}
// {#                    window.location.reload()#}
//                     location.href="/classes/"
            location.reload()
        }
        else{
            alert(arg.message)
            // $("#errormsg").text(arg.message)
        }
    }
})
}
