from locust import HttpUser, task, between


class GudlftUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def view_points_board(self):
        self.client.get('/pointsDisplay')

    @task
    def login(self):
        self.client.post('/showSummary', data={'email': 'john@simplylift.co'})

    @task
    def book_places(self):
        self.client.post('/purchasePlaces', data={
            'competition': 'Future Competition',
            'club': 'Simply Lift',
            'places': '2'
        })
