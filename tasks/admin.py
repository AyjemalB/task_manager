from django.contrib import admin
from .models import Task, SubTask, Category


"""
hw_9: 2. Настройте отображение моделей в админке: 
В файле admin.py вашего приложения добавьте классы администратора 
для настройки отображения моделей Task, SubTask и Category.
"""
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')           # отображаемые поля в списке
    search_fields = ('title', 'description')         # поиск по этим полям
    ordering = ('-created_at',)                      # сортировка по умолчанию

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')
    ordering = ('name',)
