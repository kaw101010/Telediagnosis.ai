from flask import Flask, render_template, request, jsonify
import pyttsx3
from predictor_model import prediction_rf

app = Flask(__name__)

app.config['SECRET_KEY'] = '*(]=$_@`-%^2"?n\>#|{1&+/d^(?~./'

@app.route('/')
def index_page():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/predict-api', methods = ['POST', 'GET'])
def check_sym():
    if request.method == 'GET':
        predicted_disease = prediction_rf()
        return jsonify({"prediction":predicted_disease})

@app.route("/predict")
def show_result():
    return render_template('symptom.html')
