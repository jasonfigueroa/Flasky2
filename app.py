from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from flask import Flask
app = Flask(__name__)

Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')
