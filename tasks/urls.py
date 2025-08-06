from django.urls import path
from .views import TaskCreateView, TaskDetailView, TaskStatsView, TaskListCreateView #TaskListView
from .views import SubTaskListCreateView, SubTaskDetailView #SubTaskDetailUpdateDeleteView

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='task-create'),
    # path('', TaskListView.as_view(), name='task-list'),
    # path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('stats/', TaskStatsView.as_view(), name='task-stats'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    #path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
    path('subtasks/<int:pk>/', SubTaskDetailView.as_view(), name='subtask-detail'),
]

