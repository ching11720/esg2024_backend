from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
import MySQLdb
from django.http import HttpResponse

def connect_db():
    db = MySQLdb.connect(host="esg_mysql",
            user="user", passwd="carbon2024",
            db="carbon", charset="utf8")
    return db


class boundary():
    def Post(request):
        name = request.Post['Name']
        addr = request.Post['address']
        type = request.Post['type']
        
        db = connect_db()
        cursor = db.cursor()
        
        cnt = 'SELECT COUNT(*) FROM borders'
        cursor.execute(cnt)
        cnt_result = cursor.fetchone()[0]
        bid = '05' + postal_code + str(cnt_result).zfill(3)
        insertion = 'INSERT INTO borders VALUES ({}, {}, {})'.format()
        cursor.execute(insertion)
        db.commit()
        db.close()
        return HttpResponse(bid)

    def Revise(request):
        if(request.method == 'POST'):
            bid = request.Post['BID']
            addr = request.Post['address']
            db = connect_db()
            cursor = db.cursor()
            revision = 'UPDATE FROM borders SET address = {} WHERE BID = {}'.format(addr, bid)
            cursor.execute(revision)
            retrieve = 'SELECT * FROM borders WHERE BID = {}'.format(bid)
            cursor.execute(retrieve)
            result = cursor.fetchall()
            db.commit()
            db.close()
            return HttpResponse(result)
    
    def Delete(request):
        if(request.method == 'DELETE'):
            bid = request.Post['BID']
            db = connect_db()
            cursor = db.cursor()
            delete = 'UPDATE FROM borders SET status = 0 WHERE BID = {}'.format(bid)
            cursor.execute(delete)
            db.commit()
            db.close()
            return HttpResponse('success')
    
    def retrieve(request):
        if(request.method == 'GET'):
            conditions = [request.Post['BID'], request.Post['name'], request.Post['type']]
            db = connect_db()
            cursor = db.cursor()
            retrieve = 'SELECT * FROM borders WHERE 1=1'
            param = []
            if request.Post['BID'] is not None:
                retrieve += ' AND BID = %s'
                param.append(conditions[0])
            if request.Post['name'] is not None:
                retrieve += ' AND name = %s'
                param.append(conditions[1])
            if request.Post['type'] is not None:
                retrieve += ' AND type = %s'
                param.append(conditions[2])
            cursor.execute(retrieve, param)
            result = cursor.fetchall()
            db.close()
            return HttpResponse(result)

class source():
    def Post(request):
        ename = request.Post['EName']
        form = request.Post['Form']
        mname = request.Post['MName']
        cat = request.Post['Category']
        
        db = connect_db()
        cursor = db.cursor()
        
        insertion = 'INSERT INTO borders VALUES ({}, {}, {})'.format()
        cursor.execute(insertion)
        db.commit()
        db.close()
        return HttpResponse(bid)
    def revise():
    def delete():
    def retrieve():


class statement():
    def retrieve():
    def Export():
    
class audit():
    def internal_audit():
    def external_audit():
"""
