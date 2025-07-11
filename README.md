# 📈 Bank Marketing Campaign Prediction API (FastAPI + Anaconda + Render)

This project is a complete end-to-end Machine Learning pipeline that builds a **predictive API for bank marketing success**. It uses the Bank Marketing dataset to train a classifier to predict whether a client will subscribe to a term deposit based on personal and campaign features. The trained model is served through a **FastAPI web application** and deployed on **Render** using a `render.yaml` infrastructure-as-code setup.

---

## 📌 Table of Contents

- 🔧 Project Overview
- 🧰 Tools & Technologies Used
- 📁 Project Structure
- ⚙️ Setup Instructions (Local)
- 🚀 Deployment on Render
- 🧪 How to Use the API
- 📬 Contact

---

## 🔧 Project Overview

The dataset contains attributes of clients contacted as part of a direct marketing campaign by a Portuguese bank. The goal is to build a model that predicts the success of these campaigns (whether a customer subscribes to a term deposit). The pipeline includes:

1. Data preprocessing (categorical encoding, scaling, etc.)
2. Model training using `RandomForestClassifier`
3. Saving model and scaler (`joblib`)
4. Building a RESTful API using FastAPI
5. Optional: A form-based frontend UI (HTML + Jinja2)
6. Deploying to the cloud via Render using `render.yaml`

---

## 🧰 Tools & Technologies Used

- **Language**: Python 3.10 (via Anaconda environment)
- **Machine Learning**: scikit-learn
- **API Framework**: FastAPI
- **Deployment**: Render.com (via `render.yaml`)
- **Serialization**: joblib
- **Frontend (optional)**: HTML, Jinja2
- **Dev Tools**: Uvicorn, Conda

---

## 📁 Project Structure

bank_marketing_api/
├── app.py # FastAPI application with API and form routes
├── train_model.py # Script to preprocess data and train the ML model
├── model.pkl # Trained Random Forest model
├── scaler.pkl # StandardScaler used during training
├── requirements.txt # Python dependencies
├── render.yaml # Render deployment configuration
├── templates/
│ └── form.html # Web form for user input
├── static/ # (Optional) CSS or assets for the form
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Setup Instructions (Local)

> Ensure you have **Anaconda** or **Python 3.10+** installed.

### 1. Create and activate environment

```
2. Install dependencies

Copy
Edit
pip install -r requirements.txt
3. Train the model

Copy
Edit
python train_model.py
4. Run the FastAPI app locally

Copy
Edit
uvicorn app:app --reload
5. Test the app
Swagger UI: http://127.0.0.1:8000/docs

HTML Form: http://127.0.0.1:8000/form

🚀 Deployment on Render
1. Prepare GitHub repository
Push your entire bank_marketing_api/ folder to a GitHub repo.

2. Ensure these files exist:
render.yaml

requirements.txt

Procfile (optional if using startCommand in render.yaml)

3. Deploy on Render
Log in → New Web Service → Connect your GitHub repo

Render will detect render.yaml and install automatically

Your deployed API will be accessible via a public URL (e.g., https://your-app.onrender.com)

🧪 How to Use the API
🔸 Option 1: Swagger API
Go to /docs and try the /predict endpoint by sending JSON like:

json
Copy
Edit
{
  "features": [30, 1200, 2, 0, 0, 1, 0, ...]
}
🔸 Option 2: HTML Form
Go to /form, fill in user attributes, and see the prediction.

