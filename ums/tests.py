from django.test import TestCase
from .models import Normal_User
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="anilpdl", password="anil123")
        User.objects.create_user(username="sameerkhan", password="sameerkhan")
        User.objects.create_user(username="sunilrawal", password="sunilrawal")
        User.objects.create_user(username="prtimapokhrel", password="prtimapokhrel")



       
#Test for user created to not and also test that we can create multiple users at a time 
    def testUser1(self):
        testUser1 = User.objects.get(username="anilpdl")
        self.assertEqual(testUser1.username, "anilpdl")

    def testUser2(self):
        testUser1 = User.objects.get(username="sameerkhan")
        self.assertEqual(testUser1.username, "sameerkhan")

    def testUser3(self):
        testUser1 = User.objects.get(username="sunilrawal")
        self.assertEqual(testUser1.username, "sunilrawal")

    def testUser4(self):
        testUser1 = User.objects.get(username="prtimapokhrel")
        self.assertEqual(testUser1.username, "prtimapokhrel")