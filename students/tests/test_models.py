import datetime
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase

from back_office.models import Teacher, ClassType, HalaqatClass
from students.models import Student
from helpers import generate_random_numbers


class StudentModelTestCase(TestCase):
    """
    Testing Student model
    """

    def setUp(self):
        self.student, created = Student.objects.get_or_create(
            name='New Student',
            dob=datetime.today(),
            civil_id='1234567890',
            mobile_number=generate_random_numbers(12),
            home_number=generate_random_numbers(12),
            parent_number=generate_random_numbers(12))

        self.user = User.objects.create_user('male_user', 'm.user@company.com', 'password',
                                             first_name='first_name')
        self.teacher, created = Teacher.objects.get_or_create(user=self.user, gender='M',
                                                              civil_id='123123')
        self.class_type, created = ClassType.objects.get_or_create(name='Class Type 1',
                                                                   monthly_fees=Decimal(12))
        self.halaqat_class, created = HalaqatClass.objects.get_or_create(teacher=self.teacher,
                                                                         name='Class 101',
                                                                         type=self.class_type,
                                                                         gender='M',
                                                                         days=['SUN', 'WED'],
                                                                         start_time=datetime.time(20),
                                                                         end_time=datetime.time(22),
                                                                         first_semester_start=datetime.date(2015, 9, 1),
                                                                         first_semester_end=datetime.date(2015, 10, 30),
                                                                         second_semester_start=datetime.date(2016, 2, 1),
                                                                         second_semester_end=datetime.date(2016, 6, 1))

    def test_create_new_student(self):
        new_student = Student(name='New Student',
                              dob=datetime.today(),
                              civil_id='1234567890',
                              mobile_number=generate_random_numbers(12),
                              home_number=generate_random_numbers(12),
                              parent_number=generate_random_numbers(12))
        new_student.save()

        self.assertIsInstance(new_student, Student)
        self.assertTrue(new_student.pk)
        self.assertEquals('P', new_student.status)

    def test_update_student_profile(self):
        self.student.name = 'Updated Student'
        self.student.save()

        self.assertEqual('Updated Student', self.student.name)
        self.assertTrue(self.student.pk)

    def test_delete_existing_student(self):
        self.student.delete()

        self.assertFalse(self.student.pk)

    def test_activate_student(self):
        self.student.activate()

        self.assertEqual('A', self.student.status)

    def test_suspend_student(self):
        self.student.suspend()

        self.assertEqual('S', self.student.status)

    def test_put_student_on_leave(self):
        self.student.on_leave()

        self.assertEqual('L', self.student.status)
