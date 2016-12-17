[![Stories in Ready](https://badge.waffle.io/EmadMokhtar/halaqat.png?label=ready&title=Ready)](https://waffle.io/EmadMokhtar/halaqat) [![Codeship badge](https://codeship.com/projects/fb06c070-99ce-0134-528f-7e59fd3fff7f/status?branch=master)](https://app.codeship.com/projects/187798)

# Halaqat - حلقات

## About the project

It's a Django app to manage Quran classes inside Masjid. The application will give you the ability to setup classes and assign teachers and students to it, student will get notification for any action or update happened on profile or class.

The project main goal is to make the process inside centers paperless and fast.

## عن المشروع

برنامج لتنظيم الحلقات في مراكز التحفيظ القرأن الكريم، البرنامج مكتوب بالچانجو ويتيح لك تنظيم وإضافة حلقات وإدخال الطلاب إليها و تحديد المحفظ أو المعلم لكل حلقة و الطالب سيصله إشعارات لو حدِ أي تغيير على الحلقة أو ملفه.

البرنامج هدفه جعل تنظيم الحلقات بدون ورق وإستخدام التكنولوجية لمساعدة مراكز تحفيظ القرأن

# Run locally

* Make sure that you have Python 3.5 installed on your machine.
* Clone the repository `git clone https://github.com/EmadMokhtar/halaqat`
* Go to repository directory `cd halaqat`
* Install requirements `pip install -r requirements/requirements.txt`
* Add Secret key environment variable `export SECRET_KEY="Hamada-Bel-Ganzabeel"`
* Add Django settings module environment variable `export DJANGO_SETTINGS_MODULE="haqalat.settings.local_settings"`
* Do Django migration `python manage.py migrate`
* Run Django development server `python manage.py runserver`
* Open browser and go to http://127.0.0.1:8000


# Packages Used
## Backend
- [Django](https://www.djangoproject.com/)
- [Crispy Forms](http://django-crispy-forms.readthedocs.io/en/latest/)

## Frontend
- [Bootstrap 3](http://getbootstrap.com/)
- [Flatty Bootstrap Theme](https://github.com/mendix/MxBootswatch/blob/master/theme/Flatly.zip)
- [Bootstrap Datetime Picker](http://www.malot.fr/bootstrap-datetimepicker/)
