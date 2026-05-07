from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ttad:ttad123@db:5432/ttad_db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "ttad-secret-key"

    db.init_app(app)
    jwt.init_app(app)

    from .models import User, Formation

    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    from .routes.formations import formations_bp
    app.register_blueprint(formations_bp, url_prefix="/api/formations")

    @app.route("/")
    def home():
        return {"message": "TTAD API is running 🚀"}

    return app