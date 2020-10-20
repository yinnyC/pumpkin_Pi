# app.py
from multiprocessing import Process
from flask import Response
from flask import Flask
from flask import render_template
import json
import os

app = Flask(__name__)


def readJson():
    """ This funcction reads in Image Paths in the Json file """
    filepath = os.path.dirname(__file__)
    jsonPath = os.path.join(filepath, "ImgData.json")
    dataList = []
    with open(jsonPath, 'r') as fh:
        readinJson = json.load(fh)
        data = readinJson
        dataList.extend(data)
    return dataList


@app.route('/')
def index():
    return render_template("index.html", images=readJson())


if __name__ == '__main__':
    app.run(debug=True)
