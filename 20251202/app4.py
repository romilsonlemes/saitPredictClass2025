from flask import Flask, redirect, url_for

app = Flask(__name__) # Initializind the Flask application or Flask Container

@app.route('/')
def greeting():
    return "<h1>Welcome</h1>"


@app.route('/admin') #https://127.0.0.0:5000
def welcome_admin():
    return "<h1>Welcome Admin</h1>"

@app.route('/guest/<guest>') #https://127.0.0.0:5000
def welcome_guest(guest):
    return f"<h1>Welcome {guest} as a Guest</h1>"

@app.route('/user/<name>') #https://127.0.0.0:5000
def hello_user(name):

    if name == 'admin':
        return redirect(url_for('welcome_admin'))
    else:
        return redirect(url_for('welcome_guest', guest=name))

if __name__ == '__main__':
    app.run(debug=True)


