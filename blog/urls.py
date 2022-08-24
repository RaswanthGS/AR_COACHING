from . import views
from django.urls import path

urlpatterns = [
    path('',views.main, name='main'),
    path('pages/<tag>', views.page),
    path('sample',views.sample, name='sample'),
    path('about',views.about, name='about'),
    path('slogin',views.slogin, name='slogin'),
    path('login',views.login, name='login'),
]