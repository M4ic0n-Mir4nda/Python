import pytest
from app import create_app, db


@pytest.fixture
def test_app():
    app = create_app(config_type='testing')
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(test_app):
    return test_app.test_client()
