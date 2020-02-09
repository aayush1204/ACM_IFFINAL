from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name='home'),
	path('team',views.team, name='team'),
	path('events',views.events, name='events'),
	path('djascii',views.djascii, name='djascii'),
	path('loc', views.loc, name='loc'),
	path('contact',views.contact,name='contact')
	]