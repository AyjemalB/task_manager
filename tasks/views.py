from rest_framework import generics, filters
from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from .models import SubTask
from .serializers import SubTaskSerializer, SubTaskCreateSerializer
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


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
# class TaskListView(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['-created_at']  # по умолчанию — от новых к старым

# # Получение одной задачи по ID
# class TaskDetailView(generics.RetrieveAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
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


""" hw_13_5
Задание 5: Создание классов представлений
Создайте классы представлений для работы с подзадачами (SubTasks), включая создание, 
получение, обновление и удаление подзадач. Используйте классы представлений (APIView) для реализации этого функционала.
Шаги для выполнения:
Создайте классы представлений для создания и получения списка подзадач (SubTaskListCreateView).
Создайте классы представлений для получения, обновления и удаления подзадач (SubTaskDetailUpdateDeleteView).
Добавьте маршруты в файле urls.py, чтобы использовать эти классы.
"""
# #Список и создание подзадач
# class SubTaskListCreateView(APIView):
#     def get(self, request):
#         subtasks = SubTask.objects.all()
#         serializer = SubTaskSerializer(subtasks, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = SubTaskCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# #Получение, обновление и удаление одной подзадачи
# class SubTaskDetailUpdateDeleteView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(SubTask, pk=pk)
#
#     def get(self, request, pk):
#         subtask = self.get_object(pk)
#         serializer = SubTaskSerializer(subtask)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         subtask = self.get_object(pk)
#         serializer = SubTaskCreateSerializer(subtask, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         subtask = self.get_object(pk)
#         subtask.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#-----------------------------------------------------------------------------------------------------------------#
""" hw_15_2
Задание 2: Замена представлений для подзадач (SubTasks) на Generic Views
Шаги для выполнения:
Замените классы представлений для подзадач на Generic Views:
Используйте ListCreateAPIView для создания и получения списка подзадач.
Используйте RetrieveUpdateDestroyAPIView для получения, обновления и удаления подзадач.
Реализуйте фильтрацию, поиск и сортировку:
Реализуйте фильтрацию по полям status и deadline.
Реализуйте поиск по полям title и description.
Добавьте сортировку по полю created_at.
"""
#Представление для списка и создания подзадач
class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['created_at']  # по умолчанию сортировка

#Представление для получения, обновления и удаления подзадачи
class SubTaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
