# -*- coding: utf-8 -*-
__author__ = 'qi.zhang01'

from flask import Flask
from flask import Flask, redirect, url_for, render_template, request, Response
import os, time
from flask import Blueprint

login = Blueprint('login', __name__)

@login.route('/')
def loginIndex():
    return render_template("login.html")

@login.route('/login', methods=['POST', "GET"])
def loginInto():
    if request.method == 'POST':
        result = request.form
        if result.get("username") == "Admin" and result.get("password") == "111111":
            listDate = [
                        ("HM_ECG", u"心电Smoke", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())),
                        ("HM_INS", u"检验Smoke", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())),
                        ("HM_CLT", u"会诊Smoke", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())),
                        ("HM_RFR", u"转诊Smoke", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())),
                        ("HM_RSV", u"预约Smoke", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())),
                        ("HM_TNG", u"门诊Smoke", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())),
                        ]
            return render_template("index.html", listDate=listDate)
        else:
            return render_template("login.html", error_msg=u"大哥看不见黄色字吗？")
    else:
        return redirect(url_for('login.loginIndex'))

#app.add_url_rule(‘/’, hello_world).

# @login.route('/timg', methods=['GET'])
# def loginImage():
#     path = os.path.abspath(r"./static/timg.jpg")
#     print path
#     f = open(path, "rb")
#     return Response(f)

@login.route('/timg')
def loginImage():
    return url_for('static', filename='timg.jpg')

