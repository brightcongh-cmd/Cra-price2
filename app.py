from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

# Create Flask app
app = Flask(__name__)
CORS(app)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "Car Price Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = np.array([[
        float(data["year"]),
        float(data["engine_size"]),
        float(data["mileage"]),
        float(data["cylinders"]),
        float(data["horsepower"])
    ]])

    prediction = model.predict(features)

    return jsonify({
        "prediction": round(prediction[0], 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
