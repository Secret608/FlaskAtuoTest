# -*- coding: utf-8 -*-
__author__ = 'qi.zhang01'

from flask import Flask
from flask import Flask,jsonify,redirect, url_for, render_template, request, Response,send_from_directory,make_response,send_file
import os, time
from flask import Blueprint
import json

index = Blueprint('index', __name__)

class data_list():

    LIST_DATA = []
    LIST_NUM = 0

@index.route('/index', methods=['GET'])
def indexPage():

    return render_template("index.html",listDate = data_list.LIST_DATA)

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
    return render_template("index.html")


@index.route('/index/run', methods=['post'])
def indexRun():
    if request.method=='POST':
        print("hello")
        data = request.json()
        # print data.get("name")
    return Response("OJBK")


@index.route('/index/save', methods=['post'])
def indexSave():

    if request.method=='POST':
        name = request.form["name"]
        future = request.form["future"]
        now = request.form["now"]
        if  future or now:
            data_list.LIST_NUM = data_list.LIST_NUM + 1
            data_list.LIST_DATA.append([data_list.LIST_NUM, time.strftime("%Y/%m/%d", time.localtime()),now,future,name])

    return Response("OJBK")


@index.route('/index/del', methods=['post'])
def indexDel():
    if request.method=='POST':
        name = request.form["id"]
        for i in data_list.LIST_DATA:
            if i[0] == int(name):
                print(i)
                data_list.LIST_DATA.remove(i)
    return Response("OJBK")

@index.route('/index/down', methods=['get'])
def indexDown():
    a=b=""
    if request.method=='GET':

        directory = os.path.abspath("./../../static/file_dir")
        file_name = "hh.md"
        ROOT_FOLDER = r"C:\Users\Secret\Desktop\FlaskTest\FlaskAutoTest\static\file_dir\hh.md"

        for i in data_list.LIST_DATA:
            a = a +"&nbsp;&nbsp;"+ str(data_list.LIST_DATA.index(i)+1)+". "+i[2]+";<br>"
            b = b +"&nbsp;&nbsp;"+ str(data_list.LIST_DATA.index(i)+1)+". "+ i[3]+";<br>"
        STR = '''
        <table height="100" width="900" align="center" style="margin-left:2cm"> 
            <tr style="background-color:LightBlue">
                <th height="30" width="160">处室名称</th>
                <th height="30" width="160">小组</th>
                <th height="30" width="560">工作小结</th>
            </tr>
            <tr align="center" style="font-size: 14px">
                <td rowspan="5">武汉研发处</td>
                <td>质量平台组</td>
                <td align="left">
                     【本周工作重点】<br>
                     {0}
                <br><br>

                     【下周工作计划】<br>
                     {1} 
                </td>
            </tr>
        </table>
        '''.format(a, b)
        with open(ROOT_FOLDER,"wb+") as file1:
            file1.write(STR)
        try:
            response = make_response(send_file(ROOT_FOLDER,mimetype='text/html',attachment_filename='hh.md'))
            return response
        except Exception as e:
            return jsonify({"code": "异常", "message": "{}".format(e)})


if __name__ == "__main__":

    print(os.path.abspath("./../../static/file_dir/hh.md"))
