from decimal import Decimal
from django.db import IntegrityError
from django.test import TestCase
from .models import ClassType


class ClassTypeClassTypeTestCases(TestCase):
    """
    Testing Class Type model
    """
    def setUp(self):
        self.class_type, created = ClassType.objects.get_or_create(name='Class Type 1',
                                                                   monthly_fees=Decimal(12))

    def test_create_new_class_type(self):
        new_class_type = ClassType(name='Class Type 2',
                                   monthly_fees=Decimal(10))
        new_class_type.save()

        self.assertEqual(type(new_class_type), ClassType)
        self.assertTrue(new_class_type.pk)

    def test_update_class_type(self):
        new_monthly_fees = Decimal(15)
        self.class_type.monthly_fees = new_monthly_fees
        self.class_type.save()
        self.assertEqual(new_monthly_fees, self.class_type.monthly_fees)
        self.assertTrue(self.class_type.pk)

    def test_delete_class_type(self):
        self.class_type.delete()
        self.assertFalse(self.class_type.pk)

    def test_create_class_type_with_duplicate_names(self):
        new_class_type = ClassType(name='Class Type 1',
                                   monthly_fees=Decimal(10))
        self.assertRaises(IntegrityError, lambda: new_class_type.save())
