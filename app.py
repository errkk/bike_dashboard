from flask import Flask, render_template
from data import bikes


app = Flask(__name__)


@app.route("/")
def hello():
    try:
        data = bikes()
    except Exception as e:
        return e
    return render_template('base.html', data=data)

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
