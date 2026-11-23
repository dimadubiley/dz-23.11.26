from django.urls import path
from . import views

app_name = "courses"
urlpatterns = [
    path("courses/", views.course_list, name="list"),
    path("api/courses/", views.course_api, name="api"),
]