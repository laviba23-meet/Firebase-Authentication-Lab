from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
  "apiKey": "AIzaSyA0cJk4CjD1-XW75AoF9ER4IeWsMcX1SSA",
  "authDomain": "fir-project-1-68013.firebaseapp.com",
  "projectId": "fir-project-1-68013",
  "storageBucket": "fir-project-1-68013.appspot.com",
  "messagingSenderId": "857460672805",
  "appId": "1:857460672805:web:996f5ad076c67c4f25f2cc",
  "measurementId": "G-RW80MJV0XW",
  "databaseURL":""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        try:
            login_session['user']= auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"

    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        try:
            login_session['user']= auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"

    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")

@app.route('/signout')
def signout():
    login_session['user']=None
    auth.current_user = None
    return redirect(url_for('signin'))


if __name__ == '__main__':
    app.run(debug=True)