import pytest
from server import app
import server


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_data():
    server.clubs = server.loadClubs()
    server.competitions = server.loadCompetitions()
