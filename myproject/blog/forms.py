from django import forms
from .models import BlogPost, Category

class BlogPostForm(forms.ModelForm):
    category = Category.objects.all()
    
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
