from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from newspaper.models import Redactor, Topic, Newspaper


class RedactorAdminTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="test"
        )
        self.client.force_login(self.admin_user)
        self.redactor = Redactor.objects.create(
            username="test_redactor",
            password="test123",
            years_of_experience=5
        )

    def test_redactor_years_of_experience_displayed(self):
        url = reverse("admin:newspaper_redactor_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)


class NewspaperAdminTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="test"
        )
        self.client.force_login(self.admin_user)
        self.topic = Topic.objects.create(name="Test Topic")
        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper",
            content="Test content",
            topic=self.topic
        )

    def test_search_newspaper(self):
        url = reverse("admin:newspaper_newspaper_changelist")
        data = {"q": "Test Newspaper"}
        response = self.client.get(url, data)
        self.assertContains(response, self.newspaper.title)

    def test_filter_newspaper_by_topic(self):
        url = reverse("admin:newspaper_newspaper_changelist")
        data = {"topic__id__exact": self.topic.id}
        response = self.client.get(url, data)
        self.assertContains(response, self.newspaper.title)
