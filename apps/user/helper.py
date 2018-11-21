import hashlib
from django.conf import settings
from django.shortcuts import redirect


def set_password(password):
    # 对密码进行加密
    newPassword = "{}{}".format(password, settings.SECRET_KEY)
    h = hashlib.md5(newPassword.encode('utf-8'))
    return h.hexdigest()


def set_session(request, username):
    """
    设置session
    :param request:
    :param username:
    :return:
    """
    request.session["user_id"] = username.pk


def old_request(old_def):
    """
    session函数,验证是否登录
    :param old_def:
    :return:
    """
    def new_def(request, *args, **kwargs):
        if request.session.get("user_id") is None:
            # 没有登录跳转页面
            return redirect("user:登录")
        else:
            return old_def(request, *args, **kwargs)

    return new_def