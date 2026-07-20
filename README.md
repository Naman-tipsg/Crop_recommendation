# 🌱 Crop Recommendation System using Machine Learning

A Machine Learning-based Crop Recommendation System that predicts the most suitable crop to cultivate based on soil nutrients and environmental conditions. This project helps farmers and agricultural professionals make informed decisions by analyzing key factors such as Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall.

---

# 📌 Project Overview

Choosing the right crop is one of the most important decisions in agriculture. This project uses Machine Learning algorithms to recommend the best crop for cultivation by analyzing soil properties and weather conditions.

The model is trained on agricultural data and can accurately predict the most suitable crop, making farming more efficient and data-driven.

---




# ✨ Features

* 🌱 Predicts the best crop for cultivation
* 🤖 Machine Learning-based recommendation system
* 📊 Uses soil and weather parameters
* ⚡ Fast and accurate predictions
* 💾 Saved model using Joblib (.pkl)
* 🌍 Easy deployment with Flask, FastAPI, or Streamlit
* 📱 User-friendly interface

---

# 🛠️ Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Joblib
* Jupyter Notebook / Google Colab
* Flask / FastAPI / Streamlit (Optional)

---

# 📂 Project Structure

```text
Crop-Recommendation/
│
├── dataset/
│   └── Crop_Recommendation.csv
│
├── models/
│   ├── crop_model.pkl
│   └── encoder.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── images/
```

---

# 📊 Input Features

The model takes the following agricultural parameters as input.

| Feature        | Description                |
| -------------- | -------------------------- |
| Nitrogen (N)   | Nitrogen content in soil   |
| Phosphorus (P) | Phosphorus content in soil |
| Potassium (K)  | Potassium content in soil  |
| Temperature    | Temperature (°C)           |
| Humidity       | Relative Humidity (%)      |
| pH             | Soil pH value              |
| Rainfall       | Rainfall (mm)              |

---

# 🎯 Output

The model predicts the most suitable crop.

Example Predictions:

* Rice
* Wheat
* Maize
* Cotton
* Sugarcane
* Banana
* Coconut
* Mango
* Chickpea
* Lentil
* Kidney Beans
* Coffee
* Jute
* Black Gram
* Pigeon Peas
* Apple
* Papaya
* Watermelon
* Muskmelon
* Orange

---

# ⚙️ Machine Learning Workflow

```
Agricultural Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Train-Test Split
        │
        ▼
Machine Learning Model
        │
        ▼
Model Evaluation
        │
        ▼
Save Model (.pkl)
        │
        ▼
Crop Prediction
```

---

# 📈 Model Training Process

The model was developed using the following steps:

* Data Collection
* Data Cleaning
* Handling Missing Values
* Label Encoding
* Feature Selection
* Train-Test Split
* Model Training
* Hyperparameter Tuning
* Performance Evaluation
* Model Saving

---

# 📊 Model Evaluation

The trained model was evaluated using:

* Accuracy Score
* Precision Score
* Recall Score
* F1 Score
* Confusion Matrix
* Classification Report

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Crop-Recommendation.git
```

Move into the project directory

```bash
cd Crop-Recommendation
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Using Python

```bash
python app.py
```

Using Streamlit

```bash
streamlit run app.py
```

Using Flask

```bash
flask run
```

---

# 📸 Project Screenshots

Add screenshots here.

```
images/home.png

images/prediction.png

images/result.png
```

---

# 🌾 Example Input

| Feature     |  Value |
| ----------- | -----: |
| Nitrogen    |     90 |
| Phosphorus  |     42 |
| Potassium   |     43 |
| Temperature |  20.87 |
| Humidity    |  82.00 |
| pH          |   6.50 |
| Rainfall    | 202.93 |

### Predicted Crop

```
Rice
```

---

# 📌 Future Improvements

* Weather API Integration
* Real-time Soil Sensor Support
* Fertilizer Recommendation
* Irrigation Prediction
* Disease Detection
* AI Chatbot for Farmers
* Mobile Application
* Cloud Deployment

---

# 🤝 Contributing

Contributions are always welcome.

1. Fork this repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push to your branch
6. Open a Pull Request

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

---

# 👨‍💻 Author

**Naman Sharma**

**Data Science | Machine Learning | Python Developer**

If you like this project, don't forget to ⭐ star the repository.
