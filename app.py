#source venv/bin/activate
from flask import Flask, render_template, redirect, jsonify, request, flash, url_for
import os, sqlite3, json, time

from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "Nick": generate_password_hash("t98yn38P9Y08jmefiI3")
}
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

#Database connection
def get_db_connection():
    conn = sqlite3.connect('database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

#startup
@app.route("/", methods=['POST','GET'])
def homeStartup():
    conn = get_db_connection()
    info = conn.execute('SELECT * FROM WebsiteInfo').fetchall()
    mealsDigits = list(info[0]['numMeals'])
    conn.close()
    formSubmitted = False

    if request.method == 'POST':
        print(request.form)
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        phone = request.form['phone']
        whyHelp = request.form['whyHelp']
        
        if not firstName:
            flash('First Name is required!')
        elif not lastName:
            flash('Last Name is required!')
        elif not email:
            flash('Email is required!')
        elif not phone:
            flash('Phone Number is required!')
        else:
            conn = get_db_connection()
            conn.execute("INSERT INTO Volunteers (firstName, lastName, email, phone, whyHelp) VALUES (?, ?, ?, ?, ?)",
                        (firstName, lastName, email, phone, whyHelp))
            conn.commit()
            conn.close()
            formSubmitted = True
    return render_template("index.html", title="index", info=info, formSubmitted = formSubmitted, mealsDigits=mealsDigits)
#Index
@app.route("/index", methods=["POST","GET"])
def homeIndex():
    return render_template("index.html", title="index", name="Ty Allembert")

#===admin page===
@app.route("/admin", methods=["POST","GET"])
@auth.login_required
def admin():
    conn = get_db_connection()
    volunteers = conn.execute('SELECT * FROM Volunteers').fetchall()
    conn.close()
    if request.method == 'POST':
        conn = get_db_connection()
        if 'event_input_submit' in request.form:
            event = request.form['event_input']
            change_string = "UPDATE WebsiteInfo SET headerMessage = \'" + event + "\' WHERE id = 1"
            print(change_string)
            conn.execute(change_string)
        if 'meals_input_submit' in request.form:
            meals = request.form['meals_input']
            change_string = "UPDATE WebsiteInfo SET numMeals = \'" + meals + "\' WHERE id = 1"
            print(change_string)
            conn.execute(change_string)
        conn.commit()
        conn.close()
    return render_template("admin.html", title="admin", volunteers=volunteers)
#====delete volunteer=====
@app.route("/delete_volunteer", methods=["POST", "GET"])
def delete_volunteer():
    if request.method == 'POST':

        data = request.form.getlist("data[]")
        id = data[0]

        sqlUpdate = "DELETE FROM Volunteers WHERE id = \'"+id+"\'"
        print(sqlUpdate)
        conn = get_db_connection()
        conn.execute(sqlUpdate)
        conn.commit()
        conn.close()
    return "success"
#===save form function===
@app.route("/save_form", methods=["POST","GET"])
def save_form():


#Start of sending email
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('SalvationSupperAuto@gmail.com', 'TAWikrEQs9Jjz9v')

    subject = "New Salvation Suppers Volunteer"
    html = """\
        <html>
        <head></head>
        <body>
            <h2>New Volunteer!</h2>
            <p>A new volunteer, """ + firstName + """ """ + lastName + """ just signed up!</p>
            <p>See more info by clicking <a href="https://www.salvationsuppersvt.com/admin">here</a></p>
        </body>
        </html>
        """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = "Salvation Suppers"
    msg.attach(MIMEText(html, 'html'))

    smtp.sendmail(from_addr="SalvationSupperAuto@gmail.com",
              to_addrs="tyallembert@gmail.com", msg=msg.as_string())
    smtp.quit()
    #ntgambill@gmail.com
    return "success"