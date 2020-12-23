from flask import Flask, url_for, render_template, request
from get_results import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/compare")
def compare():
    return render_template("compare.html")


@app.route("/results", methods=["GET", "POST"])
def results():
    if request:
        corpus1 = request.form["corpus1"]
        corpus2 = request.form["corpus2"]
        for i, corpus in enumerate([corpus1, corpus2]):
            if request.form["count"] == "pos":
                plot_frequencies(corpus, i)
            elif request.form["count"] == "words":
                plot_words(corpus, i)
        return render_template("results.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
