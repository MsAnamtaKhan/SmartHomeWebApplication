from flask import Flask, jsonify, request, session, redirect,flash
from passlib.hash import pbkdf2_sha256
from application import db
import uuid
import bson
class User:

  def start_session(self, user):
    del user['Password']
    session['logged_in'] = True
    session['user'] = user
    # return jsonify(user)
  
  def profile(self):
    elderly=db.Elderly.find_one({ "UserID": bson.ObjectId(session['user']['_id']) })
    return elderly
  
  

  def elderly_signup(self):
    
    Elderly = {
      "_id": bson.ObjectId(),
      "UserID":bson.ObjectId(session['user']['_id']),
      "Username": request.form.get('username'),
      "Email": request.form.get('email_address'),
      "Age": request.form.get('age'),
      "Phone": request.form.get("phone"),
      "Address": request.form.get("address")
    }
   

    if db.Elderly.find_one({ "Username": Elderly['Username'] }):
      return -1
    else:
      if db.Elderly.find_one({ "Email": Elderly['Email'] }):
        #flash(f'User with this Email already exist: ',category='alert')
        return -2
      else:
         if db.Elderly.insert_one(Elderly):
           return 1

    


  def updateUser(self):
    UserUpdate = {
      "Username": request.form.get('username'),
      "Email": request.form.get('email_address'),
      "Password": request.form.get('password1'),
      "Phone": request.form.get("phone"),
      "Address": request.form.get("address")
    }
    UserUpdate['Password'] = pbkdf2_sha256.encrypt(UserUpdate['Password'])
    response = db.User.update_one(
        { "_id": bson.ObjectId(session['user']['_id']) },
        { "$set": { "Username": UserUpdate['Username'], "Email" : UserUpdate['Email'],
        "Password" : UserUpdate['Password'],"Phone":UserUpdate["Phone"],"Address":UserUpdate['Address']} }
    )
# 62669bc5e330c57a3df1ef45

    updated=db.User.find_one({ "_id": bson.ObjectId(session['user']['_id']) })
    updated['_id']=str(updated['_id'])
    session['user'] = updated
    

    return response
  
  def updateElder(self):
    ElderlyUpdate = {
      "Username": request.form.get('username'),
      "Email": request.form.get('email_address'),
      "Age": request.form.get('age'),
      "Phone": request.form.get("phone"),
      "Address": request.form.get("address")
    }
    response = db.Elderly.update_one(
        { "UserID": bson.ObjectId(session['user']['_id']) },
        { "$set": { "Username": ElderlyUpdate['Username'], "Email" : ElderlyUpdate['Email'],
        "Age" : ElderlyUpdate['Age'],"Phone":ElderlyUpdate["Phone"],"Address":ElderlyUpdate['Address']} }
    )

    return response


   

  def signup(self):
    print(request.form)
    User = {
      "_id":bson.ObjectId(),
      "Username": request.form.get('username'),
      "Email": request.form.get('email_address'),
      "Password": request.form.get('password1'),
      "Phone": request.form.get("phone"),
      "Address": request.form.get("address")
    }


  
    
    # Encrypt the password
    User['Password'] = pbkdf2_sha256.encrypt(User['Password'])

    if db.User.find_one({ "Username": User['Username'] }):
      # flash(f'User with this Username already exist: ',category='alert')
      return -1
    else:
      if db.User.find_one({ "Email": User['Email'] }):
        # flash(f'User with this Email already exist: ',category='alert')
        return -2
      else:
         if db.User.insert_one(User):
           User['_id']=str(User['_id'])
           self.start_session(User)
           return 1

    

    # return jsonify({ "error": "Signup failed" }), 400
  
  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):
    User = db.User.find_one({
      "Username": request.form.get('username')
    })

    if User:
      if pbkdf2_sha256.verify(request.form.get('password'), User['Password']):
        User['_id']=str(User['_id'])
        self.start_session(User)
        return 1
      else:
        return -2
    else :
      return -1

  def addcontacts(self):
    contacts = {
      "_id":bson.ObjectId(),
      "UserID":bson.ObjectId(session['user']['_id']),
      "Name": request.form.get('name'),
      "EmergencyContact": request.form.get("phone")
    }


    if db.Contacts.find_one({ "Name": contacts['Name'] }):
      flash(f'User with this Name already exist: ',category='danger')
      return False
    else:
         if db.Contacts.insert_one(contacts):
           return True

    return False

  def viewContacts(self):
    contacts=db.Contacts.find({ "UserID": bson.ObjectId(session['user']['_id']) })
    return contacts
  
  def deleteContacts(self,id):
    contacts=db.Contacts.delete_one({ "_id":bson.ObjectId(id) })
    return contacts