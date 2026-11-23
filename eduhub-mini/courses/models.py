from django.db import models
from django.core.validators import MinValueValidator

class Course(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title