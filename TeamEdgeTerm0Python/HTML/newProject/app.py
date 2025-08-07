# app.py
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
# Initialize the Flask application
app = Flask(__name__)

# Define a route for the home page

@app.route('/')
def home():
    return render_template('miniBlog.html', title='Author: Rick Riordan', message='Book:Percy Jackson and the lightning thief Date:May 14 2015')

@app.route("/add", methods=["GET", "POST"])
def add_task():
    form = TaskForm() 
    if request_method=="POST":
        new_task=form.task.data
        return render_template('miniBlog.html',message2="Book added" )
    else:
        return render_template('miniBlog.html',form=form-form )








