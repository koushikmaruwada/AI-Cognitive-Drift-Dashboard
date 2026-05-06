from flask import Blueprint, request, jsonify
import joblib
import numpy as np

predict_bp = Blueprint('predict', __name__)

model = joblib.load('models/distraction_model.pkl')

@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.json

    features = np.array([
        data['switches'],
        data['scroll_speed'],
        data['notifications'],
        data['focus_duration']
    ]).reshape(1, -1)

    prediction = model.predict(features)

    return jsonify({
        'distraction_level': prediction[0]
    })