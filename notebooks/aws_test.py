sample_input_data = {"LoanAmount": 200,
        "total_income": 7000,
        "Loan_Amount_Term": 360,
        "Credit_History": 1,
        "Gender": "Female",
        "Married": "Yes",
        "Dependents": "0",
        "Education": "Not Graduate",
        "Self_Employed": "No",
        "Property_Area": "Urban"}


import requests
import json

url = 'http://ec2-3-137-213-153.us-east-2.compute.amazonaws.com:8000/predict'


response=requests.post(url, json=sample_input_data)
print(response.text)