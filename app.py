from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# (Optional) Load the scaler if you saved it
# with open("scaler.pkl", "rb") as f:
#     scaler = pickle.load(f)

# Define the input format
class InputData(BaseModel):
    age: int
    balance: float
    duration: float
    campaign: int
    pdays: int
    previous: int
    job_admin: int
    marital_married: int
    education_secondary: int
    default_yes: int
    housing_yes: int
    loan_yes: int
    contact_cellular: int
    month_aug: int
    poutcome_success: int

@app.get("/")
def home():
    return {"message": "Bank Prediction API is Live!"}

@app.post("/predict")
def predict(data: InputData):
    # Convert input to numpy array
    input_array = np.array([
        data.age, data.balance, data.duration, data.campaign,
        data.pdays, data.previous, data.job_admin,
        data.marital_married, data.education_secondary,
        data.default_yes, data.housing_yes, data.loan_yes,
        data.contact_cellular, data.month_aug, data.poutcome_success
    ]).reshape(1, -1)

    # Optional: input_array = scaler.transform(input_array)

    prediction = model.predict(input_array)
    return {"prediction": int(prediction[0])}

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize FastAPI app
app = FastAPI()

# Define input format using Pydantic
class InputData(BaseModel):
    age: int
    job_admin: int
    marital_married: int
    education_secondary: int
    default_no: int
    balance: float
    housing_yes: int
    loan_no: int
    contact_cellular: int
    day: int
    month_may: int
    duration: float
    campaign: int
    pdays: int
    previous: int
    poutcome_success: int

@app.get("/")
def root():
    return {"message": "Welcome to the prediction API!"}

@app.post("/predict")
def predict(data: InputData):
    # Convert input to array
    input_array = np.array([[
        data.age,
        data.job_admin,
        data.marital_married,
        data.education_secondary,
        data.default_no,
        data.balance,
        data.housing_yes,
        data.loan_no,
        data.contact_cellular,
        data.day,
        data.month_may,
        data.duration,
        data.campaign,
        data.pdays,
        data.previous,
        data.poutcome_success
    ]])

    # Make prediction
    prediction = model.predict(input_array)
    result = "yes" if prediction[0] == 1 else "no"
    return {"prediction": result}
