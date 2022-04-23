from application import app
from flask import render_template, redirect, url_for,flash,request,session
#from market.models import Item,User
#from market.forms import RegisterForm,LoginForm,PurchaseItemForm,SellItemForm
#from market import db
from flask_login import login_user,logout_user,login_required,current_user



@app.route('/')
def main_page():
    return render_template('landing_page.html')

@app.route('/home')
def home_page():
    return render_template('index.html')
