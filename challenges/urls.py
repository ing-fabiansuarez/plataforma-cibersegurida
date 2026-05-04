from django.urls import path
from . import views

urlpatterns = [
    # Web UI - Instructor
    path('instructor/challenges/', views.instructor_challenge_list, name='instructor_challenge_list'),
    path('instructor/challenges/create/', views.challenge_create, name='challenge_create'),
    path('instructor/challenges/<uuid:pk>/', views.instructor_challenge_detail, name='instructor_challenge_detail'),
    path('instructor/challenges/<uuid:pk>/edit/', views.challenge_edit, name='challenge_edit'),
    path('instructor/challenges/<uuid:pk>/delete/', views.challenge_delete, name='challenge_delete'),
    
    # Badges - Instructor
    path('instructor/badges/', views.instructor_badge_list, name='instructor_badge_list'),
    path('instructor/badges/create/', views.badge_create, name='badge_create'),
    path('instructor/badges/<uuid:pk>/edit/', views.badge_edit, name='badge_edit'),
    path('instructor/badges/<uuid:pk>/delete/', views.badge_delete, name='badge_delete'),
    
    # Web UI - Student
    path('challenges/', views.student_challenge_list, name='student_challenge_list'),
    path('challenges/<uuid:pk>/', views.challenge_detail, name='challenge_detail'),
    
    # Scoreboard
    path('podio/', views.scoreboard, name='scoreboard'),

    # User Profile
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/<str:username>/', views.user_profile, name='user_profile_public'),
]
