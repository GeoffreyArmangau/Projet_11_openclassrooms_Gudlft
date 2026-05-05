from tests.conftest import client


def test_full_booking_happy_path(client):
    client.post('/showSummary', data={'email': 'john@simplylift.co'})
    response = client.post('/purchasePlaces', data={
        'competition': 'Future Competition',
        'club': 'Simply Lift',
        'places': '2'
    })
    assert b'Great-booking complete!' in response.data
    assert b'Points available: 11' in response.data

def test_full_booking_sad_path_unknown_email(client):
    response = client.post('/showSummary', data={'email': 'hacker@evil.com'})
    assert b'Sorry, that email was not found.' in response.data
    assert b'Points available' not in response.data

def test_full_booking_sad_path_past_competition(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '1'
    })
    assert b'You cannot book a past competition' in response.data

def test_points_board_accessible_without_login(client):
    response = client.get('/pointsDisplay')
    assert response.status_code == 200
    assert b'Points Board' in response.data
