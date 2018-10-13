from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>/')
def profile(username):
    return '{}\'s profile'.format(username)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = True):
    return render_template('index.html', name=name)