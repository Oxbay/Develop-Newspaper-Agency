from django.test import TestCase
from newspaper.forms import RedactorCreationForm, RedactorUpdateForm, NewspaperSearchForm


class RedactorCreationFormTest(TestCase):
    def test_redactor_creation_form(self):
        form_data = {
            'username': 'test_user',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!',
            'years_of_experience': 5,
            'first_name': 'John',
            'last_name': 'Doe',
        }

        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())


class RedactorUpdateFormTest(TestCase):
    def test_redactor_update_form(self):
        redactor_data = {
            'username': 'test_user',
            'years_of_experience': 5,
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com',
        }

        form = RedactorUpdateForm(data=redactor_data)
        self.assertTrue(form.is_valid())


class NewspaperSearchFormTest(TestCase):
    def test_newspaper_search_form(self):
        search_data = {
            'title': 'Test Title',
        }

        form = NewspaperSearchForm(data=search_data)
        self.assertTrue(form.is_valid())
