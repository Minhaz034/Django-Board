from . import views
from django.urls import path 

urlpatterns = [
    path('', views.home,name = 'board-home'),
    path('about/',views.about, name = 'board-about')
]