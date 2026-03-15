import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os

# Sample dataset
data = {
    "age":[25,30,35,40,28,32,45,50],
    "experience":[1,3,5,7,2,4,10,12],
    "education":[1,2,3,3,2,2,3,3],
    "salary":[30000,40000,60000,80000,35000,50000,120000,150000]
}

df = pd.DataFrame(data)

X = df[['age','experience','education']]
y = df['salary']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

mlflow.set_experiment("salary_prediction")

with mlflow.start_run():

    model = LinearRegression()
    model.fit(X_train,y_train)

    score = model.score(X_test,y_test)

    mlflow.log_param("model","LinearRegression")
    mlflow.log_metric("accuracy",score)

    mlflow.sklearn.log_model(model,"model")

os.makedirs("../model",exist_ok=True)

joblib.dump(model,"../model/salary_model.pkl")

print("Model trained and saved")