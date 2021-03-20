from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse


# class MD1(MiddlewareMixin):
#
#     def process_request(self, request):
#         # print(request.path_info)
#         print('我是MD1的process_request')
#
#     def process_response(self, request, response):
#         print('我是MD1的process_response')
#         return response


class MD1(MiddlewareMixin):  # 验证登录
    # white_list = ['/liuyan/', '/index/', '/pageAjax/', '', '/about/', '/learn/*', '/slowlife/']  # 白名单
    black_list = ['/user/publish', '/about/']  # 黑名单
    ret = {"status": 0, 'url': '', 'msg': ''}  # 默认状态

    def process_request(self, request):  # 请求之前
        request_url = request.path_info  # 获取请求路径
        # get_full_path()表示带参数的路径
        # print(request.path_info, request.get_full_path())
        # 黑名单的网址限制访问
        if request.session.get("userinfo"):
            return None

        # 白名单的网址或者登陆用户不做限制
        # 判断是否在白名单内或者已经有了session(表示已经登录了)
        elif request_url in self.black_list:
            self.ret['msg'] = "请登录后,再访问!"
            self.ret['url'] = "/user/login/"
        else:
            return None
            # self.ret['msg'] = "请登录后,再访问!"
            # self.ret['url'] = "/liuyan/"

        # 错误页面提示
        return render(request, "usermanager/jump.html", self.ret)