import server
from tests.conftest import client


class TestUnit:

    def setup_method(self):
        server.clubs = server.loadClubs()
        server.competitions = server.loadCompetitions()

    def test_login_unknown_email(self, client):
        response = client.post('/showSummary', data={'email': 'unknown@example.com'})
        assert response.status_code == 200

    def test_login_unknown_email_returns_error(self, client):
        response = client.post('/showSummary', data={'email': 'unknown@test.com'})
        assert response.status_code == 200
        assert b"Sorry, that email was not found." in response.data

    def test_login_known_email_returns_welcome(self, client):
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200
        assert b'Welcome' in response.data

    def test_points_deducted_after_booking(self, client):
        response = client.post('/purchasePlaces', data={
            'competition': 'Future Competition',
            'club': 'Simply Lift',
            'places': '3'
        })
        assert b'Points available: 10' in response.data

    def test_cannot_book_more_than_12_places(self, client):
        response = client.post('/purchasePlaces', data={
            'competition': 'Future Competition',
            'club': 'Simply Lift',
            'places': '13'
        })
        assert b'You cannot book more than 12 places' in response.data

    def test_cannot_book_with_insufficient_points(self, client):
        response = client.post('/purchasePlaces', data={
            'competition': 'Future Competition',
            'club': 'Iron Temple',
            'places': '5'
        })
        assert b'You do not have enough points' in response.data

    def test_cannot_book_more_places_than_available(self, client):
        response = client.post('/purchasePlaces', data={
            'competition': 'Future Competition',
            'club': 'Simply Lift',
            'places': '6'
        })
        assert b'Not enough places available' in response.data

    def test_cannot_book_past_competition(self, client):
        response = client.post('/purchasePlaces', data={
            'competition': 'Spring Festival',
            'club': 'Simply Lift',
            'places': '1'
        })
        assert b'You cannot book a past competition' in response.data

    def test_public_points_board(self, client):
        response = client.get('/pointsDisplay')
        assert response.status_code == 200
        assert b'Simply Lift' in response.data
        assert b'Iron Temple' in response.data
        assert b'She Lifts' in response.data
