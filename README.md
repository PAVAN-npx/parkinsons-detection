# 🧠✨ Parkinson's Disease Detection API 🎉

Welcome to the **Parkinson's Disease Detection API**! This project leverages advanced machine learning techniques to predict the presence of Parkinson's disease based on voice measurements. The API is built with **Flask** and **SVM** and features **dynamic animations** and **super styling** for an engaging user experience.

🚀 **Deployed at:** [Parkinson's Detection](https://parkinsons-detection-avxi.onrender.com)

## 🌟 Features
- 🎯 **High Accuracy Prediction**: Uses a robust **SVM model** to predict Parkinson's disease.
- 🌀 **Animated User Interaction**: Every action, from button clicks to form submissions, is accompanied by smooth animations and hover effects.
- ⚡ **Lightning Fast**: Optimized for rapid response times and seamless user experience.
- 🖼️ **Visual Feedback**: Predictions come with stunning visuals for clear insights.
- 🌐 **Cross-Origin Support**: CORS-enabled for easy integration with web apps.
- 🛠 **Deployed on Render** for hassle-free usage.

## 🌀 Animations & Styling 🎨
- **Smooth Page Transitions**: All endpoints feature animated loading spinners, slide-in effects, and fade transitions.
- **Hover Effects**: Buttons and input fields have hover effects that scale and change color with fluid motion.
- **Dynamic Loading Bars**: While waiting for predictions, a visually appealing progress bar keeps users engaged.
- **CSS Keyframes**: Used to create infinite animations like glowing buttons, shaking error messages, and success icons.
- **Responsive Design**: Frontend is built with flexible layouts that adapt to all screen sizes, offering users a mobile-first experience.

## 🚦 API Endpoints

### 🏠 Home Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Response**: A friendly message with spinning text effects: `"Hello, World"`

### 🔮 Predict Endpoint
- **URL**: `/predict`
- **Method**: `POST`
- **Request Body**:
  - `data`: A JSON array of voice measurement values, elegantly animated input forms.

- **Response**: JSON object containing the animated prediction:
  ```json
  {
    "prediction": "🎉 yes" or "😞 no"
  }
