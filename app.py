# app.py
from multiprocessing import Process
from flask import Response
from flask import Flask
from flask import render_template
import json
import os

imgList = []
app = Flask(__name__)
def readJson():
    filepath = os.path.dirname(__file__)
    jsonPath = os.path.join(filepath, "ImgData.json")
    with open(jsonPath, 'r') as fh:
        readinJson = json.load(fh)
        imgList = readinJson
    print(imgList)


@app.route('/')
def index():
    readJson()
    return render_template("index.html", images=imgList)

if __name__ == '__main__':

    app.run(debug=True)