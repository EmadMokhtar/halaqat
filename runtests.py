#!/usr/bin/env python
import os
import subprocess
import sys

import coverage
import django
from django.conf import settings
from django.test.utils import get_runner

FLAKE8_ARGS = ["--ignore=E501", "--exclude=halaqat/settings/*"]
APPS = ["back_office", "master_data", "students"]
EXCLUDE_FILES = ["halaqat/__init__.py", "halaqat/settings/*",
                 "*/migrations/*", "*/tests/*"]


def exit_on_failure(command, message=None):
    if command:
        sys.exit(command)


def flake8_main(args):
    print('Running: flake8', args)
    command = subprocess.call(['flake8'] + args)
    print("Failed: flake8 failed." if command else "Success. flake8 passed.")
    return command


def run_django_tests_with_coverage():
    if __name__ == "__main__":
        # Set up and start test coverage
        cov = coverage.coverage(source=APPS, omit=EXCLUDE_FILES)
        cov.start()
        # Setup and start Django tests
        django.setup()
        TestRunner = get_runner(settings)
        test_runner = TestRunner()
        failures = test_runner.run_tests(APPS)
        if bool(failures):
            cov.erase()
            sys.exit("Tests Failed. Coverage Cancelled.")
        # If success show coverage results
        cov.stop()
        cov.save()
        cov.report()  # Show report on terminal
        cov.html_report(directory='covhtml')  # Export HTML report


if __name__ == "__main__":
    exit_on_failure(flake8_main(APPS + FLAKE8_ARGS))
    exit_on_failure(run_django_tests_with_coverage())
