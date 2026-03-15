from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_salary

app = FastAPI()

class InputData(BaseModel):
    age:int
    experience:int
    education:int


@app.get("/")
def home():
    return {"message":"Salary Predictor API running"}


@app.post("/predict")
def predict(data:InputData):

    salary = predict_salary(
        data.age,
        data.experience,
        data.education
    )

    return {"predicted_salary":salary}