from django.test import TestCase, Client
from .models import *


class MovieViewSetTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.movie = Movie.objects.create(name='Avatar', year=2022, genre='man', imdb=123)
        self.movie2 = Movie.objects.create(name='Poos in Boots', year=2023, genre='man2', imdb=589)
        self.actor = Actor.objects.create(name='Actor', birthdate='2023-01-01')

    def test_movie(self):
        response = self.client.get('/movie/')
        data = response.data

        self.assertEquals(len(data), 2)
        self.assertEquals(data[0]['name'], 'Avatar')
        self.assertEquals(data[0]['year'], 2022)
        self.assertEquals(data[0]['genre'], 'man')
        self.assertEqual(data[0]['imdb'], 123)

    def test_search(self):
        response = self.client.get('/movie/?search=man')
        data = response.data

        self.assertEquals(len(data), 2)
        self.assertEquals(data[0]['name'], 'Avatar')
        self.assertEquals(data[0]['imdb'], 123)
        self.assertEquals(data[0]['genre'], 'man')

    def test_filter(self):
        response = self.client.get('/movie/?order=58')
        data = response.data

        self.assertEquals(len(data), 2)
        self.assertEquals(data[1]['imdb'], 589)
