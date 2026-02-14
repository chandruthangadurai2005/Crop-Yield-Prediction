from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "..", "models", "random_forest_model.pkl"))
feature_columns = joblib.load(os.path.join(BASE_DIR, "..", "models", "feature_columns.pkl"))

def detect_season():

    month = datetime.now().month

    if month in [6,7,8,9]:
        return "Kharif"
    elif month in [10,11,12,1]:
        return "Rabi"
    else:
        return "Whole Year"

def safe_value(val):
    try:
        return float(val)
    except:
        return 0

@app.route("/")
def home():
    return "Crop Yield Prediction API Running ✅"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    rainfall = safe_value(data.get("annual_rainfall"))
    fertilizer = safe_value(data.get("fertilizer"))
    pesticide = safe_value(data.get("pesticide"))

    detected_season = detect_season()

    crops = ["Rice", "Wheat", "Maize"]

    crop_results = {}

    for crop in crops:

        input_data = data.copy()

        input_data["crop_Rice"] = 1 if crop == "Rice" else 0
        input_data["crop_Wheat"] = 1 if crop == "Wheat" else 0
        input_data["crop_Maize"] = 1 if crop == "Maize" else 0

        input_data["season_Kharif"] = 1 if detected_season == "Kharif" else 0
        input_data["season_Rabi"] = 1 if detected_season == "Rabi" else 0
        input_data["season_Whole Year"] = 1 if detected_season == "Whole Year" else 0

        df_input = pd.DataFrame([input_data])
        df_input = df_input.reindex(columns=feature_columns, fill_value=0)

        crop_results[crop] = float(model.predict(df_input)[0])

    recommended_crop = max(crop_results, key=crop_results.get)

    recommendations = []

    if rainfall < 50:
        recommendations.append("🌧 Low rainfall — irrigation planning advised.")

    if fertilizer > 100:
        recommendations.append("⚠ High fertilizer usage — check efficiency.")

    if pesticide > 20:
        recommendations.append("⚠ Excess pesticide may reduce yield.")

    return jsonify({
        "predicted_yield": crop_results[data["selected_crop"]],
        "recommended_crop": recommended_crop,
        "detected_season": detected_season,
        "all_predictions": crop_results,
        "recommendations": recommendations
    })

if __name__ == "__main__":
    app.run(debug=True, port=5001)
