from flask import Blueprint, render_template, redirect, url_for, request

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('base.html')
    
@views.route('login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] not in accounts or request.form['password'] != accounts[request.form['username']]:
            error = 'Invalid Credentials. Please try again.'
        else:
            login = request.form['username']
            return redirect("http://127.0.0.1:5000/")
    return render_template('login.html', error=error)


@views.route('sign_up')
def sign_up():
    error = None
    if request.method == 'POST':
        if not request.form['username'] in accounts:
            accounts[request.form['username']] = request.form['password']
            return redirect("http://127.0.0.1:5000/login")
    return render_template('sign_up.html', error=error)