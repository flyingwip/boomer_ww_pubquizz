from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from core.models import Quizz

from quizz.serializers import QuizzSerializer

# /api/quizz/quizzes
QUIZZES_URL = reverse('quizz:quizz-list')


def sample_quizz(**params):
    """Create and return a sample quizz"""
    defaults = {
        'title': 'Boomer WW II Quizz',
        'description': 'Are You A World War II Whiz?'
    }
    defaults.update(params)

    return Quizz.objects.create(**defaults)


class PublicQuizzesApiTest(TestCase):
    """Test unauthenticated quizz api access"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """ Test that authentication is required """

        res = self.client.get(QUIZZES_URL)

        self.assertTrue(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateQuizzesApiTests(TestCase):
    """Test authenticated quizz API access"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@londonappdev.com',
            'password'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_recipes(self):
        """Test retrieving a list of recipes"""
        sample_quizz()
        sample_quizz()

        res = self.client.get(QUIZZES_URL)

        quizzes = Quizz.objects.all()
        serializer = QuizzSerializer(quizzes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
