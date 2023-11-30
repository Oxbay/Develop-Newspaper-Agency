from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from newspaper.models import Newspaper, Topic, Redactor
from django.urls import reverse


class NewspaperModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        topic = Topic.objects.create(name='Test Topic')

        redactor = Redactor.objects.create(username='test_redactor', first_name='Test', last_name='Redactor')

        cls.newspaper = Newspaper.objects.create(title='Test Title', content='Test Content',
                                                 published_date=timezone.now(), topic=topic)
        cls.newspaper.publishers.add(redactor)

    def test_newspaper_title(self):
        newspaper = Newspaper.objects.get(id=self.newspaper.id)
        self.assertEqual(newspaper.title, 'Test Title')

    def test_newspaper_content(self):
        newspaper = Newspaper.objects.get(id=self.newspaper.id)
        self.assertEqual(newspaper.content, 'Test Content')

    def test_newspaper_published_date(self):
        newspaper = Newspaper.objects.get(id=self.newspaper.id)
        self.assertIsNotNone(newspaper.published_date)

    def test_newspaper_topic(self):
        newspaper = Newspaper.objects.get(id=self.newspaper.id)
        self.assertEqual(newspaper.topic.name, 'Test Topic')

    def test_newspaper_redactors(self):
        newspaper = Newspaper.objects.get(id=self.newspaper.id)
        redactors = newspaper.publishers.all()
        self.assertEqual(redactors.count(), 1)
        self.assertEqual(redactors[0].username, 'test_redactor')

    def test_newspaper_absolute_url(self):
        newspaper = Newspaper.objects.get(id=self.newspaper.id)
        expected_url = reverse('newspaper:newspaper-details', args=[str(self.newspaper.id)])
        self.assertEqual(newspaper.get_absolute_url(), expected_url)


class TopicModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Topic.objects.create(name='Test Topic')
        Topic.objects.create(name='B Topic')
        Topic.objects.create(name='A Topic')

    def test_topic_ordering(self):
        topics = Topic.objects.all().order_by('name')
        expected_order = ['A Topic', 'B Topic', 'Test Topic']

        topics_str = [str(topic) for topic in topics]

        self.assertListEqual(topics_str, expected_order)


class RedactorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.redactor = get_user_model().objects.create(
            username="test_redactor",
            first_name="Test",
            last_name="Redactor",
            years_of_experience=5
        )

    def test_redactor_str(self):
        redactor = get_user_model().objects.get(id=self.redactor.id)
        self.assertEqual(str(redactor), 'test_redactor (Test Redactor)')

    def test_redactor_years_of_experience(self):
        redactor = get_user_model().objects.get(id=self.redactor.id)
        self.assertEqual(redactor.years_of_experience, 5)

    def test_redactor_absolute_url(self):
        redactor = get_user_model().objects.get(id=self.redactor.id)
        expected_url = reverse('newspaper:redactor-detail', kwargs={'pk': redactor.pk})
        self.assertEqual(redactor.get_absolute_url(), expected_url)
