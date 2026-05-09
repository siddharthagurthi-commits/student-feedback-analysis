from flask import Flask, render_template, request
from model import predict_feedback

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template("index.html")

# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    feedback = request.form['feedback']
    result = predict_feedback(feedback)
    return render_template("index.html", prediction=result)

# Run App
if __name__ == "__main__":
    app.run(debug=True)