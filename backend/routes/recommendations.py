from flask import Blueprint, jsonify

recommendation_bp = Blueprint('recommendation', __name__)

@recommendation_bp.route('/recommendations', methods=['GET'])
def recommendations():

    tips = [
        "Disable notifications during study",
        "Take 5 minute break every 45 minutes",
        "Avoid Instagram after 10 PM"
    ]

    return jsonify(tips)