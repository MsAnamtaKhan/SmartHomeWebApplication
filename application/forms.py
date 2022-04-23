from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired,ValidationError,NumberRange

# from market.models import User

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Login')

class UserForm(FlaskForm):
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    address = StringField(label='Address:', validators=[Length(min=5, max=30), DataRequired()])
    phone = StringField(label='Phone:', validators=[Length(min=11, max=11), DataRequired()])    
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Next')


class ElderlyForm(FlaskForm):
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    address = StringField(label='Address:', validators=[Length(min=5, max=30), DataRequired()])
    phone = StringField(label='Phone:', validators=[Length(min=11, max=11), DataRequired()])    
    age=IntegerField(label='Age:',validators=[NumberRange(min=1, max=100),DataRequired()])
    submit = SubmitField(label='SUBMIT')
