from django.urls import path
from . import views

urlpatterns = [
    path ('', views.getRoutes),
    path ('user/', views.getUser),
    path ('reminders/', views.getReminder),
    path ('reminders/create/', views.createReminder),
    path ('reminders/<str:pk>/update/', views.updateReminder),
    path ('reminders/<str:pk>/delete/', views.deleteReminder),
    path ('user/<str:pk>/', views.getUserData),
    path ('user/create/', views.createReminder),
    path ('user/<str:pk>/update/', views.updateReminder),
]