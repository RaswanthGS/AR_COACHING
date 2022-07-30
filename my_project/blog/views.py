from django.shortcuts import render
from .models import Content, Post, Announcement
from .forms import PostForm, AnnouncementForm

def main(request):
    context={
        'posts' : Post.objects.all().order_by('-date_posted'),
        'announcements' : Announcement.objects.all()
    }
    return render(request, "blog/mainpage.html", context)

def contentPage(request):
    context={
        'contents':Content.objects.filter(nickname='PG TRB'),
        'posts' : Post.objects.filter(tag='PG TRB').order_by('date_posted'),
        'announcements' : Announcement.objects.all()
    }
    return render(request, "blog/content.html", context)
    
def polytrb(request):
    context={
        'posts' : Post.objects.filter(tag='POLY TRB').order_by('date_posted'),
        'announcements' : Announcement.objects.all()
    }
    return render(request, "blog/polytrb.html", context)

def enggtrb(request):
    context={
        'posts' : Post.objects.filter(tag='ENGG TRB').order_by('date_posted'),
        'announcements' : Announcement.objects.all()
    }
    return render(request, "blog/enggtrb.html", context)

def tnset(request):
    context={
        'posts' : Post.objects.filter(tag='TNSET').order_by('date_posted'),
        'announcements' : Announcement.objects.all()
    }
    return render(request, "blog/tnset.html", context)

def ugtrb(request):
    context={
        'posts' : Post.objects.filter(tag='UG TRB').order_by('date_posted'),
        'announcements' : Announcement.objects.all()
    }
    return render(request, "blog/ugtrb.html", context)

def sample(request):
    return render(request, "blog/sample.html")
    
def about(request):
    return render(request, "blog/about.html")

def slogin(request):
    return render(request, "blog/slogin.html")

def login(request):
    return render(request, "blog/login.html")

