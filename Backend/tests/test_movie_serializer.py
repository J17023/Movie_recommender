from django.test import TestCase
from movies.serializers import movie_serializer

class TestMovieSerializer(TestCase):

    def setUp(self):
        self.movie_data = {'title':'Inception', 'description':'no description', 'rate':8.0 }
        self.serializer = movie_serializer(data = self.movie_data)

    def test_serializer_valid(self):
        self.assertTrue(self.serializer.is_valid())
        self.assertEqual(self.serializer.validated_data, self.movie_data)