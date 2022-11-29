import json
import handler.handler as handler
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
  scores = handler.get_scores()
  return render_template("base.html", scores=scores), 200


@app.route("/sort/<string:key>", methods=["GET"])
def sort(key):
  scores = handler.get_scores()
  scores.sort(key=lambda x: x[key])
  return render_template("sort.html", scores=scores, key=key), 200


if __name__ == "__main__":
  app.run(debug=True)