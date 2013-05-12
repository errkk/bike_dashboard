from flask import Flask, request, session, redirect, render_template
from data import bikes


app = Flask(__name__)


@app.route("/")
def hello():
    data = bikes()
    return render_template('base.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
