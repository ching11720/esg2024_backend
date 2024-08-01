from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import random, string
from django.contrib.auth.models import Group
import MySQLdb
from django.http import HttpResponse
import datetime
import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

def connect_db():
    db = MySQLdb.connect(host="esg_mysql",
            user="user", passwd="carbon2024",
            db="carbon", charset="utf8")
    return db

def create_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        permission = request.POST["Access"]
        
        # produce random password
        digits = string.digits
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        rdpassword = random.sample(digits, 3) + random.sample(upper, 3) + random.sample(lower, 4)
        random.shuffle(rdpassword)
        rdpassword = ''.join(rdpassword)

        # create user
        user = User.objects.create_user(username, password="testpswd") # for testing, not the randomized one

        # add user into groups for permission
        permissions = permission.split(", ")
        for x in permissions:
            gp = Group.objects.get(name=x) 
            gp.user_set.add(user)

        # i want to put user into users table but there is no name in users
        # after that do work_on
        db = connect_db()
        cursor = db.cursor()
        search = 'SELECT * FROM employees WHERE `name` = "{}"'.format(username)
        data = cursor.fetchone()
        un = data[1]
        uid = data[0]
        insertion = 'INSERT INTO users VALUES ("{}", "{}", "{}");'.format(uid, ) 

        message = "User Created\nUsername: " + username +"\nPassword: " + rdpassword
        messages.success(request, message)
    return render(request, 'create_user.html')
    # return HttpResponse([uid, rdpassword])


def create_project(request):
    if request.method == 'POST':
        project_name = request.POST["projectName"]
        PMID = request.POST["PMID"]
        Material = request.POST["Material"]
        Equipment = request.POST["Equipment"]
        flow = 'flow' 

        db = connect_db()
        cursor = db.cursor()
        
        # TABLE `projects`
        date = datetime.datetime.now()
        y = str(date.year)
        m = date.month
        cnt = "SELECT * FROM projects ORDER BY CAST(PID AS INT) DESC"
        cursor.execute(cnt)
        last_one = cnt.fetchone()
        last_pid = last_one[0]
        last_m = int(last_pid[4:6])
        PID = '01' + y[2:4] + str(m)
        if(m == last_m):
            num = int(last_pid[6:])
            no = str(num).zfill(2)
            PID += no
        else:
            PID += '00'
        insertion = 'INSERT INTO porjects (PID, pname, flow, PMID) VALUES ("{}", "{}", "{}", "{}");'.format(PID, project_name, flow, PID) 
        cursor.execute(insertion)
        
        # usage_e
        eqs = Equipment.split(', ')
        for x in eqs:
            insertion = 'INSERT INTO usage_e VALUES("{}", "{}")'.format(PID, x)
            cursor.execute(insertion)
        
        # usage_m
        ms = Material.split(', ')
        for x in ms:
            insertion = 'INSERT INTO usage_m VALUES("{}", "{}")'.format(PID, x)
            cursor.execute(insertion)
        
        db.commit()
        db.close()
        
        # create group for the project
        group = Group.objects.create(name=project_name)

"""
def Accept_Record_Revise():

def Reject_Record_Revise():
"""


def employee_management(request):
    return render(request, 'employee.html')

def employee(request):
    # POST
    if request.method == 'POST':
        name = request.POST["name"]
        gender = request.POST["gender"]
        phone = request.POST["phone"]
        mail = request.POST["mail"]
        region = request.POST["region"]
        pID = request.POST["pID"] # 預設是Null
            
        db = db = connect_db()
        cursor = db.cursor()
            
        date = datetime.datetime.now()
        y = str(date.year)
        m = str(date.month)
        cnt = 'SELECT COUNT(*) FROM employees'
        cursor.execute(cnt)
        cnt_result = cursor.fetchone()[0]
        eid = '02' + y + m + str(cnt_result).zfill(4)
        insertion = 'INSERT INTO `employees` VALUES ("{}", "{}", "{}", "{}", "{}", "{}");'.format(eid, name, gender, mail, phone, region) 
        cursor.execute(insertion)
            
        db.commit()
        db.close()
        return JsonResponse({"message": f"Added employee with name {name}"})
    # REVISE
    elif request.method == 'PUT':
        EID = request.PUT["EID"]
        newname = request.PUT["name"]
        newgender = request.PUT["gender"]
        newphone = request.PUT["phone"]
        newmail = request.PUT["mail"]
        newregion = request.PUT["region"]
        newpID = request.PUT["pID"] # 預設是null work_on
            
        db = connect_db()
        cursor = db.cursor()
        revision = 'UPDATE `employees` SET `name`="{}", `gender`="{}", `phone`="{}", `mail`="{}", `nation`="{}", `pID`="{}" WHERE `EID`="{}"'.format(newname, newgender, newphone, newmail, newregion, newpID, EID)
        cursor.execute(revision)
        db.commit()
        db.close()
        return JsonResponse({"message": f"Updated employee with ID {id} to name {name}"})
    # DELETE
    elif request.method == 'DELETE':
        EID = request.Delete['EID']
        name = request.Delete['name']
        db = connect_db()
        cursor = db.cursor()
        delete = "UPDATE FROM employees SET status = 0 WHERE EID = '{}'".format(EID)
        cursor.execute(delete)
        db.commit()
        db.close()
        return JsonResponse({"message": f"Deleted employee with ID {id}"})
    # RETRIEVE
    elif request.method == 'GET':
        conditions = [request.GET["EID"], request.GET["name"], request.GET["region"], request.GET["pID"]]
        """
        EID = request.PUT["EID"]
        retrieve_name = request.PUT["name"]
        retrieve_region = request.PUT["region"]
        retrieve_PID = request.PUT["pID"]
        """
        db = connect_db()
        cursor = db.cursor()
        retrieve = 'SELECT * FROM employees WHERE 1=1'
        param = []
        if request.Post['EID'] is not None:
            retrieve += ' AND EID = %s'
            param.append(conditions[0])
        if request.Post['name'] is not None:
            retrieve += ' AND name = %s'
            param.append(conditions[1])
        if request.Post['region'] is not None:
            retrieve += ' AND nation = %s'
            param.append(conditions[2])
        cursor.execute(retrieve, param)
        result = cursor.fetchall()
        if request.Post['pID'] is not None:
            retrieve = 'SELECT * FROM works_on WHERE PID = {}'.format(request.Post['pID'])
            cursor.execute(retrieve)
            result2 = cursor.fetchall()
        fresult = []
        for x in result:
            if x in result2:
                fresult.append(x)
        return JsonResponse(employees, safe=False)
    else:
        return HttpResponseNotAllowed(['GET', 'POST', 'PUT', 'DELETE'])

# def Log():

"""
1. how to generate PID
2. create_project doesn't take flow and UID now
3. create_project takes eq and m now but db doesn't store them
4. now table for borders and factors and source now
5. does revise employee send everything?
6. mark as delete?
7. haven't deal with permission

pid  01yymmnn 生成當下的日期 00~99同月份
uid == eid
eid  02yyyymmnnnn 總數量
eqid 03yyyymm(報廢)nnnn 總數量
mid  04yyyymm(進貨)yy(年限)nnnn 總數量 
bid  05xxxxxx(郵遞區號 前面補0)nnn 總數量
sid == mid
"""

"""
1. 先有employee才有user
2. db沒有username
"""

