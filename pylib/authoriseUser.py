import json
from pylib import common_module as cm


def authorise(apikey):

    access = False
    try:

        if apikey:
            selectQry = """SELECT * FROM user where APIKEY=%s"""
            selectVal = (str(apikey))
            result = cm.selectQuery(selectQry, selectVal)
            if result:
                access = True

    except Exception as e:
        print(str(e))

    return access
