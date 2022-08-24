from django.shortcuts import render
from .models import Content, Post, Announcement
from .forms import PostForm, AnnouncementForm

def main(request):
    context={
        'posts' : Post.objects.all().order_by('-date_posted'),
        'announcements' : Announcement.objects.all()
    }
    return render(request, "blog/mainpage.html", context)

def page(request, tag):
    context={
        'contents':Content.objects.filter(nickname=tag),
        'posts' : Post.objects.filter(nickname=tag).order_by('-date_posted'),
        'announcements' : Announcement.objects.all()
    }
    return render(request, "blog/content.html", context)

def sample(request):
    return render(request, "blog/sample.html")
    
def about(request):
    return render(request, "blog/about.html")

def slogin(request):
    return render(request, "blog/slogin.html")

def login(request):
    return render(request, "blog/login.html")

