/**
 * Created by Administrator on 2021/3/20.
 */
function showModel(){
        document.getElementById("shadow").classList.remove('hide')
        document.getElementById("model").classList.remove('hide')
    }


function cancelModel(){
        document.getElementById("shadow").classList.add('hide')
        document.getElementById("model").classList.add('hide')
    }


function AjaxSend() {
        $.ajax({
            url:'/model_add_class/',
            type:'POST',
            data:{'title': $("#title").val()},
            success:function (data) {
                //当服务端处理完成后，返回数据时，该函数自动调用
                //data=服务端返回的值
                if(data == "ok"){
// {#                    alert("添加成功")#}
// {#                    window.location.reload()#}
//                     location.href="/classes/"
                    location.reload()
                }
                else{
                    $("#errormsg").text(data)
                }
            }
        })
    }



    /**
 * Created by Administrator on 2021/1/16.
 */

function showModel_1(className,cid){
        document.getElementById("shadow").classList.remove('hide')
        document.getElementById("modelToEdit").classList.remove('hide')
        document.getElementById("className").value=className
        document.getElementById("cid").value=cid
}

function AjaxEdit() {
        $.ajax({
            url:"/model_edit_class/",
            type:"POST",
            data:{"cid": $("#cid").val(),
            "cName": $("#className").val()},
            dataType: "JSON",
            success:function(arg){
                // JSON.parse(字符串) =>对象
                // JSON.stringify(对象) => 字符串
                // var arg = JSON.parse(data);
                if(arg.status){
                    // location.href="/classes/"
                    location.reload()
                }
                else{
                    $("#editError").text(arg.message)
                }

            }
        })

}

function AjaxDelete(cid) {
    $.ajax({
        url: "/model_delete_class/",
        type: "POST",
        data: {"cid": cid},
        success: function (data) {
            location.href = "/classes/"
        }
    })
}