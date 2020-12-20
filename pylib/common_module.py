import sys
import pymysql
import pymysql.cursors
import json
from pylib import config



def connectDB():
    try:
        conn = pymysql.connect(host=config.db_host, user=config.db_user, passwd=config.db_pswd, db=config.db_name, charset=config.db_charset, cursorclass=pymysql.cursors.DictCursor)
        return conn

    except Exception as e:
        print(e)
        sys.exit()


def selectQuery(query, data):
    conn = connectDB()
    cursor = conn.cursor()
    if data !="":
        print('------------11---------------')
        cursor.execute(query, data)
    else:
        print('------------222---------------')
        cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result


def queryIUD(query, data):
    conn = connectDB()
    insertCursor = conn.cursor()
    print(query)
    print(data)
    if data !="":
        insertCursor.execute(query, data)
    else:
        insertCursor.execute(query)
    conn.commit()
    conn.close()


def getUserDetails(userId):
    userInfo = {}
    conn = connectDB()
    selectQry = """SELECT * FROM user where ID=%s"""
    result = selectQuery(selectQry, userId)
    if result:
        for row in result:
            print(row["ID"])
            userInfo["userid"] = row["ID"]
            userInfo["username"] = row["NAME"]
            userInfo["usertype"] = row["USERTYPE"]
            userInfo["apikey"] = row["APIKEY"]
    return userInfo