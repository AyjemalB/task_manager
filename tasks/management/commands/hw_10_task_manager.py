from django.core.management.base import BaseCommand
from tasks.models import Task, SubTask
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Домашнее задание: CRUD операции для Менеджера задач'

    def handle(self, *args, **kwargs):
        # --- Создание записей ---
        print("Создание задачи и подзадач...")
        task, created = Task.objects.get_or_create(
            title="Prepare presentation",
            defaults={
                'description': "Prepare materials and slides for the presentation",
                'status': "NEW",
                'deadline': datetime.now() + timedelta(days=3)
            }
        )

        if created:
            SubTask.objects.create(
                title="Gather information",
                description="Find necessary information for the presentation",
                status="NEW",
                deadline=datetime.now() + timedelta(days=2),
                task=task
            )
            SubTask.objects.create(
                title="Create slides",
                description="Create presentation slides",
                status="NEW",
                deadline=datetime.now() + timedelta(days=1),
                task=task
            )
            print("Задача и подзадачи созданы.")
        else:
            print("Задача уже существует.")

        # --- Чтение записей ---
        print("Задачи со статусом 'New':")
        for t in Task.objects.filter(status='NEW'):
            print(f"- {t.title}")

        print("Просроченные подзадачи со статусом 'Done':")
        for st in SubTask.objects.filter(status='DONE', deadline__lt=datetime.now()):
            print(f"- {st.title} (Deadline: {st.deadline})")

        # --- Изменение записей ---
        print("Обновление записей...")
        task.status = 'IN_PROGRESS'
        task.save()

        SubTask.objects.filter(title="Gather information").update(
            deadline=datetime.now() - timedelta(days=2)
        )

        SubTask.objects.filter(title="Create slides").update(
            description="Create and format presentation slides"
        )
        print("Записи обновлены.")

        # --- Удаление записей ---
        print("Удаление задачи и связанных подзадач...")
        task.delete()
        print("Задача 'Prepare presentation' и её подзадачи удалены.")
