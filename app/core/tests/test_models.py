from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Quizz, Question


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""

        email = "dont@think.so"
        password = "Testpassword123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for a new user is normalized"""
        email = "test@ALLCAPITALS.COM"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""

        # everything with in the with statement should raise an ValueError
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
            # get_user_model().objects.create_user('test@test.nl', 'test123')

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_quizz_str(self):
        """ Test quizz string representation """
        quizz_title = "Boomer WW II Quizz"
        quizz = Quizz.objects.create(title=quizz_title)

        self.assertEqual(str(quizz), quizz_title)

    def test_question_str(self):
        """ Test question string representation """

        # first create a quizz
        # quizz = Quizz.objects.create(title="Boomer WW II Quizz")

        question_text = """Who was in charge of the attempt to assassinate
                Adolf Hitler on 20 july 1944"""

        question = Question.objects.create(text=question_text)

        self.assertEqual(str(question), question_text)
