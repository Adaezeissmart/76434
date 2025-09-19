from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators

class ContactForms(Form):

    name = TextField("Candidate Name", [validators.Required("Please Enter your name.")])

    Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])

    Address = TextAreaField("Address")

    Age = IntegerField("Age")
    
    language = SelectField('Progamming Languages',choices = [('java','Java'),('py','Python')])


    submit = SubmitField("Submit")