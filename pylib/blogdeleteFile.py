import json
from pylib import common_module as cm


def deleteBlog(event):
    
    status = "Success"
    message = "Successfully Deleted"
    returnJson = {}

    try:
        if event and ('userid' in event and event["userid"]) and 'postid' in event and event["postid"]:
            deleteQry = """DELETE FROM blogposts WHERE POST_ID=%s and USER_ID=%s"""
            deleteVal = (event["postid"], event["userid"])
            cm.queryIUD(deleteQry, deleteVal)

            deleteCommentsQry = """DELETE FROM blogcomments WHERE POST_ID=%s and USER_ID=%s"""
            deleteCommentsVal = (event["postid"], event["userid"])
            cm.queryIUD(deleteCommentsQry, deleteCommentsVal)

        else:
            status = "Failure"
            message = "Pleae try again!"

    except Exception as e:
        status = "Failure"
        message = str(e)

    returnJson = {"status":status, "message":message}
    print(returnJson)
    return returnJson



    
# event = {"userid":3, "postid":5}    
# deleteBlog(event)