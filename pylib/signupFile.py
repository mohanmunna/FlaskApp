import uuid 
from pylib import common_module as cm



def signup(event):

    status = "Success"
    message = "Name Already Used"
    returnJson = {}
    
    try:
        if event:
            if ("username" in event and event["username"]) and ("password" in event and event["password"]):
                username = event["username"]
                password = event["password"]
                apikey = uuid.uuid4().hex
                selectQry = """SELECT * FROM user where NAME=%s"""
                result = cm.selectQuery(selectQry, username)

                accType = "USER"
                if username.lower() == "admin":
                    accType = "ADMIN"
                    
                if not result:
                    insertQry = "INSERT INTO user (NAME, PASSWORD, USERTYPE, APIKEY, USERSTATUS) VALUES (%s, %s, %s, %s, %s)"
                    insertVal = (username, password, accType, str(apikey), "ACTIVE")
                    cm.queryIUD(insertQry, insertVal)
                    message = "Successfully Processed"
                else:
                    status = "Failure"
        else:
            status = "Failure"
            message = "Name / Password is missing"

    except Exception as e:
        status = "Failure"
        message = str(e)

    returnJson = {"status":status, "message":message}
    print(returnJson)
    return returnJson




# event = {"name":"mohanmunna31", "password":"pass"}
# signup(event)

