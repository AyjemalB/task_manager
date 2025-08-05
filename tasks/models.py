from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    # ---------------- hw_9 задание -----------------------------------------------------------------------#
    #Добавить метод str, который возвращает название категории.
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task_manager_category'  # имя таблицы в базе данных
        verbose_name = 'Category'  # человекочитаемое имя модели
    #----------------------------------------------------------------------------------------------------#

class Task(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('IN_PROGRESS', 'In progress'),
        ('PENDING', 'Pending'),
        ('BLOCKED', 'Blocked'),
        ('DONE', 'Done'),
    ]

    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='NEW')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    #---------------- hw_9 задание -----------------------------------------------------------------------#
    #Добавить метод str, который возвращает название задачи.
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_task'  # имя таблицы в базе данных
        ordering = ['-created_at']  # сортировка по убыванию даты создания
        verbose_name = 'Task'  # человекочитаемое имя модели
    #-----------------------------------------------------------------------------------------------------#

# ----- hw_10 ---------------------------------------------------------------#

class SubTask(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    status = models.CharField(max_length=15, choices=Task.STATUS_CHOICES, default='NEW')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    # ---------------- hw_9 задание -----------------------------------------------------------------------#
    # Добавить метод str, который возвращает название подзадачи.
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_subtask'  # имя таблицы в базе данных
        ordering = ['-created_at']  # сортировка по убыванию даты создания
        verbose_name = 'SubTask'  # человекочитаемое имя модели
    # -------------------------------------------------------------------------------------------------------#