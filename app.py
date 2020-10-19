# app.py
from flask import Response
from flask import Flask
from flask import render_template
import os
from pumpkinPi import imgList
app = Flask(__name__)

print(imgList)


@app.route('/')
def index():
    # return the rendered template
    return render_template("index.html", images=imgList)


if __name__ == '__main__':
    app.run(debug=True)
