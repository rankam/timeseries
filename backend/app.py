# /predict
from flask import Flask, render_template, request, jsonify
import numpy as np
import traceback
import pickle
import pandas as pd

# Function to fit a Prophet model on input JSON
def prophet_forecast(input_json, forecast_periods = 10):
    # Format JSON data to a pandas dataframe
    data_json_unpacked = [json.loads(i) for i in input_json]
    data_df = pd.json_normalize(data_json_unpacked)
    data_df.columns = ['ds', 'y']

    # Instantiate a new Prophet object and fit model
    m = Prophet()
    m.fit(data_df)

    # Make predictions: Predictions are made on a dataframe with a column ds containing the dates for which a prediction is to be made
    future = m.make_future_dataframe(periods = forecast_periods) # Predict 10 days

    forecast = m.predict(future)

    forecast_json = forecast.to_json(orient = 'records', lines = True).splitlines()
    
    return forecast_json


app = Flask(__name__)

@app.route('/predict', methods = ["POST"])
def predict():

    data = request.json
    forecast = prophet_forecast(input_json = data, forecast_periods=10)
    
    return jsonify({"output": str(forecast), "message": "forecast successful"})



if __name__ == '__main__':
    app.run()