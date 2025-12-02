from flask import Flask

app = Flask(__name__) # Initializind the Flask application or Flask Container

@app.route('/')

def greeting():
    return "<h1>Welcome</h1>"


@app.route('/voting/<int:age>') #https://127.0.0.0:5000
def voting(age):
    voting=""
    if age > 18:
        voting =  "<h1>Eligible to vote/h1>"
    else:
        voting =  "<h1>Not Eligible to vote</h1>"
    return voting

if __name__ == '__main__':
    app.run(debug=True)


