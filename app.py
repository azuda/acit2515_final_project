import json
from flask import Flask, render_template, request


app = Flask(__name__)
# read scores.json
with open("data/scores.json", "r") as f:
  scores = json.load(f)


@app.route("/")
def home():
  return render_template("base.html", scores=scores), 200


if __name__ == "__main__":
  app.run(debug=True)