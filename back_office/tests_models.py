from datetime import date, time
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from .models import ClassType, HalaqatClass, Teacher


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
        with self.assertRaises(IntegrityError):
            new_class_type.save()


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

        # def test_create_duplicate_teacher_with_name_and_civilid(self):
        #     new_user = User.objects.create_user('new_teacher', 'user@company.com', 'password', first_name='first_name')
        #     new_teacher = Teacher(user=new_user, gender='M', civil_id='123123')
        #
        #     self.assertRaises(ValidationError, lambda: new_teacher.save())


class ClassTestCases(TestCase):
    """
    Testing Class model
    """

    def setUp(self):
        self.male_user = User.objects.create_user('male_user', 'm.user@company.com', 'password',
                                                  first_name='first_name')
        self.male_teacher, created = Teacher.objects.get_or_create(user=self.male_user, gender='M',
                                                                   civil_id='123123')
        self.female_user = User.objects.create_user('female_user', 'f.user@company.com', 'password',
                                                    first_name='first_name')
        self.female_teacher, created = Teacher.objects.get_or_create(user=self.female_user,
                                                                     gender='F',
                                                                     civil_id='9860876')
        self.class_type, created = ClassType.objects.get_or_create(name='Class Type 1',
                                                                   monthly_fees=Decimal(12))
        self.halaqat_class, created = HalaqatClass.objects.get_or_create(teacher=self.male_teacher,
                                                                         name='Class 101',
                                                                         class_type=self.class_type,
                                                                         gender='M',
                                                                         days=['SUN', 'WED'],
                                                                         start_time=time(20),
                                                                         end_time=time(22),
                                                                         first_semester_start=date(2015, 9, 1),
                                                                         first_semester_end=date(2015, 10, 30),
                                                                         second_semester_start=date(2016, 2, 1),
                                                                         second_semester_end=date(2016, 6, 1))

    def test_creating_new_class(self):
        new_halaqat_class = HalaqatClass(teacher=self.male_teacher,
                                         name='Class 101',
                                         class_type=self.class_type,
                                         gender='M',
                                         days=['SUN', 'WED'],
                                         start_time=time(20),
                                         end_time=time(22),
                                         first_semester_start=date(2015, 9, 1),
                                         first_semester_end=date(2015, 10, 30),
                                         second_semester_start=date(2016, 2, 1),
                                         second_semester_end=date(2016, 6, 1))
        new_halaqat_class.save()

        self.assertTrue(new_halaqat_class.pk)
        self.assertIsInstance(new_halaqat_class, HalaqatClass)

    def test_update_class(self):
        new_days = ['MON', 'THU']
        self.halaqat_class.days = new_days
        self.halaqat_class.save()

        self.assertEqual(new_days, self.halaqat_class.days)

    def test_deleting_class(self):
        self.halaqat_class.delete()

        self.assertFalse(self.halaqat_class.pk)
        self.assertIsInstance(self.halaqat_class, HalaqatClass)

    def test_assign_male_teacher_to_male_class(self):
        male_halaqat_class = HalaqatClass(teacher=self.male_teacher,
                                          name='Class 101',
                                          class_type=self.class_type,
                                          gender='M',
                                          days=['SUN', 'WED'],
                                          start_time=time(20),
                                          end_time=time(22),
                                          first_semester_start=date(2015, 9, 1),
                                          first_semester_end=date(2015, 10, 30),
                                          second_semester_start=date(2016, 2, 1),
                                          second_semester_end=date(2016, 6, 1))
        male_halaqat_class.save()

        self.assertTrue(male_halaqat_class.pk)
        self.assertIsInstance(male_halaqat_class, HalaqatClass)

    def test_assign_female_teacher_to_female_class(self):
        male_halaqat_class = HalaqatClass(teacher=self.female_teacher,
                                          name='Class 101',
                                          class_type=self.class_type,
                                          gender='F',
                                          days=['SUN', 'WED'],
                                          start_time=time(20),
                                          end_time=time(22),
                                          first_semester_start=date(2015, 9, 1),
                                          first_semester_end=date(2015, 10, 30),
                                          second_semester_start=date(2016, 2, 1),
                                          second_semester_end=date(2016, 6, 1))
        male_halaqat_class.save()

        self.assertTrue(male_halaqat_class.pk)
        self.assertIsInstance(male_halaqat_class, HalaqatClass)

    def test_assign_female_teacher_to_male_class(self):
        male_halaqat_class = HalaqatClass(teacher=self.female_teacher,
                                          name='Class 101',
                                          class_type=self.class_type,
                                          gender='M',
                                          days=['SUN', 'WED'],
                                          start_time=time(20),
                                          end_time=time(22),
                                          first_semester_start=date(2015, 9, 1),
                                          first_semester_end=date(2015, 10, 30),
                                          second_semester_start=date(2016, 2, 1),
                                          second_semester_end=date(2016, 6, 1))

        with self.assertRaises(ValidationError):
            male_halaqat_class.save()

    def test_assign_male_teacher_to_female_class(self):
        female_halaqat_class = HalaqatClass(teacher=self.male_teacher,
                                            name='Class 101',
                                            class_type=self.class_type,
                                            gender='F',
                                            days=['SUN', 'WED'],
                                            start_time=time(20),
                                            end_time=time(22),
                                            first_semester_start=date(2015, 9, 1),
                                            first_semester_end=date(2015, 10, 30),
                                            second_semester_start=date(2016, 2, 1),
                                            second_semester_end=date(2016, 6, 1))

        with self.assertRaises(ValidationError):
            female_halaqat_class.save()

    def test_set_wrong_first_semester_start_date_should_fail(self):
        halaqat_class = HalaqatClass(teacher=self.female_teacher,
                                     name='Class 101',
                                     class_type=self.class_type,
                                     gender='F',
                                     days=['SUN', 'WED'],
                                     start_time=time(20),
                                     end_time=time(22),
                                     first_semester_start=date(2015, 11, 1),
                                     first_semester_end=date(2015, 10, 30),
                                     second_semester_start=date(2016, 2, 1),
                                     second_semester_end=date(2016, 6, 1))

        with self.assertRaises(ValidationError):
            halaqat_class.save()

    def test_set_wrong_first_semester_end_date_should_fail(self):
        halaqat_class = HalaqatClass(teacher=self.female_teacher,
                                     name='Class 101',
                                     class_type=self.class_type,
                                     gender='F',
                                     days=['SUN', 'WED'],
                                     start_time=time(20),
                                     end_time=time(22),
                                     first_semester_start=date(2015, 9, 1),
                                     first_semester_end=date(2015, 6, 30),
                                     second_semester_start=date(2016, 2, 1),
                                     second_semester_end=date(2016, 6, 1))

        with self.assertRaises(ValidationError):
            halaqat_class.save()

    def test_set_wrong_second_semester_start_date_should_fail(self):
        halaqat_class = HalaqatClass(teacher=self.female_teacher,
                                     name='Class 101',
                                     class_type=self.class_type,
                                     gender='F',
                                     days=['SUN', 'WED'],
                                     start_time=time(20),
                                     end_time=time(22),
                                     first_semester_start=date(2015, 9, 1),
                                     first_semester_end=date(2015, 10, 30),
                                     second_semester_start=date(2015, 2, 1),
                                     second_semester_end=date(2016, 6, 1))

        with self.assertRaises(ValidationError):
            halaqat_class.save()

    def test_set_wrong_second_semester_end_date_should_fail(self):
        halaqat_class = HalaqatClass(teacher=self.female_teacher,
                                     name='Class 101',
                                     class_type=self.class_type,
                                     gender='F',
                                     days=['SUN', 'WED'],
                                     start_time=time(20),
                                     end_time=time(22),
                                     first_semester_start=date(2015, 9, 1),
                                     first_semester_end=date(2015, 10, 30),
                                     second_semester_start=date(2016, 2, 1),
                                     second_semester_end=date(2015, 6, 1))

        with self.assertRaises(ValidationError):
            halaqat_class.save()

        # TODO Check that no class with the same type, dates, and teacher

    def test_enroll_one_student(self):
        pass

    def test_enroll_many_student(self):
        pass
