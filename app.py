from flask import Flask, render_template, jsonify
from nyt_api import most_popular_topics

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/headlines")
def headlines():
    data = most_popular_topics()
    return jsonify(data)


@app.route("/<name>")
def name(name):
    return render_template('name.html', name=name)

app.run(debug=True)
