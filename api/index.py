from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    symptoms = request.form.get("symptoms")

    if symptoms:
        risk = "Medium Risk"
        color = "orange"
    else:
        risk = "Low Risk"
        color = "green"

    return render_template("result.html", risk=risk, color=color)

app = app
