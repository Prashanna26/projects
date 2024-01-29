from flask import render_template, request, redirect, session, url_for
from model_data.model_login import ModelLoginData
from model_data.model_home import ModelHomeData
from datetime import datetime

login_data = ModelLoginData()
home_data = ModelHomeData()

def log_the_user_in(username):
    session['username'] = username

def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = login_data.get_all_item()
        if username in users and users[username]['password']==password :
            log_the_user_in(username)
            return redirect('/home')
        else:
            error = 'Invalid Username/Password'
    return render_template('login.html', error = error)

def signup():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        users = login_data.get_all_item()
        if username not in users:
            login_data.add_item(username, password, email)
            return redirect('/')
        else:
            error = 'Username is not available.'
    return render_template('signup.html',error = error)

def home():
    task = home_data.get_all_item()
    if task:
        return render_template('home.html', tasks = task)
    else:
        return render_template('home.html')
    

def button_clicked():
    if request.method == 'POST':
        text_area = request.form.get('writing_space', '')
        status_msg = 0
        date_time = request.form.get('datentime', '')
        priority = int(request.form.get('priority', ''))
        now = datetime.now()
        p_datetime = now.strftime("%Y/%m/%d, %H:%M")
        date_time = (", ").join(date_time.split('T'))
        home_data.add_item(text_area, date_time, priority, status_msg, p_datetime)
        return redirect('/home')
    else:
        return redirect('/home')
    

def delete_button(task_id):
    button_index = int(task_id)
    home_data.delete_item(button_index)
    return redirect('/home')


def complete_button(task_id):
    status = home_data.get_item('status',task_id)
    if status == 0:
        home_data.update_message(task_id, 'status', 1)
    else:
        home_data.update_message(task_id, 'status', 0)
    return redirect('/home')

def edit_button(task_id):
    message = home_data.get_item('message', task_id)
    datetime = home_data.get_item('datatime', task_id)
    priority = home_data.get_item('priority', task_id)
    datetime = ('T').join(datetime.split(", "))
    home_data.delete_item(task_id)
    task = home_data.get_all_item()
    content = {'message':message, 'datetime':datetime, 'priority': priority}
    return render_template('home.html', tasks = task, contents = content)