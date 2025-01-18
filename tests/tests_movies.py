from django.test import TestCase
from movies.models import movies_model

class TestMovieModel(TestCase):

    def setUp(self):
        self.movie = movies_model.objects.create(title = "bee movie",
                                                description = "it's just a test movie", 
                                                rate = 9.0 )
    def test_mvie_creation(self):
        self.assertEqual(self.movie, "bee movie")
        self.assertEqual(self.movie, "it's just a test movie")
        self.assertEqual(self.movie, 9.0)
