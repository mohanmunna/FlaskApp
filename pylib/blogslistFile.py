import json
from pylib import common_module as cm


def listBlogs(event):
    
    status = "Success"
    message = "Succesfully Processed"
    returnJson = {}
    blogsList = []
    usrId = ""

    try:
        selectQry = """SELECT * FROM blogposts"""
        if 'userid' in event and event["userid"]:
            selectQry = """SELECT * FROM blogposts where USER_ID=%s"""
            usrId = int(event["userid"])
        result = cm.selectQuery(selectQry, usrId)
        if result:
            for row in result:
                obj = {}
                commentList= []
                obj["postid"] = row["POST_ID"]
                obj["userid"] = row["USER_ID"]
                obj["username"] = row["USER_NAME"]
                obj["title"] = row["TITLE"]
                obj["created_date"] = row["CREATED_DATE"]
                obj["updated_date"] = row["UPDATED_DATE"]
                obj["short_description"] = row["SHORT_DESCRIPTION"]
                obj["long_description"] = row["LONG_DESCRIPTION"]
                obj["image"] = row["IMAGE"]
                
                selectCmntQry = """SELECT * FROM blogcomments where POST_ID=%s"""
                selectCmntData = (int(obj["postid"]))
                commentResult = cm.selectQuery(selectCmntQry, selectCmntData)
                for cmnt in commentResult:
                    print(cmnt)
                    comments = {}
                    comments["cmntid"] = cmnt["ID"]
                    comments["cmntpostid"] = cmnt["POST_ID"]
                    comments["msg"] = cmnt["COMMENT"]
                    comments["cmntupdateddate"] = cmnt["UPDATED_DATE"]
                    comments["cmntuserid"] = cmnt["USER_ID"]
                    comments["cmntusername"] = cmnt["USER_NAME"]
                    commentList.append(comments)
                obj["comments"] = commentList
                blogsList.append(obj)

        else:
            status = "Failure"
            message = "No Blogpost Found.!"

    except Exception as e:
        status = "Failure"
        message = str(e)

    returnJson = {"status":status, "message":message}
    if blogsList:
        returnJson["bloglist"] = blogsList
    return returnJson



# listBlogs('')