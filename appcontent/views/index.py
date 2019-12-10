# -*- coding: utf-8 -*-
__author__ = 'qi.zhang01'

from flask import Flask
from flask import Flask, redirect, url_for, render_template, request, Response
import os, time
from flask import Blueprint
import json

index = Blueprint('index', __name__)

LIST_DATA = []

@index.route('/index', methods=['GET'])
def indexPage():

    return render_template("index.html",listDate = LIST_DATA)

@index.route('/forms', methods=["GET", 'POST'])
def forms():
    return render_template("forms.html")

@index.route('/tables', methods=["GET", 'POST'])
def tables():
    return render_template("tables.html")

@index.route('/components', methods=["GET", 'POST'])
def components():
    return render_template("components.html")

@index.route('/notifications', methods=["GET", 'POST'])
def notifications():
    return render_template("notifications.html")

@index.route('/typography', methods=["GET", 'POST'])
def typography():
    return render_template("typography.html")


@index.route('/icons', methods=["GET", 'POST'])
def icons():
    return render_template("icons.html")


@index.route('/index/run', methods=['post'])
def indexRun():
    if request.method=='POST':
        print("hello")
        data = request.json()
        print data.get("name")
    return Response("OJBK")


@index.route('/index/save', methods=['post'])
def indexSave():
    if request.method=='POST':
        name = request.form["name"]
        future = request.form["future"]
        now = request.form["now"]
        if  future or  now:
            LIST_DATA.append((time.strftime("%Y/%m/%d", time.localtime()),now,future,name))
    return Response("OJBK")


@index.route('/index/del', methods=['post'])
def indexDel():
    if request.method=='POST':
        name = request.form["id"]
        for i in LIST_DATA:
            if i[0] == str(name):
                print(LIST_DATA)
                LIST_DATA.remove(i)
    return Response("OJBK")