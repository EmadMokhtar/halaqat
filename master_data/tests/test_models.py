from django.test import TestCase
from django.core.exceptions import ValidationError

from master_data.models import Nationality


class NationalityModeTestCases(TestCase):
    def setUp(self):
        self.nationality, created = Nationality(name='Egyptian')

    def test_create_new_nationality(self):
        new_nationality = Nationality(name='American')
        new_nationality.save()

        self.assertTrue(new_nationality.pk)
        self.assertTrue(new_nationality.is_active)
        self.assertIsInstance(new_nationality, Nationality)

    def test_update_nationality(self):
        self.nationality.name = 'Egypt'
        self.nationality.save()

        self.assertTrue(self.nationality.pk)
        self.assertNotEqual('Egyptian', self.nationality.name)

    def test_delete_nationality(self):
        self.nationality.delete()

        self.assertFalse(self.nationality.pk)

    def test_add_new_nationality_with_duplicate_name(self):
        new_nationality = Nationality(name=self.nationality.name)

        with self.assertRaises(ValidationError):
            new_nationality.save()

    def test_deactivate_nationality(self):
        self.nationality.is_active = False
        self.nationality.save()

        self.assertFalse(self.nationality.is_active)
