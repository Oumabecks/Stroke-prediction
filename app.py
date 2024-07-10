import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

model = pickle.load(open('KNN_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('Userinput.html')


@app.route('/predict', methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    return render_template("Userinput.html", prediction_text="The pateint result is {}".format(prediction))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
