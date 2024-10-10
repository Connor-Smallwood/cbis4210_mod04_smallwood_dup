from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy object globally (but don't bind to app yet)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Use your JawsDB MySQL connection string
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://llhtyotodwxbjg0v:qua7h46709vukc28@etdq12exrvdjisg6.cbetxkdyhwsb.us-east-1.rds.amazonaws.com/ue3mk9oxlac1yly6'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind the database object to this app instance
    db.init_app(app)

    # Register your routes blueprint (replace this with your actual routes)
    from .routes import main
    app.register_blueprint(main)

    # Ensure tables are created (you may use Flask-Migrate later for production)
    with app.app_context():
        db.create_all()

    return app


