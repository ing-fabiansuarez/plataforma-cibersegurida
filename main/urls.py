from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('narrativas/', views.NarrativasListView.as_view(), name='narrativas_list'),
    path('narrativas/narrativa-1/', views.NarrativaUnoView.as_view(), name='narrativa_1'),
    path('narrativas/narrativa-2/', views.NarrativaDosView.as_view(), name='narrativa_2'),
    path('narrativas/narrativa-3/', views.NarrativaTresView.as_view(), name='narrativa_3'),
    path('narrativas/narrativa-4/', views.NarrativaCuatroView.as_view(), name='narrativa_4'),
]
