#some imports needed for flask
from flask import Blueprint, render_template, redirect, url_for, request

#make a views a bleuprint object so it can be used. to be rendered
views = Blueprint('views', __name__)

# the base route's for the webapp.
@views.route('/')
def home():
    """
    hompage route
    """
    return render_template('base.html')

@views.route('login', methods=['GET', 'POST'])
def login():
    """
    login page render
    (able to login with username: admin and password: admin)
    """
    error = None
    if request.method == 'POST':
        # if something gets posted from the web. it comes in here.
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            # checks wether account is existent. 
            # could change != admin with request.form[username] in {dict of users} and
            # user_dict[request.form[username]] == request.form[password]
            error = 'Invalid Credentials. Please try again.'
        else:
            # set the login to true on account that has been filled in
            # login = request.form['username']
            return redirect("http://127.0.0.1:5000/")
    # if GET then it ends up on the base page.
    return render_template('login.html', error=error)


@views.route('sign_up')
def sign_up():
    """
    the signup page, 
    """
    error = None
    # attempted to make a signin page that added accounts to the database.
    # if request.method == 'POST':
        # if not request.form['username'] in accounts:
        #     accounts[request.form['username']] = request.form['password']
        #     return redirect("http://127.0.0.1:5000/login")
    return render_template('sign_up.html', error=error)