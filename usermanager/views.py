import json

import datetime
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from . import forms, models


# Create your views here.
class Register(View):
    def get(self, request):
        return render(request, "usermanager/register.html")

    def post(self, request):
        obj = forms.UserCheck(request.POST)
        if obj.is_valid():
            data = obj.cleaned_data
            username = data['username']
            flag = models.UserInfo.objects.filter(username=username).first()
            if not flag:
                models.UserInfo.objects.create(**data)
                print(obj.cleaned_data['password'])
                return render(request, "usermanager/login.html", {"form": obj})
                # request.session["userinfo"] = {"username": username, "gender": sex}
            else:
                # return redirect("/user/register")
                return render(request, "usermanager/register.html", {"emsg": "用户已存在"})
        else:
            return render(request, "usermanager/register.html", {"error_msg": obj.errors})


class Login(View):
    def get(self, request):
        form = forms.UserCheck()
        return render(request, "usermanager/login.html", {"form": form})

    def post(self, request):
        obj = forms.UserLoginCheck(request.POST)
        print(request.POST.get("password"))
        ret = {"status": 0, 'url': '', 'msg': ''}  # 默认状态
        if obj.is_valid():
            username = obj.cleaned_data['username']
            password = obj.cleaned_data['password']
            flag = models.UserInfo.objects.filter(username=username, password=password).first()
            if flag:
                request.session['userinfo'] = {"username": flag.username, "u_id": flag.id}
                # print(request.path_info)
                return redirect('/liuyan/')
            else:
                ret['msg'] = "用户名或密码错误"
                ret['url'] = "/liuyan/"
                return render(request, "usermanager/jump.html", ret)
                # return render(request, 'usermanager/login.html', {"form": obj})
        else:
            ret['msg'] = "用户名或密码格式错误"
            ret['url'] = "/liuyan/"
            return render(request, "usermanager/jump.html", ret)
            # return render(request, 'usermanager/login.html', {"form": forms})


class SignOut(View):
    def get(self, request):
        ret = {"status":True, "message": None}
        del request.session['userinfo']
        return HttpResponse(json.dumps(ret  ))



class Publish(View):
    def post(self, request):
        ret = {"status": True, "message": None}
        u_id = request.session['userinfo']['u_id']
        content = request.POST.get('title')
        # print(content)
        if len(content) < 3:
            ret["status"] = False
            ret["message"] = "您说的太少了"
            return HttpResponse(json.dumps(ret))
        models.comment.objects.create(usr_id=u_id, content=content, time=datetime.datetime.now())
        return HttpResponse(json.dumps(ret))
