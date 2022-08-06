from flask import Flask, render_template, redirect, url_for
import runModel

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/runModel")
def runPred():
    results = runModel.runPredictions()

    return results


if __name__ == "__main__":
    app.run(debug=True)