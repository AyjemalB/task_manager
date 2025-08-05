from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

"""
Задание 1: Эндпоинт для создания задачи
Создайте эндпоинт для создания новой задачи. Задача должна быть создана с полями title, description, status, и deadline.
Шаги для выполнения:
Определите сериализатор для модели Task.
Создайте представление для создания задачи.
Создайте маршрут для обращения к представлению.
"""
class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

"""
Задание 2: Эндпоинты для получения списка задач и конкретной задачи по её ID
Создайте два новых эндпоинта для:
Получения списка задач
Получения конкретной задачи по её уникальному ID
Шаги для выполнения:
Создайте представления для получения списка задач и конкретной задачи.
Создайте маршруты для обращения к представлениям.
"""
# Получение списка всех задач
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Получение одной задачи по ID
class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

"""
Задание 3: Агрегирующий эндпоинт для статистики задач
Создайте эндпоинт для получения статистики задач, таких как общее количество задач, количество задач по каждому статусу и количество просроченных задач.
Шаги для выполнения:
Определите представление для агрегирования данных о задачах.
Создайте маршрут для обращения к представлению.
"""
class TaskStatsView(APIView):
    def get(self, request):
        now = timezone.now()

        total_tasks = Task.objects.count()
        pending_tasks = Task.objects.filter(status='pending').count()
        in_progress_tasks = Task.objects.filter(status='in_progress').count()
        completed_tasks = Task.objects.filter(status='completed').count()
        overdue_tasks = Task.objects.filter(deadline__lt=now).exclude(status='completed').count()

        data = {
            "total_tasks": total_tasks,
            "pending": pending_tasks,
            "in_progress": in_progress_tasks,
            "completed": completed_tasks,
            "overdue": overdue_tasks
        }

        return Response(data)