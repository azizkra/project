from django.urls import path
from . import views
from .views import *

app_name = 'center'

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug:post>', views.post_detail, name='post_detail'),
    path('activities', views.activities, name='activities'),
    # path('supportus/', views.supportus, name='supportus'),
]