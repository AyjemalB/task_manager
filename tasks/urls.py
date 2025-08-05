from django.urls import path
from .views import TaskCreateView, TaskListView, TaskDetailView, TaskStatsView

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('', TaskListView.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('stats/', TaskStatsView.as_view(), name='task-stats'),
]
