from flask import Flask, render_template

app = Flask(__name__)

data = [
    {
    "title": "Python",
    "bio": "Python is a dynamically interpreted language"
    },
    {
    "title": "Java",
    "bio": "Java is an object oriented language language"
    },
    {
    "title": "HTML",
    "bio": "A markup language used for creating webpages"
    },
    {
    "title": "C",
    "bio": "Used for creating games"
    },
    {
    "title": "CSS",
    "bio": "Used for styling webpages"
    }
    ]

@app.route('/')
def hello_world():
    title = "Flask Blog"
    return render_template('index.html', title=title)


@app.route('/lang/<name>')
def lang(name):
    title = name
    lang = next(item for item in data if item["title"].lower() == name.lower())
    return render_template('lang.html', title=title, lang=lang)

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
