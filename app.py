from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    title = "Flask Blog"

    programmingLanguages = [
        "python",
        "Perl",
        "Java",
        "C"
    ]
    return render_template('index.html', title=title, programmingLanguages=programmingLanguages)
