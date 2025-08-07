from flask import Flask, render_template
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import random
app=Flask(__name__)
@app.route("/")
def home():return "hello alexa :]"
@app.route('/about')
def about():return render_template('about.html')
@app.route('/greet/<name>')
def greet_user(name):return render_template('greetings.html', name =name )
@app.route('/index')
def index():
    dt= datetime
    now = datetime.now()
    dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
    formatted_date_time = now.strftime("%A, %B %d, %Y %I:%M:%S %p")
    dt.tzname()
    return render_template('index.html', date_time=formatted_date_time, timezone= dt)


@app.route('/')
def random1():
    return render_template('challenge.html',num1="Click the button", num2= "to roll the dice")

@app.route('/challenge1', methods=['POST'])
def randomGen():
    number1= random.randint(1,6)
    number2= random.randint(1,6)
    message=False
    if(number1==number2):
        message=True
    return render_template('challenge.html', num1=number1, num2=number2, message=message)

@app.route('/challenge2/<year>')
def age(year):
    yearG=int(year)
    ageNum= 2025-yearG
    return render_template('challenge.html', answ=ageNum )
    
