from flask import Flask, render_template, jsonify,request
from os import listdir
import json
import time

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
    return "success"