from flask import Flask, request, url_for, render_template, redirect
import numpy as np
import pickle 

app = Flask(__name__)

model = pickle.load(open('random_forest_model_1.pkl', 'rb'))

# Home Route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    pass 




if __name__ == '__main__':
    app.run()