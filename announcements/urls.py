from django.urls import path
from .views import AnnouncementListView, AnnouncementCreateView, toggle_read, toggle_reaction, add_comment

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcements_list'),
    path('create/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('<int:pk>/read/', toggle_read, name='announcement_toggle_read'),
    path('<int:pk>/react/', toggle_reaction, name='announcement_toggle_reaction'),
    path('<int:pk>/comment/', add_comment, name='announcement_add_comment'),
]
