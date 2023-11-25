from django.test import TestCase
from django.urls import reverse

from newspaper.forms import NewspaperSearchForm
from newspaper.models import Newspaper, Redactor, Topic


class ViewsTest(TestCase):
    def setUp(self):
        self.user = Redactor.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_index_view(self):
        response = self.client.get(reverse("newspaper:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/index.html")

    def test_newspaper_list_view(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("newspaper:newspaper-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/newspaper_list.html")

    def test_search_form_initialization(self):
        response = self.client.get(reverse("newspaper:newspaper-list"))
        form = response.context['search_form']
        self.assertIsInstance(form, NewspaperSearchForm)

    def test_topic_list_view(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("newspaper:topic-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/topic_list.html")

    def test_redactor_list_view(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("newspaper:redactor-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/redactor_list.html")
