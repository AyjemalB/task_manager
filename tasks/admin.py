from django.contrib import admin
from .models import Task, SubTask, Category


"""
hw_9: 2. Настройте отображение моделей в админке: 
В файле admin.py вашего приложения добавьте классы администратора 
для настройки отображения моделей Task, SubTask и Category.
"""
# +++
"""
hw_11
"""
# Инлайн для отображения подзадач внутри задачи
class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1
    fields = ('title', 'description', 'status', 'deadline')

# Админ-класс для Task с инлайном SubTask
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')           # отображаемые поля в списке
    search_fields = ('title', 'description')         # поиск по этим полям
    ordering = ('-created_at',)                      # сортировка по умолчанию
    #---------------------------------------------------------------------------------------------#
    inlines = [SubTaskInline]

    def short_title(self, obj):
        return obj.title[:10] + '...' if len(obj.title) > 10 else obj.title

    short_title.short_description = 'Название задачи'
    # ---------------------------------------------------------------------------------------------#

# Админ-класс для SubTask
@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    actions = ['mark_as_done']

    @admin.action(description='Отметить как Done')
    def mark_as_done(self, request, queryset):
        updated = queryset.update(status='DONE')
        self.message_user(request, f'{updated} подзадач переведены в статус DONE.')

# Админ-класс для Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')
    ordering = ('name',)




