from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from core.models import Quizz


def sample_quizz(**params):
    """Create and return a sample quizz"""
    defaults = {
        'title': 'Boomer WW II Quizz',
        'description': 'Are You A World War II Whiz?'
    }
    defaults.update(params)

    return Quizz.objects.create(**defaults)


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@londonappdev.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@londonappdev.com',
            password='password123',
            name='Test User Full Name',
        )

    def test_users_listed(self):
        """Test that users are listed on the user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page_change(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_quizz_listed(self):
        """Test that quizzes are listed on the user page"""
        test_quizz = str(sample_quizz())
        url = reverse('admin:core_quizz_changelist')
        res = self.client.get(url)

        # print(res.data)
        self.assertContains(res, test_quizz)
        # self.assertContains(res, self.user.email)
