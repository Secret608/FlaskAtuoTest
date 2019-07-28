# -*- coding: utf-8 -*-
__author__ = 'qi.zhang01'

from flask import Flask
from flask import Flask, redirect, url_for, render_template, request, Response
import os
from flask import Blueprint

index = Blueprint('index', __name__)

@index.route('/index', methods=['GET'])
def indexPage():
    listDate = ["111111111111111111111111111",2,3]
    return render_template("index.html",listDate = listDate)

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