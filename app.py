from flask import Flask, render_template, redirect, jsonify,request
import os
import json
import time

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

#startup
@app.route("/", methods=["POST","GET"])
def homeStartup():
    return render_template("index.html", title="index", name="Ty Allembert")
#Index
@app.route("/index.html", methods=["POST","GET"])
def homeIndex():
    return render_template("index.html", title="index", name="Ty Allembert")

#===admin page===
@app.route("/admin.html", methods=["POST","GET"])
@auth.login_required
def admin():
    return render_template("admin.html", title="admin", name="Ty Allembert")

@app.route("/display_volunteers", methods=["POST","GET"])
def display_volunteers():
    ALL_VOLUNTEERS = []
    volunteer = []
    with open("form_data.txt", "r") as file:
        for line in file.readlines():
            line = line.rstrip()
            if line == "*":
                ALL_VOLUNTEERS.append(volunteer)
                volunteer = []
            if line != "*":
                volunteer.append(line.rstrip())

    return jsonify(ALL_VOLUNTEERS)
#===save form function===
@app.route("/save_form", methods=["POST","GET"])
def save_form():
    #the_array=request.get_json(force=True)
    the_array=request.form.getlist("form[]")
    print(the_array)
    with open("form_data.txt", "a") as fo:
        for x in the_array:
            fo.write(str(x))
            fo.write(str("\n"))
        fo.write(str("*\n"))

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
            <p>A new volunteer, """ + the_array[0] + """ """ + the_array[1] + """ just signed up!</p>
            <p>See more info by clicking <a href="https://www.salvationsuppersvt.com/admin.html">here</a></p>
        </body>
        </html>
        """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = "Salvation Suppers"
    msg.attach(MIMEText(html, 'html'))

    smtp.sendmail(from_addr="SalvationSupperAuto@gmail.com",
              to_addrs="ntgambill@gmail.com", msg=msg.as_string())
    smtp.quit()
    return "success"