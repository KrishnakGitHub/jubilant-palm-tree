from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Category
from .forms import BlogPostForm

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog:post_list')
    else:
        form = BlogPostForm()
    category = Category.objects.all()
    return render(request, 'blog/create_blog_post.html', {'form': form, 'category': category})

def post_list(request):
    posts = BlogPost.objects.filter(is_draft=False)
    return render(request, 'blog/post_list.html', {'posts': posts})