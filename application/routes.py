from application import app
from flask import render_template, redirect, url_for,flash,request,session
#from market.models import Item,User
#from market.forms import RegisterForm,LoginForm,PurchaseItemForm,SellItemForm
#from market import db
from flask_login import login_user,logout_user,login_required,current_user

from application.forms import LoginForm,UserForm,ElderlyForm,AddContactsForm



@app.route('/')
def main_page():
    return render_template('landing_page.html')

@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/activities')
def activities_page():
    return render_template('activities.html')

@app.route('/contacts')
def contacts_page():
    return render_template('contacts.html')

@app.route('/addcontacts',methods=['GET', 'POST'])
def add_contacts_page():
    form=AddContactsForm()
    if form.validate_on_submit():
        print('validated')
        return redirect(url_for('contacts_page'))
    return render_template('addcontacts.html',form=form)
    

@app.route('/login',methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        print('validated')
        return redirect(url_for('home_page'))
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




@app.route('/elderly_profile',methods=['GET', 'POST'])
def elderly_profile():
    return render_template('elderly_profile.html')


@app.route('/elderly_update',methods=['GET', 'POST'])
def elderly_update():
    form=ElderlyForm()
    if form.validate_on_submit():
        return redirect(url_for('home_page'))
    return render_template('elderly_update.html',form=form)


@app.route('/user_update',methods=['GET', 'POST'])
def user_update():
    form=UserForm()
    if form.validate_on_submit():
        print('validated')
        return redirect(url_for('home_page'))
    return render_template('user_update.html',form=form)