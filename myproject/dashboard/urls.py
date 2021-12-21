from . import views
from django.urls import path 

urlpatterns = [
    path('', views.dashboard_home,name = 'dashboard-home'),
    # path('about/',views.about, name = 'board-about')
]