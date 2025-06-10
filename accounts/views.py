from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

from blogs.models import Blog, BlogPost

def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        print("POST data:", request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("blogs:index")

    context = {"form": form}
    return render(request, "registration/register.html", context)

def my_account(request):
    """Show user's account information."""
    user_blogs = Blog.objects.filter(owner=request.user.id)
    user_blogs_ids = [blog.id for blog in user_blogs]
    user_posts = BlogPost.objects.filter(blog__in=user_blogs_ids)
    context = {"user_blogs": user_blogs, "user_posts": user_posts}
    return render(request, "registration/my_account.html", context)