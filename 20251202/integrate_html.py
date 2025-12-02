from flask import Flask, redirect, url_for

app = Flask(__name__) # Initializind the Flask application or Flask Container

@app.route('/')
def greeting():
    return "<h1>Welcome</h1>"


@app.route('/eligible/<int:age>') #https://127.0.0.0:5000
def eligible(age):
    if age < 18:
        return f"<h2 style='background-color:Tomato;'>Age is {age} and user is  Not Eligible</h2>"
    else:
        return f"<h2 style='background-color:DodgerBlue;'>Age is {age} and user is Eligible</h2>"




if __name__ == '__main__':
    app.run(debug=True)


