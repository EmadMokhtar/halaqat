import random
import string


def generate_random_letters(length):
    return ''.join([random.choices(string.letters) for _ in range(length)])


def generate_random_numbers(length):
    return ''.join([random.choices(string.numbers) for _ in range(length)])