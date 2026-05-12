from flask import Blueprint
from flask import request
from flask import jsonify

mobile_bp = Blueprint(
    'mobile',
    __name__
)

latest_data = {}

@mobile_bp.route(
    '/mobile-data',
    methods=['POST']
)
def mobile_data():

    global latest_data

    latest_data = request.json

    print(latest_data)

    return jsonify({
        'status':'received'
    })

@mobile_bp.route(
    '/live-data'
)
def live_data():

    return jsonify(
        latest_data
    )