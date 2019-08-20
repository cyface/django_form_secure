"""
Tests
"""
from django.test import TestCase


class TestTest(TestCase):
    def setUp(self):
        print("Setup")

    def test_one(self):
        print("TEST ONE")
