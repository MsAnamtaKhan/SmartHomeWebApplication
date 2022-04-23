from application import app
from flask import render_template, redirect, url_for,flash,request,session
#from market.models import Item,User
#from market.forms import RegisterForm,LoginForm,PurchaseItemForm,SellItemForm
#from market import db
from flask_login import login_user,logout_user,login_required,current_user

from application.forms import LoginForm,UserForm,ElderlyForm



@app.route('/')
def main_page():
    return render_template('landing_page.html')

@app.route('/home')
def home_page():
    return render_template('index.html')


@app.route('/login',methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    return render_template('login.html',form=form)

@app.route('/signup',methods=['GET', 'POST'])
def signup_page():
    form=UserForm()
    if form.validate_on_submit():
        print('validated')
        return redirect(url_for('elderly_page'))
    return render_template('user_signup.html',form=form)


@app.route('/elderly_signup',methods=['GET', 'POST'])
def elderly_page():
    form=ElderlyForm()
    if form.validate_on_submit():
        return redirect(url_for('home_page'))
    return render_template('elderly_signup.html',form=form)



@app.route('/user_profile',methods=['GET', 'POST'])
def user_profile():
    return render_template('user_profile.html')

