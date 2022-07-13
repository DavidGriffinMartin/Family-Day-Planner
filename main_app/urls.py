from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:user_id>/', views.users_profile, name='users_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('event/create/', views.EventCreate.as_view(), name='event_create'),
    path('event/<int:pk>/update/', views.EventUpdate.as_view(), name='event_update'),
    path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
    path('dashboard/date_detail/', views.date_detail, name='date_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]
