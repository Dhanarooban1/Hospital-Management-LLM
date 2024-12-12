import os
from flask import Flask, jsonify
from Routers import user_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})
app.register_blueprint(user_bp, url_prefix='/')

@app.route('/')
def home():
    return jsonify({"message": "Backend is running successfully!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
