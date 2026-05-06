from flask import Flask
from flask_cors import CORS

from routes.analytics import analytics_bp
from routes.upload import upload_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(analytics_bp)
app.register_blueprint(upload_bp)

@app.route('/')
def home():
    return "AI Cognitive Drift Backend Running"

if __name__ == '__main__':
    app.run(debug=True)