from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.applications, name = 'applications'),
    path('leave-request/', views.leave_request, name = 'leave_request'),
    path('leave-request/approve/<int:pk>', views.approve, name = 'approve_request'),
    path('leave-request/decline/<int:pk>', views.decline, name = 'decline_request'),
]
