import joblib

model = joblib.load("model/salary_model.pkl")

def predict_salary(age,experience,education):

    prediction = model.predict([[age,experience,education]])

    return float(prediction[0])