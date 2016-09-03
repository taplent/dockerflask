import time
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    context = {'ctime': time.strftime("%Y-%m-%d %H:%M:%S")}
    return render_template("home.html", **context)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
