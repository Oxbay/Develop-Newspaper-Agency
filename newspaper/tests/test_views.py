# from django.test import TestCase, Client
# from django.urls import reverse
#
# from newspaper.models import Redactor, Topic, Newspaper
#
#
# NEWSPAPER_LIST_URL = reverse("newspaper:newspaper-list")
#
#
# class NewspaperListViewTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         topic = Topic.objects.create(name='Test Topic')
#         for i in range(10):
#             Newspaper.objects.create(title=f'Test Newspaper {i}', topic=topic)
#
#     def test_newspaper_list_view(self):
#         response = self.client.get(reverse(NEWSPAPER_LIST_URL))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "newspaper/newspaper_list.html")
#         self.assertTrue('paginator' in response.context)
#         self.assertTrue('page_obj' in response.context)
#         self.assertEqual(len(response.context['page_obj']), 5)
#
#     def test_newspaper_list_view_search(self):
#         response = self.client.get(reverse(NEWSPAPER_LIST_URL))
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue('page_obj' in response.context)
#         self.assertEqual(len(response.context['page_obj']), 10)
