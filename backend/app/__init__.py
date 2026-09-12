from flask import Flask

from app.config import Config
from app.extensions import db
from app.modules.pets.routes import bp as pets_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        if not Pet.query.first():  # seed some sample pets
            db.session.add_all([
                Pet(name="Luna", species="dog", breed="Golden Retriever", price=450.0, stock=2),
                Pet(name="Mochi", species="cat", breed="British Shorthair", price=320.0, stock=1),
                Pet(name="Pip", species="parrot", breed="Cockatiel", price=90.0, stock=3),
            ])
            db.session.commit()

    app.register_blueprint(pets_bp)

    @app.get("/api/health")
    def health():
        return {"status": "ok"}

    return app


from app.models import Pet  # noqa: E402  (import after db init to avoid circulars)