from flask import Flask, render_template, jsonify,request
from os import listdir
import json
import time

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib

app = Flask(__name__)

#startup
@app.route("/", methods=["GET"])
def homeStartup():
    return render_template("index.html", title="index", name="Ty Allembert")
#Index
@app.route("/index.html", methods=["GET"])
def homeIndex():
    return render_template("index.html", title="index", name="Ty Allembert")
@app.route("/save_form", methods=["POST","GET"])
def save_form():
    print("got here")
    #the_array=request.get_json(force=True)
    the_array=request.form.getlist("form[]")
    print(the_array)
    with open("form_data.txt", "a") as fo:
        for x in the_array:
            fo.write(str(x))
            fo.write(str("\n"))
        fo.write(str("\n"))

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('SalvationSupperAuto@gmail.com', 'TAWikrEQs9Jjz9v')

    subject = "New Salvation Suppers Volunteer"
    #text = "<p>A new volunteer, " + the_array[0] + " " + the_array[1] + " just signed up!</p>"
    text = """\
        <html>
        <head></head>
        <body>
            <h2>New Volunteer!</h2>
            <p>A new volunteer, """ + the_array[0] + """ """ + the_array[1] + """ just signed up!</p>
            <p>See more info by clicking <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">here</a></p>
        </body>
        </html>
        """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'html'))

    smtp.sendmail(from_addr="SalvationSupperAuto@gmail.com",
              to_addrs="tallembe@uvm.edu", msg=msg.as_string())
    smtp.quit()
    return "success"