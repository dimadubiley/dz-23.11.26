from django.test import TestCase
from django.urls import reverse
from .models import Course

class CourseTests(TestCase):
    def test_list_page_opens(self):
        response = self.client.get(reverse("courses:list"))
        self.assertEqual(response.status_code, 200)

    def test_api_excludes_drafts(self):
        Course.objects.create(title="Python", slug="python", capacity=10, status="published")
        Course.objects.create(title="Secret", slug="secret", capacity=5, status="draft")

        response = self.client.get(reverse("courses:api"))
        self.assertEqual(response.status_code, 200)

        titles = [c["title"] for c in response.json()["courses"]]
        self.assertEqual(titles, ["Python"])