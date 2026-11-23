from django.http import JsonResponse
from django.shortcuts import render
from .models import Course

# Демонстрація формату JSON (НЕ фінальний endpoint):
def example_json(request):
    return JsonResponse({"message": "Hello, Django!"})


def course_list(request):
    courses = Course.objects.filter(status="published")
    return render(request, "courses/list.html", {"courses": courses})
    pass


def course_api(request):
    courses = Course.objects.filter(status="published")
    data = list(courses.values("title", "capacity"))
    return JsonResponse({"courses": data})
    pass