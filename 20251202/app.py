from flask import Flask

app = Flask(__name__) # Initializind the Flask application or Flask Container

@app.route('/') #https://127.0.0.0:5000
#Define function jusr below decorator mean when user going to visit above URL, below function will triggered
def greeting():
    return "<h1> Welcome to Flask!</h1>"


if __name__ == '__main__':
    app.run(debug=True)

