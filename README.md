# 🌾 AI Crop Yield Prediction & Recommendation System

An AI-powered decision support system that predicts crop yield and provides intelligent crop recommendations using environmental and agricultural input factors.

------------------------------------------------------------

🚀 PROJECT OVERVIEW

This system leverages Machine Learning to assist farmers in making data-driven decisions by analyzing:

• Land Area  
• Rainfall & Climatic Conditions  
• Fertilizer Usage  
• Pesticide Usage  
• Soil Quality Proxy  
• Crop & Seasonal Factors  

The platform predicts expected crop yield and recommends the most suitable crop for maximum productivity.

------------------------------------------------------------

✨ KEY FEATURES

✅ Crop Yield Prediction (Machine Learning)  
✅ Intelligent Crop Recommendation Engine  
✅ GPS-Based Location Detection  
✅ Climate-Aware Rainfall Estimation  
✅ Measurement Unit Normalization  
✅ Flask REST API Backend  
✅ Interactive Web Interface  
✅ Automatic Season Detection  

------------------------------------------------------------

🧠 MACHINE LEARNING MODEL

Algorithm Used:
Random Forest Regressor

Problem Type:
Regression

Target Variable:
Crop Yield

Evaluation Metrics:
RMSE, R² Score

------------------------------------------------------------

📊 INPUT PARAMETERS

The model considers multiple agricultural and environmental factors:

• Area (Standardized to Hectares)  
• Annual Rainfall  
• Fertilizer Usage  
• Pesticide Usage  
• Soil Quality Index  
• Crop Encoding  
• Seasonal Encoding  
• Regional Encoding  

------------------------------------------------------------

🌍 SMART INTELLIGENCE COMPONENTS

✔ Geo-Intelligence → GPS Location Detection  
✔ Climate Intelligence → Weather API Integration  
✔ Domain Normalization → Unit Conversion Engine  
✔ Seasonal Logic → Month → Season Mapping  

------------------------------------------------------------

🛠 TECH STACK

Machine Learning:
• Python  
• Pandas, NumPy  
• Scikit-Learn  

Backend:
• Flask (REST API)  
• Flask-CORS  

Frontend:
• HTML, CSS, JavaScript  

External APIs:
• OpenWeather API (Climate Data)  
• Reverse Geocoding API (Location Context)  

------------------------------------------------------------

📦 MODEL FILES

Due to GitHub file size constraints, trained ML model binaries are hosted externally.

Download Model Files:
https://drive.google.com/drive/folders/17oHk4DpjUPDuC0Zo2dx4q3RP2hv0vttN

After downloading, place the files inside:

models/

------------------------------------------------------------

🚀 INSTALLATION & SETUP

1️⃣ Clone Repository

git clone https://github.com/chandruthangadurai2005/Crop-Yield-Prediction.git

cd Crop-Yield-Prediction


2️⃣ Install Dependencies

pip install pandas numpy scikit-learn flask flask-cors joblib


3️⃣ Download ML Model

Download the .pkl model files from Google Drive.

Place them inside:

models/


4️⃣ Run Backend API

python api/app.py


Flask server will start at:

http://127.0.0.1:5001


5️⃣ Run Frontend

Open:

ui/index.html

in your browser.

------------------------------------------------------------

📈 FUTURE ENHANCEMENTS

• Real Soil Data API Integration  
• Crop Disease Prediction Module  
• Market Price Forecasting  
• Farmer Advisory Dashboard  
• Mobile Application Version  

------------------------------------------------------------

🎯 PROJECT SIGNIFICANCE

This project demonstrates:

✅ End-to-End ML System Design  
✅ Real-World API Integration  
✅ Intelligent Decision Support Logic  
✅ Domain-Aware Data Normalization  
✅ Full Stack + Machine Learning Integration  

------------------------------------------------------------

👨‍💻 AUTHOR

Chandru T  
Bachelor of Information Technology  
Machine Learning & Software Engineering Enthusiast 🚀
