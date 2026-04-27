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
        'competition': 'Future Competition',
        'club': 'Simply Lift',
        'places': '3'
    })
    assert b'Points available: 10' in response.data

def test_cannot_book_more_than_12_places(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Future Competition',
        'club': 'Simply Lift',
        'places': '13'
    })
    assert b'You can not book more than 12 places' in response.data

def test_cannot_book_with_insufficient_points(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Future Competition',
        'club': 'Iron Temple',
        'places': '5'
    })
    assert b'You can not book with insufficient points' in response.data

def test_cannot_book_more_places_than_available(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Future Competition',
        'club': 'Simply Lift',
        'places': '6'
    })
    assert b'You can not book more places than available' in response.data

def test_cannot_book_past_competition(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '1'
    })
    assert b'You cannot book a past competition' in response.data
