from decimal import Decimal

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.contrib.auth.models import User
from .models import ClassType, Teacher


class ClassTypeTestCases(TestCase):
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

        self.assertIsInstance(new_class_type, ClassType)
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


class TeacherTestCases(TestCase):
    """
    Testing Teacher model
    """

    def setUp(self):
        self.user = User.objects.create_user('user', 'user@company.com', 'password', first_name='first_name')
        self.teacher, created = Teacher.objects.get_or_create(user=self.user, gender='M', civil_id='123123')

    def test_creating_new_teacher(self):
        new_user = User.objects.create_user('new_teacher', 'user@company.com', 'password')
        new_teacher = Teacher(user=new_user, gender='M', civil_id='34534')
        new_teacher.save()

        self.assertIsInstance(new_teacher, Teacher)
        self.assertTrue(new_teacher.pk)

    def test_update_teacher(self):
        new_teacher_name = 'Awesome Developer'
        self.teacher.user.first_name = new_teacher_name
        self.teacher.user.save()

        self.assertEqual(self.teacher.user.first_name, new_teacher_name)

    def test_deleting_teacher_should_disable_not_deleting(self):
        self.teacher.delete()
        self.assertFalse(self.teacher.user.is_active)

    def test_getting_teacher_full_name(self):
        self.assertNotEqual(self.teacher.full_name, self.user.username)
        self.assertEqual(self.teacher.full_name, self.user.first_name)

    def test_getting_teacher_name_without_name(self):
        self.user.first_name = ''
        self.assertEqual(self.teacher.full_name, self.user.username)
        self.assertNotEqual(self.teacher.full_name, self.user.first_name)

    def test_create_duplicate_teacher_with_name_and_civilid(self):
        new_user = User.objects.create_user('new_teacher', 'user@company.com', 'password', first_name='first_name')
        new_teacher = Teacher(user=new_user, gender='M', civil_id='123123')

        self.assertRaises(ValidationError, lambda :new_teacher.save())
