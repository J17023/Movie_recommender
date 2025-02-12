from django.test import TestCase
from movies.models import movies_model
from django.db import IntegrityError

class TestMovieModel(TestCase):

    def setUp(self):
        self.movie = movies_model.objects.create(title = "bee movie",
                                                description = "it's just a test movie", 
                                                rate = 9.0 )
    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "bee movie")
        self.assertEqual(self.movie.description, "it's just a test movie")
        self.assertEqual(self.movie.rate, 9.0)

    def test_title_is_unique(self):
        with self.assertRaises(IntegrityError):
            movies_model.objects.create(title = "bee movie",
                                        description = "dsasd",
                                        rate = 8.0)


