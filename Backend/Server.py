from flask import Flask
from extensions import db, ma  
from routes import user_bp  
import os
from flask_cors import CORS

app = Flask(__name__)

CORS(user_bp, resources={r"/*": {"origins": "*", "supports_credentials": True}})

base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, "dp.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
ma.init_app(app)

# Register blueprint
app.register_blueprint(user_bp,url_prefix='/')

# Create database tables
with app.app_context():
    db.create_all()
    print("Database schema created successfully.")

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
