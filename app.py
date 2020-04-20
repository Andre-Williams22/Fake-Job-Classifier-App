from flask import Flask, request, url_for, render_template, redirect
import numpy as np
import pickle 
import sklearn

app = Flask(__name__)

#model = pickle.load(open('random_forest_model_1.pkl', 'rb'))
model = pickle.load(open('example_dtclf_model.pkl', 'rb'))

# Home Route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final = [np.array(int_features)]
    prediction = model.predict_proba(final)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)

    if output == 1.00:
        yes = 'yes'
        return render_template('base.html', yes=yes)
    else:
        no = 'no'
        return render_template('base.html', no=no)


if __name__ == '__main__':
    app.run()