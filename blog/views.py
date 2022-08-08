from django.shortcuts import render
from .models import Content, Post, Announcement
from .forms import PostForm, AnnouncementForm

def main(request):
    context={
        'posts' : Post.objects.all().order_by('-date_posted'),
        'announcements' : Announcement.objects.all()
    }
    return render(request, "blog/mainpage.html", context)

def pgtrb(request):
    context={
        'contents':Content.objects.filter(nickname='PG TRB'),
        'posts' : Post.objects.filter(tag='PG TRB').order_by('-date_posted'),
        'announcements' : Announcement.objects.all()
    }
    return render(request, "blog/content.html", context)
    
def polytrb(request):
    context={
        'contents':Content.objects.filter(nickname='POLY TRB'),
        'posts' : Post.objects.filter(tag='POLY TRB').order_by('-date_posted'),
        'announcements' : Announcement.objects.all()
    }
    return render(request, "blog/content.html", context)

def enggtrb(request):
    context={
        'contents':Content.objects.filter(nickname='ENGG TRB'),
        'posts' : Post.objects.filter(tag='ENGG TRB').order_by('-date_posted'),
        'announcements' : Announcement.objects.all()
    }
    return render(request, "blog/content.html", context)

def tnset(request):
    context={
        'contents':Content.objects.filter(nickname='TNSET'),
        'posts' : Post.objects.filter(tag='TNSET').order_by('-date_posted'),
        'announcements' : Announcement.objects.all()
    }
    return render(request, "blog/content.html", context)

def ugtrb(request):
    context={
        'contents':Content.objects.filter(nickname='UG TRB'),
        'posts' : Post.objects.filter(tag='UG TRB').order_by('-date_posted'),
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

