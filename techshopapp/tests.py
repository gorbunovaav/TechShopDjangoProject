from django.test import TestCase
from .models import Feedback, Item, User
from django.urls import reverse


class TestBlogapp(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            name='test_user',
            age=25,
            email='test@mail.ru',)


    def test_feedback_create(self):
        feedback_data = {
            'item': 'Item1',
            'title': 'test_title',
            'content': 'test_content',
            'author': self.user,
            'is_published': True,
            'published_date': '2024-01-01'}

        response = self.client.post(reverse('feedback_create'), data=feedback_data)
        self.assertEqual(response.status_code, 200)

    # def tearDown(self):
    #     User.objects.all.delete()


class FeedbackListViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            name='test_user',
            age=25,
            email='test@mail.ru',)

        self.feedback = Feedback.objects.create(
            item='Item1',
            title='test_title',
            content='test_content',
            author=self.user,
            is_published=True,
            published_date='2024-01-01')

        self.feedback2 = Feedback.objects.create(
            item='Item2',
            title='test_title2',
            content='test_content2',
            author=self.user,
            is_published=True,
            published_date='2024-01-03')

    def test_feedback_list_view(self):
        response = self.client.get(reverse('feedback_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'techshopapp/feedback_list.html')
        self.assertIn('feedback_list', response.context)
        self.assertEqual(len(response.context['feedback_list']), Feedback.objects.count())

