from flask import Blueprint, jsonify
import pandas as pd

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/analytics', methods=['GET'])
def analytics():

    data = pd.read_csv('../dataset/student_behavior.csv')

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
        "focus_score": focus_score,
        "average_focus_duration": avg_focus,
        "average_switches": avg_switches,
        "distraction_rate": distraction_rate
    })