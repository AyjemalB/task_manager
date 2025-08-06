from rest_framework import serializers
from datetime import datetime
from .models import Task
from .models import SubTask
from .models import Category

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline']


""" hw_13_1
Задание 1: Переопределение полей сериализатора
Создайте SubTaskCreateSerializer, в котором поле created_at будет доступно только для чтения (read_only).
Шаги для выполнения:
Определите SubTaskCreateSerializer в файле serializers.py.
Переопределите поле created_at как read_only.
"""
class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'
        read_only_fields = ['created_at']  # поле будет доступно только для чтения

""" hw_13_2
Задание 2: Переопределение методов create и update
Создайте сериализатор для категории CategoryCreateSerializer, переопределив методы create и 
update для проверки уникальности названия категории. Если категория с таким названием уже существует, возвращайте ошибку валидации.
Шаги для выполнения:
Определите CategoryCreateSerializer в файле serializers.py.
Переопределите метод create для проверки уникальности названия категории.
Переопределите метод update для аналогичной проверки при обновлении.
"""
class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_title(self, value):
        """
        Проверка уникальности названия категории.
        """
        # При создании: если уже есть категория с таким названием
        if self.instance is None and Category.objects.filter(title=value).exists():
            raise serializers.ValidationError("Категория с таким названием уже существует.")

        # При обновлении: исключаем текущую категорию из проверки
        if self.instance is not None and Category.objects.filter(title=value).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError("Категория с таким названием уже существует.")

        return value

    def create(self, validated_data):
        # validate_title будет вызван автоматически
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # validate_title будет вызван автоматически
        return super().update(instance, validated_data)


""" hw_13_3
Задание 3: Использование вложенных сериализаторов
Создайте сериализатор для TaskDetailSerializer, который включает вложенный сериализатор для полного 
отображения связанных подзадач (SubTask). Сериализатор должен показывать все подзадачи, связанные с данной задачей.
Шаги для выполнения:
Определите TaskDetailSerializer в файле serializers.py.
Вложите SubTaskSerializer внутрь TaskDetailSerializer.
"""
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'title', 'status', 'created_at', 'deadline']

class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline', 'subtasks']

"""
Задание 4: Валидация данных в сериализаторах
Создайте TaskCreateSerializer и добавьте валидацию для поля deadline, чтобы дата 
не могла быть в прошлом. Если дата в прошлом, возвращайте ошибку валидации.
Шаги для выполнения:
Определите TaskCreateSerializer в файле serializers.py.
Переопределите метод validate_deadline для проверки даты.
"""
class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_deadline(self, value):
        if value < datetime.now():
            raise serializers.ValidationError("Срок выполнения не может быть в прошлом.")
        return value