from flask import Blueprint, request, jsonify
import pandas as pd

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload():

    if 'file' not in request.files:

        return jsonify({
            "error": "No file uploaded"
        }), 400

    file = request.files['file']

    data = pd.read_csv(file)

    avg_focus = round(
        data['focus_duration'].mean(),
        2
    )

    avg_switches = round(
        data['switches'].mean(),
        2
    )

    distraction_rate = round(
        (
            data['label']
            .value_counts(normalize=True)
            .get('Distracted', 0)
        ) * 100,
        2
    )

    focus_score = round(
        100 - (
            (distraction_rate * 0.6)
            + (avg_switches * 2)
        ),
        2
    )

    return jsonify({

        "message":
            "CSV uploaded successfully",

        "rows":
            len(data),

        "focus_score":
            focus_score,

        "average_focus_duration":
            avg_focus,

        "average_switches":
            avg_switches,

        "distraction_rate":
            distraction_rate
    })