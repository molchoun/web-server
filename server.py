from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def works(page_name):
    return render_template(page_name)