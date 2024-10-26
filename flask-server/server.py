from flask import Flask, request, jsonify
from flask_cors import CORS
from db_setup import db
from routes.products import products_bp
from datetime import datetime, timedelta
import threading

app = Flask(__name__)
CORS(app) # Allows cross-origin requests from React frontend

# Config SQLite database

# Tells Flask-SQLAlchemy to use an SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
# Set this to False to improve performance and avoid seeing unnecessary warnings.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Set up the database
db.init_app(app)

# Register blueprints
app.register_blueprint(products_bp)


# Initialize the database
with app.app_context():
    db.create_all()

# Members API route
@app.route("/members")

def members():
  return {"members": ["Member1", "Member2", "Member3"]}


if __name__ == "__main__":
  app.run(debug=True)