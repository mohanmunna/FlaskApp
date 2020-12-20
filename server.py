from flask import Flask, render_template, request, jsonify
from pylib import config
from pylib import loginFile
from pylib import common_module as cm
from pylib import blogslistFile
from pylib import commentcreateAndupdateFile
from pylib import commentdeleteFile
from pylib import blogcreateANDupdateFile
from pylib import blogdeleteFile
from pylib import signupFile
from pylib import authoriseUser


app = Flask(__name__, static_url_path='/static')


@app.route('/')
@app.route('/login')
def login():
   return render_template('login.html')


@app.route('/signup')
def signup():
   return render_template('signup.html')


@app.route('/createaccount', methods=['POST'])
def createAccount():
    data = request.get_json()
    return signupFile.signup(data)


@app.route('/loginaccount', methods=['POST'])
def loginAccount():
    data = request.get_json()
    print(data)
    return loginFile.loginAccount(data)


@app.route('/blogs')
def blogs():
   return render_template('bloglist.html')


@app.route('/getbloglist', methods=['POST'])
def getBlogList():
    access = False
    if "x-api-key" in request.headers and request.headers["x-api-key"]:
        access = authoriseUser.authorise(request.headers.get('x-api-key'))
    if access:
        data = request.get_json()
        print(data)
        return blogslistFile.listBlogs(data)
    else:
        return {"status":"Failure", "message":"Un Authoriser"}


@app.route('/commentcrud', methods=['POST'])
def addComment():
    access = False
    if "x-api-key" in request.headers and request.headers["x-api-key"]:
        access = authoriseUser.authorise(request.headers.get('x-api-key'))
    if access:
        data = request.get_json()
        print(data)
        return commentcreateAndupdateFile.createAndUpdateComment(data)
    else:
        return {"status":"Failure", "message":"Un Authoriser"}


@app.route('/deletecomment', methods=['POST'])
def deleteComment():
    access = False
    if "x-api-key" in request.headers and request.headers["x-api-key"]:
        access = authoriseUser.authorise(request.headers.get('x-api-key'))
    if access:
        data = request.get_json()
        print(data)
        return commentdeleteFile.deleteComment(data)
    else:
        return {"status":"Failure", "message":"Un Authoriser"}


@app.route('/newblog')
def newBlog():
   return render_template('createandupdateblog.html')    


@app.route('/createblog', methods=['POST'])
def createBlog():
    access = False
    if "x-api-key" in request.headers and request.headers["x-api-key"]:
        access = authoriseUser.authorise(request.headers.get('x-api-key'))
    if access:
        data = request.get_json()
        print(data)
        return blogcreateANDupdateFile.createAndUpdateBlog(data)
    else:
        return {"status":"Failure", "message":"Un Authoriser"}
    

@app.route('/updateblog')
def updateBlog():
   return render_template('updateBlog.html')


@app.route('/deleteblog', methods=['POST'])
def deleteBlog():
    access = False
    if "x-api-key" in request.headers and request.headers["x-api-key"]:
        access = authoriseUser.authorise(request.headers.get('x-api-key'))
    if access:
        data = request.get_json()
        print(data)
        return blogdeleteFile.deleteBlog(data)
    else:
        return {"status":"Failure", "message":"Un Authoriser"}


@app.route('/myaccount')
def myAccount():
   return render_template('myAccount.html')


@app.route('/blogdetail')
def blogDetail():
   return render_template('blogdetail.html')

if __name__ == '__main__':
   app.run(debug=True,host='127.0.0.1',port=5000)