from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

# Load the trained model and scaler
with open('parkinsons_disease_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)
@app.route('/')
def home():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = data['data']
    print(input_data)

    
    input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)

    
    std_data = scaler.transform(input_data_as_numpy_array)

    
    prediction = model.predict(std_data)

    
    result = 'no' if prediction[0] == 0 else 'yes'
    return jsonify({'prediction': result})


if __name__ == '__main__':
    app.run(debug=True)