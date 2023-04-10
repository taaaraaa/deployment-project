# from flask import Flask, jsonify, request
# import pickle
# import pandas as pd
# import numpy as np
# #from my_transformers import DenseTransformer
#
# def log_transform(X):
#     X_log = np.log(X)
#     return X_log
#
# with open('loan_model.pkl', 'rb') as f:
#     pipeline = pickle.load(f)
#
# app = Flask(__name__)
#
# @app.route('/predict', methods=['POST'])
# def predict():
#     json_data = {"LoanAmount": 200,
#                  "total_income": 7000,
#                  "Loan_Amount_Term": 360,
#                  "Credit_History": 1,
#                  "Gender": "Female",
#                  "Married": "Yes",
#                  "Dependents": "0",
#                  "Education": "Not Graduate",
#                  "Self_Employed": "No",
#                  "Property_Area": "Urban"}
#     # Extract data from the POST request
#     # data = request.get_json(force=True)
#     # Convert data into pandas DataFrame
#     data_df = pd.DataFrame(json_data, index=[0])
#
#     # Make predictions using the trained model
#     predictions = pipeline.predict(data_df)
#
#     # Return the predictions as a JSON response
#     return jsonify(predictions.tolist())
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port='5000',debug=True)
from flask import Flask, jsonify, request
import pickle
import pandas as pd
import numpy as np


# from my_transformers import DenseTransformer

def log_transform(X):
    X_log = np.log(X)
    return X_log


with open('loan_model.pkl', 'rb') as f:
    pipeline = pickle.load(f)

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from the POST request
    data = request.get_json(force=True)
    print(data)

    # Convert data into pandas DataFrame
    data_df = pd.DataFrame(data, index=[0])

    # Make predictions using the trained model
    predictions = pipeline.predict(data_df)

    # Return the predictions as a JSON response
    return jsonify(predictions.tolist())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000',debug=True)