from django.contrib import admin
from django.urls import path, include, register_converter

from . import views
# from .converters import DateConverter

# register_converter(DateConverter, 'date')

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('event/create', views.EventCreate.as_view(), name='event_create'),
    
    
    # path('dashboard/pick_date', views.pick_date, name='pick_date'),
    
    path('dashboard/date_detail/', views.date_detail, name='date_detail'),
    
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]
