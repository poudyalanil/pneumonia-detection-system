from django.test import TestCase

from . models import Blog, Category, Tags

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(category="test_case_1")
        Category.objects.create(category="test_case_2")

    def testCategoryNames1(self):
        test_case_1 = Category.objects.get(category="test_case_1")
        self.assertEqual(test_case_1.category,"test_case_1")

    def testCategoryNames2(self):
        test_case_2 = Category.objects.get(category="test_case_2")
        self.assertEqual(test_case_2.category,"test_case_2")

class TagsTestCase(TestCase):
    def setUp(self):
        Tags.objects.create(tag="test_tag")

    def testTagName(self):
        test = Tags.objects.get(tag="test_tag")
        self.assertEqual(test.tag,"test_tag")



