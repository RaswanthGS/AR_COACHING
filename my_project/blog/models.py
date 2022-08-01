from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class Content(models.Model):
	title = models.CharField(max_length=100)
	sub_title = models.CharField(max_length=200)
	subject = models.TextField()
	nickname = models.CharField(max_length=20)

	def __str__(self) -> str:
		return self.title

class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	tag =  models.CharField(max_length=255, null=False)
	link = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.title

class Announcement(models.Model):
	announcement = models.TextField(max_length=500)
	time = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.announcement
