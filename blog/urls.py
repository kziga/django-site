from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list') # This means the main page should access the view post_list in views.py
]