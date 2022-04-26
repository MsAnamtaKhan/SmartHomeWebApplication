import imp
from application import app
from flask import render_template, redirect, url_for,flash,request,session
from application.models import User
#from market.forms import RegisterForm,LoginForm,PurchaseItemForm,SellItemForm
from application import db
from flask_login import login_user,logout_user,login_required,current_user

from application.forms import LoginForm,UserForm,ElderlyForm,AddContactsForm
import device
import cv2

from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *



@app.route('/')
def main_page():
    return render_template('landing_page.html')

@app.route('/home')
def home_page():
    devices = QCameraInfo.availableCameras()
    available_devices = []
    for name in devices:
        print(available_devices.append(name.description()))
    return render_template('index.html',available_devices=available_devices)

@app.route('/activities')
def activities_page():
    return render_template('activities.html')

@app.route('/contacts')
def contacts_page():
    contacts=User().viewContacts()
    return render_template('contacts.html',contacts=contacts)

@app.route('/addcontacts',methods=['GET', 'POST'])
def add_contacts_page():
    form=AddContactsForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if(User().addcontacts()!=False):
                flash(f'Contact Add Successfully',category='success')
                return redirect(url_for('contacts_page'))
    return render_template('addcontacts.html',form=form)
    

@app.route('/login',methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if(User().login()!=False):
    
                flash(f'Successfully Logged in!: ',category='success')
                return redirect(url_for('home_page'))
            else:
                flash(f'User with this Email does not exist: ',category='danger')
            
            
    
    # messagebox.showerror('User With this Email does not exist')
    return render_template('login.html',form=form)


@app.route('/signup',methods=['GET', 'POST'])
def signup_page():
    form=UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            res=User().signup()
            if(res>0):
                return redirect(url_for('elderly_page'))
            else:
                if (res==-1):
                    flash(f'User with this Username already exist: ',category='danger')
                else:
                    if res==-2:
                        flash(f'User with this Email already exist: ',category='danger')

    return render_template('user_signup.html',form=form)


@app.route('/elderly_signup',methods=['GET', 'POST'])
def elderly_page():
    form=ElderlyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            res=User().elderly_signup()
            if(res>0):
                flash(f'Successfully Register ',category='success')
                return redirect(url_for('home_page'))
            else:
                if (res==-1):
                    flash(f'User with this Username already exist: ',category='danger')
                else:
                    if res==-2:
                        flash(f'User with this Email already exist: ',category='danger')
                
    return render_template('elderly_signup.html',form=form)



@app.route('/user_profile',methods=['GET', 'POST'])
def user_profile():
    return render_template('user_profile.html')




@app.route('/elderly_profile',methods=['GET', 'POST'])
def elderly_profile():
    elderly=User().profile()
    return render_template('elderly_profile.html',elderly=elderly)


@app.route('/elderly_update',methods=['GET', 'POST'])
def elderly_update():
    form=ElderlyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if(User().updateElder()):
                flash(f'Update Successfully',category='success')
                return redirect(url_for('elderly_profile'))
    return render_template('elderly_update.html',form=form)


@app.route('/user_update',methods=['GET', 'POST'])
def user_update():
    form=UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if(User().updateUser()):
                flash(f'Update Successfully',category='success')
                return redirect(url_for('user_profile'))
    return render_template('user_update.html',form=form)

@app.route('/delete/<string:id>',methods=['GET', 'POST'])
def delete_contacts(id):
    if(User().deleteContacts(id)):
        flash(f'Delete Successfully',category='success')
        return redirect(url_for('contacts_page'))