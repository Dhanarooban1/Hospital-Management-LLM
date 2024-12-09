from flask import Flask
from Routers import user_bp
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})
app.register_blueprint(user_bp, url_prefix='/')
if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)