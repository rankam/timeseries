# /predict
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods = ["POST"])
def predict():
    return jsonify({"response": "hello world"})






if __name__ == '__main__':
    app.run()