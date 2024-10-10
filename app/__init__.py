from flask import Flask

def create_app():
    app = Flask(__name__)

    # Use your JawsDB MySQL connection string
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@hostname/databasename'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app

