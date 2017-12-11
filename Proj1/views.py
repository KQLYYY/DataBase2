# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
import MySQLdb
import csv
import random
import codecs
import json
import MySQLdb as mdb


random.seed()

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def lab2(request):
    table_name = 'order'
    db = MySQLdb.connect(host="localhost", user="root", passwd="MySql12321", db="mydb")
    cur = db.cursor()
    cur.execute("SELECT * FROM mydb." + table_name)
    rows = cur.fetchall()
    desc = cur.description
    cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE `TABLE_NAME` = '" + table_name + "' AND `TABLE_SCHEMA` = 'projects'")
    cols = cur.fetchall()
    db.close()
    return render(request,'show.html',locals())

def show(request):
    if request.method == "POST":
        table_name = request.POST['table_name']
        db = MySQLdb.connect(host="localhost" , user="root" , passwd="MySql12321" , db="mydb")
        cur = db.cursor()
        cur.execute("SELECT * FROM mydb."+table_name)
        rows = cur.fetchall()
        desc = cur.description
        cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE `TABLE_NAME` = '"+table_name+"' AND `TABLE_SCHEMA` = 'projects'")
        cols = cur.fetchall()
        cur.execute("SELECT * FROM mydb.order")
        order = cur.fetchall()
        cur.execute("SELECT * FROM product")
        product = cur.fetchall()
        cur.execute("SELECT * FROM client")
        client = cur.fetchall()
        cur.execute("SELECT * FROM store")
        store = cur.fetchall()
        db.close()
    return render(request,'show.html',locals())

def delete(request):
    if request.method == "POST":
        row_id = request.POST['row_id']
        db = MySQLdb.connect(host="localhost" , user="root" , passwd="MySql12321" , db="mydb")
        cur = db.cursor()
        cur.execute("DELETE FROM `mydb`.`order` WHERE `idOrder` = "+row_id[1:3])
        db.commit()
        db.close()
    return redirect('/lab2')

def create(request):
    db = MySQLdb.connect(host="localhost", user="root", passwd="MySql12321", db="mydb")
    cur = db.cursor()
    cur.execute("SELECT * FROM mydb.product")
    rows = cur.fetchall()
    cur.execute("SELECT * FROM mydb.client")
    rows1 = cur.fetchall()
    cur.execute("SELECT * FROM mydb.store")
    rows2 = cur.fetchall()
    db.close()
    return render(request,'sh.html',locals())

def add(request):
    if request.method == "POST":
        db = MySQLdb.connect(host="localhost", user="root", passwd="MySql12321", db="mydb")
        cur = db.cursor()
        rows = request.POST['row_id']
        rows1 = request.POST['row1_id']
        rows2 = request.POST['row2_id']
        cur.execute("SELECT Name FROM mydb.product WHERE idProduct =" + rows[1:2])
        cur.execute("INSERT INTO `mydb`.`order` (`idOrder`, `Date`, `Amount`, `Cost`, `Product_idProduct`, `Store_idStore`, `Client_idClient`) VALUES('%s','2010/10/10','1','%s','%s','%s','%s')" % (random.randint(10,100),rows[-4:-2], rows[1:2], rows2[1:2], rows1[1:2]))
        db.commit()
        db.close()
    return redirect('/lab2')

def load(request):
    con = mdb.connect('localhost', 'root', 'MySql12321', 'mydb')
    f = open('DB.json', 'r')
    json_string = f.read()
    parsed_string = json.loads(json_string)

    with con:
        cur = con.cursor()
        i = 0
        while i < 5:
            cur.execute("INSERT INTO Store(IdStore, Name, Adress, Email) VALUES(%d,'%s','%s','%s')" %(parsed_string["Store"][i]["idStore"],parsed_string["Store"][i]["Name"],parsed_string["Store"][i]["Adress"],parsed_string["Store"][i]["Email"]))
            cur.execute("INSERT INTO Client(idClient, FName, SurName, PhoneNumber, Adress) VALUES(%d,'%s','%s','%s','%s')" % (parsed_string["Client"][i]["idClient"],parsed_string["Client"][i]["FName"],parsed_string["Client"][i]["SurName"],parsed_string["Client"][i]["PhoneNumber"],parsed_string["Client"][i]["Adress"]))
            cur.execute("INSERT INTO Product(idProduct,Name,Manufacturer,ManufacturerCountry,Category,Type,Capacity,Price) VALUES(%d,'%s','%s','%s','%s','%s','%s','%s')" % (parsed_string["Product"][i]["idProduct"],parsed_string["Product"][i]["Name"],parsed_string["Product"][i]["Manuf"],parsed_string["Product"][i]["ManufCountry"],parsed_string["Product"][i]["Category"],parsed_string["Product"][i]["Type"],parsed_string["Product"][i]["Capacity"],parsed_string["Product"][i]["Price"]))
            i+=1
    return redirect('/lab2')

def update(request):
        db = MySQLdb.connect(host="localhost" , user="root" , passwd="MySql12321" , db="mydb")
        cur = db.cursor()
        cur.execute("SELECT * FROM mydb.product")
        rows = cur.fetchall()
        cur.execute("SELECT * FROM mydb.client")
        rows1 = cur.fetchall()
        cur.execute("SELECT * FROM mydb.store")
        rows2 = cur.fetchall()
        cur.execute("SELECT * FROM mydb.order")
        rows3 = cur.fetchall()
        db.close()
        return render(request,'update.html',locals())

def onl(request):
    if request.method == "POST":
        db = MySQLdb.connect(host="localhost", user="root", passwd="MySql12321", db="mydb")
        cur = db.cursor()
        rows = request.POST['row_id']
        rows1 = request.POST['row1_id']
        rows2 = request.POST['row2_id']
        rows3 = request.POST['row3_id']
        #print rows3[1:3] ,'\n', rows[1:2],'\n', rows1,'\n', rows2
    con = mdb.connect('localhost', 'root', 'MySql12321', 'mydb')
    with con:
        cur = con.cursor()
        cur.execute("UPDATE mydb.order SET Product_idProduct = "+ rows[1:2] +" WHERE idOrder = " + rows3[1:3])
        cur.execute("UPDATE `mydb`.`order` SET `Store_idStore` = "+ rows2[1:2] +" WHERE `idOrder` = " + rows3[1:3])
        cur.execute("UPDATE `mydb`.`order` SET `Client_idClient` = "+ rows1[1:2] +" WHERE `idOrder` = " + rows3[1:3])
    con.close()
    return redirect('/lab2')

def searchdigit(request):
    if request.method == "POST":
        db = MySQLdb.connect(host="localhost", user="root", passwd="MySql12321", db="projects")
        cur = db.cursor()
        cur.execute("SELECT * FROM `mydb`.`order` WHERE `idOrder` >= '" + request.POST['start'] + "' AND `idOrder` <= '" + request.POST['end'] +"'")
        rows = cur.fetchall()
        db.close()
        return render(request,'show.html',locals())
    else:
        return redirect('/lab2')