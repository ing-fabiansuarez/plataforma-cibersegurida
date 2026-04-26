from django.urls import path
from . import views

urlpatterns = [
    # Web UI - Instructor
    path('instructor/challenges/', views.instructor_challenge_list, name='instructor_challenge_list'),
    path('instructor/challenges/create/', views.challenge_create, name='challenge_create'),
    path('instructor/challenges/<uuid:pk>/', views.instructor_challenge_detail, name='instructor_challenge_detail'),
    path('instructor/challenges/<uuid:pk>/edit/', views.challenge_edit, name='challenge_edit'),
    path('instructor/challenges/<uuid:pk>/delete/', views.challenge_delete, name='challenge_delete'),
    
    # Web UI - Student
    path('challenges/', views.student_challenge_list, name='student_challenge_list'),
    path('challenges/<uuid:pk>/', views.challenge_detail, name='challenge_detail'),
]
