from flask import Flask

app = Flask(__name__) # Initializind the Flask application or Flask Container

@app.route('/') #https://127.0.0.0:5000
#Define function jusr below decorator mean when user going to visit above URL, below function will triggered
def greeting():
    return "<h1> Welcome to Flask!</h1>"

username = "Romison" 

@app.route('/user')  #https://127.0.0.0:5000/user
def user():
    return f"<h1>Welcome New User: {username}</h1>"


@app.route('/user1/<username>')  #https://127.0.0.0:5000/user1/john
def user1(username):
    return f"<h1>Welcome: {username}</h1>"

@app.route('/user2/<username>')  #https://127.0.0.0:5000/user2/jass
def user2(username):
    return f"<h1>Welcome: {username}</h1>"

@app.route('/eligible/<int:age>')  #https://127.0.0.0:5000/ueligible/15
def eligible(age):
    return f"<h1>Age is {age} and {username} is <font-color=green>eligible</font-color></h1>"

@app.route('/noteligible/<int:age>')  #https://127.0.0.0:5000/noteligible/15
def noteligible(age):
    return f"<h1>Age is {age} and {username} is <font-color=red>not eligible</font-color></h1>"

if __name__ == '__main__':
    app.run(debug=True)


