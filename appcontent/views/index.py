# -*- coding: utf-8 -*-
__author__ = 'qi.zhang01'

from flask import Flask
from flask import Flask,jsonify,redirect, url_for, render_template, request, Response,send_from_directory,make_response,send_file
import os, time
from flask import Blueprint
import json

index = Blueprint('index', __name__)
LI = {"0":"质量平台组","1":"内务系统组","2":"快递业务组","3":"数据平台组","4":"电商业务组"}

class data_list():

    LIST_DATA = {"0":{},"1":{},"2":{},"3":{},"4":{}}

@index.route('/index', methods=['GET'])
def indexPage():

    return render_template("index.html",listDate = data_list.LIST_DATA["0"])

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

# 索引
@index.route('/index/run', methods=['post'])
def indexRun():
    if request.method=='POST':
        print("hello")
        data = request.json()
        # print data.get("name")
    return Response("OJBK")

# 保存
@index.route('/index/save', methods=['post'])
def indexSave():
    num = request.form["num"]
    name = request.form["name"]
    future = request.form["future"]
    now = request.form["now"]
    data = data_list.LIST_DATA.setdefault(num,{})
    try:
        l = max(data)
    except:
        l=0
    else:
        l=max(data)+1
    data.update({l:[time.strftime("%Y/%m/%d", time.localtime()),now,future,name]})
    print(data)
    return jsonify(data)

#修改
@index.route('/index/edit', methods=['post'])
def indexEdit():

    num = request.form["num"]
    id1 = request.form["id"]
    name = request.form["name"]
    future = request.form["future"]
    now = request.form["now"]
    data = data_list.LIST_DATA.setdefault(num,{})
    data.update({int(id1):[time.strftime("%Y/%m/%d", time.localtime()),now,future,name]})
    print(data)
    return jsonify(data)

# 删除
@index.route('/index/del', methods=['post'])
def indexDel():
    num = request.form["num"]
    name = request.form["id"]
    data = data_list.LIST_DATA.setdefault(num, {})
    del data[int(name)]
    return jsonify(data)

# select
@index.route('/index/change', methods=['post'])
def indexChange():
    if request.method=='POST':
        name = request.form["num"]

        return jsonify(data_list.LIST_DATA[name])

# 预览
@index.route('/index/see/<num>', methods=['get',"post"])
def indexSee(num):
    a=b=""
    id1 = num[0]
        # directory = os.path.abspath("./../../static/file_dir")
        # file_name = "hh.md"
    ROOT_FOLDER = r"C:\Users\Secret\Desktop\FlaskTest\FlaskAutoTest\static\file_dir\hh.md"
    # print(data_list.LIST_DATA[str(id1)])
    for j,k in data_list.LIST_DATA[str(id1)].items():
        a = a +"&nbsp;&nbsp;"+ str(j+1)+". "+k[2]+";<br>"
        b = b +"&nbsp;&nbsp;"+ str(j+1)+". "+k[3]+";<br>"
    STR = '''<table height="100" width="900" align="center" style="margin-left:2cm"> 
    <tr style="background-color:LightBlue">
        <th height="30" width="160">处室名称</th>
        <th height="30" width="160">小组</th>
        <th height="30" width="560">工作小结</th>
    </tr>
    <tr align="center" style="font-size: 14px">
        <td rowspan="5">武汉研发处</td>
        <td>{0}</td>
        <td align="left">
             【本周工作重点】<br>
             {1}
        <br><br>
             【下周工作计划】<br>
             {2} 
        </td>
    </tr>
    </table>
    '''.format(LI[id1], a, b)
    with open(ROOT_FOLDER,"wb+") as file1:
        file1.write(STR)
    try:
        response = make_response(send_file(ROOT_FOLDER,mimetype='text/html',attachment_filename='hh.md'))
        return response
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)})

# 下载
@index.route('/index/down/<num>', methods=['get',"post"])
def indexDown(num):
    a=b=""
    id1 = num
        # directory = os.path.abspath("./../../static/file_dir")
        # file_name = "hh.md"
    ROOT_FOLDER = r"C:\Users\Secret\Desktop\FlaskTest\FlaskAutoTest\static\file_dir\hh.md"
    # print(data_list.LIST_DATA[str(id1)])
    for j,k in data_list.LIST_DATA[str(id1)].items():
        a = a +"&nbsp;&nbsp;"+ str(j+1)+". "+k[2]+";<br>"
        b = b +"&nbsp;&nbsp;"+ str(j+1)+". "+k[3]+";<br>"
    STR = '''<table height="100" width="900" align="center" style="margin-left:2cm"> 
    <tr style="background-color:LightBlue">
        <th height="30" width="160">处室名称</th>
        <th height="30" width="160">小组</th>
        <th height="30" width="560">工作小结</th>
    </tr>
    <tr align="center" style="font-size: 14px">
        <td rowspan="5">武汉研发处</td>
        <td>{0}</td>
        <td align="left">
             【本周工作重点】<br>
             {1}
        <br><br>
             【下周工作计划】<br>
             {2} 
        </td>
    </tr>
    </table>
    '''.format(LI[id1], a, b)
    with open(ROOT_FOLDER,"wb+") as file1:
        file1.write(STR)
    try:
        response = make_response(send_file(ROOT_FOLDER,mimetype='text/html',attachment_filename='hh.md'))
        return response
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)})


# 下载全部
@index.route('/index/down', methods=['get',"post"])
def indexDownAll():
    STR = '''<table height="100" width="900" align="center" style="margin-left:2cm"> 
        <tr style="background-color:LightBlue">
            <th height="30" width="160">处室名称</th>
            <th height="30" width="160">小组</th>
            <th height="30" width="560">工作小结</th>
        </tr>
        <tr align="center" style="font-size: 14px">
            <td rowspan="5">武汉研发处</td>
            
            
        '''
    a=b=""
        # directory = os.path.abspath("./../../static/file_dir")
        # file_name = "hh.md"
    ROOT_FOLDER = r"C:\Users\Secret\Desktop\FlaskTest\FlaskAutoTest\static\file_dir\hh.md"
    # print(data_list.LIST_DATA[str(id1)])
    for i,j in data_list.LIST_DATA.items():
        for k,l in j.items():
            a = a +"&nbsp;&nbsp;"+ str(k+1)+". "+l[2]+";<br>"
            b = b +"&nbsp;&nbsp;"+ str(k+1)+". "+l[3]+";<br>"
        STR = STR + """<td>{0}</td> <td align="left">
                 【本周工作重点】<br>
                 {1}
            <br><br>
                 【下周工作计划】<br>
                 {2} 
            </td></tr>
            <tr align="center" style="font-size: 14px">
            """.format(LI[i], a, b)
        a = b = ""
    STR = STR+"</tr></table>"
    with open(ROOT_FOLDER,"wb+") as file1:
        file1.write(STR)
    try:
        response = make_response(send_file(ROOT_FOLDER,mimetype='text/html',attachment_filename='hh.md'))
        return response
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)})



if __name__ == "__main__":

    print(os.path.abspath("./../../static/file_dir/hh.md"))
