from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "capacity")
    list_filter = ("status",)
    search_fields = ("title",)