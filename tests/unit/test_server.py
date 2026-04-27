from tests.conftest import client


def test_login_unknown_email(client):
    response = client.post('/showSummary', data={'email': 'unknown@example.com'})
    assert response.status_code == 200

def test_login_unknown_email_returns_error(client):
    response = client.post('/showSummary', data={'email': 'unknown@test.com'})
    assert response.status_code == 200
    assert b"Sorry, that email was not found." in response.data

def test_login_known_email_returns_welcome(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_points_deducted_after_booking(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '3'
    })
    assert b'Points available: 10' in response.data
