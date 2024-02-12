from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug:post>', views.post_detail, name='post_detail'),
    path('activities', views.activities, name='activities'),
    path('about-us', views.about, name='about'),
    path('supportus/', views.supportus, name='supportus'),
]