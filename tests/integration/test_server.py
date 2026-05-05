from tests.conftest import client


def test_login_and_view_competitions(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'Spring Festival' in response.data
    assert b'Fall Classic' in response.data
    assert b'Future Competition' in response.data

def test_login_and_book_place(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Future Competition',
        'club': 'Simply Lift',
        'places': '2'
    })
    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data

def test_login_and_view_points_board(client):
    response = client.get('/pointsDisplay')
    assert response.status_code == 200
    assert b'Simply Lift' in response.data


def test_logout_redirects_to_index(client):
    response = client.get('/logout')
    assert response.status_code == 302
