from flask import Flask
from flask_cors import CORS
import os

from routes.mobile_data import mobile_bp
from routes.analytics import analytics_bp
from routes.upload import upload_bp

from twilio.rest import Client

app = Flask(__name__)

CORS(app)

# =========================
# Twilio Setup
# =========================

account_sid = os.environ.get(
    "TWILIO_ACCOUNT_SID"
)

auth_token = os.environ.get(
    "TWILIO_AUTH_TOKEN"
)

client = Client(
    account_sid,
    auth_token
)

def send_parent_alert(message):

    client.messages.create(

        body=message,

        from_="+99550685918",

        to="+919550685918"
    )

# =========================
# Blueprints
# =========================

app.register_blueprint(
    analytics_bp
)

app.register_blueprint(
    upload_bp
)

app.register_blueprint(
    mobile_bp
)

# =========================
# Routes
# =========================

@app.route('/')

def home():

    return "AI Cognitive Drift Backend Running"

@app.route('/test-alert')

def test_alert():

    send_parent_alert(

        "Student distracted during Zoom class"
    )

    return "Alert Sent Successfully"

# =========================
# Run App
# =========================

if __name__ == '__main__':

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(

        host='0.0.0.0',

        port=port
    )