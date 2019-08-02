from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    title = "Flask Blog"
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = "About Us"
    return render_template('about.html', title=title)

@app.route('/contact')
def contactUs():
    title = "Contact Us"
    return render_template('contact.html', title=title)

@app.route('/join')
def getStarted():
    title = "Join Us"
    return render_template('join.html', title=title)

@app.route('/privacy')
def privacy():
    title = "Privacy Policy"
    return render_template('policy.html', title=title)
