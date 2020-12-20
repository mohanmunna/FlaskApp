import json
from datetime import datetime
from pylib import common_module as cm


def createAndUpdateBlog(event):
    
    status = "Success"
    message = "Successfully created"
    returnJson = {}

    title = ""
    short_des = ""
    username = ""
    long_des = ""
    image = None
    updateBlog = False

    try:
        if event and 'userid' in event and event["userid"]:
            currentDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if 'username' in event:
                username = event["username"]
            if 'title' in event:
                title = event["title"]
            if 'short_description' in event:
                short_des = event["short_description"]
            if 'long_description' in event:
                long_des = event["long_description"]
            if 'image' in event:
                image = event["image"]

            if "postid" in event and event["postid"]:
                updateBlog = True

            if updateBlog:
                insertQry = """UPDATE blogposts SET TITLE=%s, UPDATED_DATE=%s, SHORT_DESCRIPTION=%s, LONG_DESCRIPTION=%s, IMAGE=%s where USER_ID=%s and POST_ID=%s"""
                insertVal = (title, currentDate, short_des, long_des, image, event["userid"], event["postid"])
                cm.queryIUD(insertQry, insertVal) 
            else:
                insertQry = """INSERT INTO blogposts (TITLE, CREATED_DATE, UPDATED_DATE, USER_NAME, USER_ID, SHORT_DESCRIPTION, LONG_DESCRIPTION, IMAGE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                insertVal = (title, currentDate, currentDate, username, event["userid"], short_des, long_des, image)
                cm.queryIUD(insertQry, insertVal)    

        else:
            status = "Failure"
            message = "Pleae try again!"

    except Exception as e:
        status = "Failure"
        message = str(e)

    returnJson = {"status":status, "message":message}
    print(returnJson)
    return returnJson


    
# event = {"userid":1, "postid":7, "username":"Mohan", "title":"New", "short_description":"First blog in the my sql db",
# "long_description":"His promotion and swift"}
# createAndUpdateBlog(event)