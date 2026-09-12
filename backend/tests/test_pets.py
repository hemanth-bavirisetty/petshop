import pytest

from app import create_app
from app.extensions import db as _db
from app.config import Config


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # fast, isolated tests
    TESTING = True


@pytest.fixture()
def client():
    app = create_app(TestConfig)
    with app.test_client() as c:
        with app.app_context():
            _db.create_all()
        yield c


def test_health(client):
    assert client.get("/api/health").json == {"status": "ok"}


def test_create_and_list_pet(client):
    client.post("/api/pets", json={
        "name": "Rocky", "species": "dog", "breed": "Beagle", "price": 300
    })
    pets = client.get("/api/pets").json
    assert any(p["name"] == "Rocky" for p in pets)


def test_get_pet_404(client):
    assert client.get("/api/pets/999").status_code == 404