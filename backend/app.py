from flask import Flask
from flask_cors import CORS
import os

from routes.mobile_data import mobile_bp
from routes.analytics import analytics_bp
from routes.upload import upload_bp


app = Flask(__name__)

CORS(app)



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