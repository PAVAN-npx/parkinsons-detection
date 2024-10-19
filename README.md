# Parkinson's Disease Detection API

This project is a Flask-based web API that predicts whether a person has Parkinson's disease based on voice measurements. The machine learning model used is an SVM (Support Vector Machine) trained on the `parkinsons.data` dataset. The API is deployed on Render at [Parkinson's Detection](https://parkinsons-detection-avxi.onrender.com).

## Features
- **Prediction**: The API predicts whether the input data suggests Parkinson's disease.
- **Model**: SVM model trained on `parkinsons.data`.
- **Scaling**: Input data is preprocessed with a scaler before being passed to the model.
- **Cross-Origin Support**: CORS is enabled to allow requests from any origin.

## API Endpoints

### Home Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Response**: Simple message: `"Hello, World"`

### Predict Endpoint
- **URL**: `/predict`
- **Method**: `POST`
- **Request Body**:
  - `data`: A list of voice measurement values (array of floats/integers).

- **Response**: JSON object containing the prediction result:
  ```json
  {
    "prediction": "yes" or "no"
  }
