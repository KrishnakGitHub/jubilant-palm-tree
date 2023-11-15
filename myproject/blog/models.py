from django.db import models
from myapp.models import User

class Category(models.Model):
    # Mental Health, Heart Disease, Covid19, Immunization
    CATEGORY_CHOICES = [
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19', 'Covid19'),
        ('Immunization', 'Immunization'),
    ]
    name = models.CharField(max_length=255, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/blog_images', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
