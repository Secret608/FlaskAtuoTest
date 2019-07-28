# -*- coding: utf-8 -*-
__author__ = 'qi.zhang01'

from flask import Flask
from flask import Flask, redirect, url_for, render_template, request, Response
import os, time
from flask import Blueprint

index = Blueprint('index', __name__)

LIST_DATA = [
        ("HM_ECG", u"心电Smoke", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())),
        ("HM_INS", u"检验Smoke", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())),
        ("HM_CLT", u"会诊Smoke", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())),
        ("HM_RFR", u"转诊Smoke", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())),
        ("HM_RSV", u"预约Smoke", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())),
        ("HM_TNG", u"门诊Smoke", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())),
    ]

@index.route('/index', methods=['GET'])
def indexPage():

    return render_template("index.html",listDate = LIST_DATA)

@index.route('/forms', methods=["GET", 'POST'])
def forms():
    return render_template("index.html")

@index.route('/tables', methods=["GET", 'POST'])
def tables():
    return render_template("index.html")

@index.route('/components', methods=["GET", 'POST'])
def components():
    return render_template("index.html")

@index.route('/notifications', methods=["GET", 'POST'])
def notifications():
    return render_template("index.html")

@index.route('/typography', methods=["GET", 'POST'])
def typography():
    return render_template("index.html")


@index.route('/icons', methods=["GET", 'POST'])
def icons():
    return render_template("icons.html")


@index.route('/index/run', methods=['post'])
def indexRun():
    if request == "POST":
        data = request.json()
        print data.get("name")
    return Response("OJBK")