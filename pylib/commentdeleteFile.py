import json
from pylib import common_module as cm

def deleteComment(event):
    
    status = "Success"
    message = "Successfully Deleted"
    returnJson = {}

    try:
        if event and ('userid' in event and event["userid"]) and 'postid' in event and event["postid"] and 'id' in event and event['id']:
            deleteCommentsQry = """DELETE FROM blogcomments WHERE POST_ID=%s and USER_ID=%s and ID=%s"""
            deleteCommentsVal = (event["postid"], event["userid"], event['id'])
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



    
# event = {"userid":1, "postid":6, 'id':2}    
# deleteBlog(event)