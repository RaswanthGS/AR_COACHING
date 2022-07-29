from . import views
from django.urls import path

urlpatterns = [
    path('',views.main, name='main'),
    path('pgtrb',views.pgtrb, name='pgtrb'),
    path('polytrb',views.polytrb, name='polytrb'),
    path('enggtrb',views.enggtrb, name='enggtrb'),
    path('tnset',views.tnset, name='tnset'),
    path('ugtrb',views.ugtrb, name='ugtrb'),
    path('sample',views.sample, name='sample'),
    path('about',views.about, name='about'),
    path('slogin',views.slogin, name='slogin'),
    path('login',views.login, name='login'),

]