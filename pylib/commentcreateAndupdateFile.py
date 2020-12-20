import json
from datetime import datetime
from pylib import common_module as cm



def createAndUpdateComment(event):

    print(event)
    
    status = "Success"
    message = "Successfully created"
    returnJson = {}
    updateBlog = False

    try:
        if event and ("postid" in event and event["postid"]) and ("comment" in event and event["comment"]):
            currentDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if "id" in event and event["id"]:
                updateBlog = True

            if updateBlog:
                insertQry = """UPDATE blogcomments SET COMMENT=%s, UPDATED_DATE=%s where ID=%s and USER_ID=%s and POST_ID=%s"""
                insertVal = (event["comment"], currentDate, event["id"], event["userid"], event["postid"])
                cm.queryIUD(insertQry, insertVal) 
            else:
                insertQry = """INSERT INTO blogcomments (POST_ID, COMMENT, UPDATED_DATE, USER_ID, USER_NAME) VALUES (%s, %s, %s, %s, %s)"""
                insertVal = (event["postid"], event["comment"], currentDate, event["userid"], event["username"])
                cm.queryIUD(insertQry, insertVal) 

        else:
            status = "Failure"
            message = "Failed to update!"
            
    except Exception as e:
        status = "Failure"
        message = str(e)

    returnJson = {"status":status, "message":message}
    print(returnJson)
    return returnJson




# event = {"postid":5, "comment": "test", "userid":3, "id":5, "username":"mohanmunna"}
# createAndUpdateComment(event)