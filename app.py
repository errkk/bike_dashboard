from flask import Flask, render_template
from data import bikes


app = Flask(__name__)


@app.route("/")
def hello():
    data = bikes()
    return render_template('base.html', data=data)


@app.route("/favicon.ico")
def fav():
    return ''

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
