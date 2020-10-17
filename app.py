# app.py
from flask import Response
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    # return the rendered template
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)