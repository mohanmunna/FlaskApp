import json
from pylib import common_module as cm


def loginAccount(event):

    status = "Success"
    message = "Invalid user"
    returnJson = {}
    userDetails = {}

    try:
        if event:
            if ("username" in event and event["username"]) and ("password" in event and event["password"]):
                selectQry = """SELECT * FROM user where NAME=%s and PASSWORD=%s and USERSTATUS=%s"""
                selectVal = (event["username"], event["password"], "ACTIVE")
                result = cm.selectQuery(selectQry, selectVal)
                if result:
                    for row in result:
                        userDetails["userid"] = row["ID"]
                        userDetails["username"] = row["NAME"]
                        userDetails["usertype"] = row["USERTYPE"]
                        userDetails["apikey"] = row["APIKEY"]
                        message = "Login Succesfully"

                else:
                    status = "Failure"
        else:
            status = "Failure"
            message = "Name / Password is missing"

    except Exception as e:
        status = "Failure"
        message = str(e)

    returnJson = {"status":status, "message":message}
    if userDetails:
        returnJson["userdetail"] = userDetails
    print(returnJson)
    return returnJson


# event = {"name":"Mohan", "password":"pass"}
# login(event)