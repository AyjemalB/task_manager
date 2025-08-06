from fastapi import APIRouter, Query
from typing import List, Optional
from tasks.schemas import TaskSchema
from tasks.models import Task
from tasks.models import SubTask
from tasks.schemas import SubTaskSchema

router = APIRouter()


""" hw_14_1
Задание 1:
Написать, или обновить, если уже есть, эндпоинт на получение списка всех задач по дню недели.
Если никакой параметр запроса не передавался - по умолчанию выводить все записи.
Если был передан день недели (например вторник) - выводить список задач только на этот день недели.
"""
def get_weekday_number(day_name: str) -> int:
    days = {
        "понедельник": 2,
        "вторник": 3,
        "среда": 4,
        "четверг": 5,
        "пятница": 6,
        "суббота": 7,
        "воскресенье": 1,
    }
    return days.get(day_name.lower(), 0)



@router.get("/tasks", response_model=List[TaskSchema])
def get_tasks(day: Optional[str] = Query(None)):
    if day:
        queryset = Task.objects.filter(deadline__week_day=get_weekday_number(day))
    else:
        queryset = Task.objects.all()
    return list(queryset)


""" hw_14_2
Задание 2:
Добавить пагинацию в отображение списка подзадач. На одну страницу должно отображаться не более 5 объектов. 
Отображение объектов должно идти в порядке убывания даты (от самого последнего добавленного объекта к самому первому)
"""
# @router.get("/subtasks", response_model=List[SubTaskSchema])
# def get_subtasks(limit: int = Query(5, ge=1), offset: int = Query(0, ge=0)):
#     queryset = SubTask.objects.all().order_by('-created_at')[offset:offset + limit]
#     return list(queryset)



""" hw_14_3
Задание 3:
Добавить или обновить, если уже есть, эндпоинт на получение списка всех подзадач по названию главной задачи и статусу подзадач.
Если фильтр параметры в запросе не передавались - выводить данные по умолчанию, с учётом пагинации.
Если бы передан фильтр параметр названия главной задачи - выводить данные по этой главной задаче.
Если был передан фильтр параметр конкретного статуса подзадачи - выводить данные по этому статусу.
Если были переданы оба фильтра - выводить данные в соответствии с этими фильтрами.
"""
@router.get("/subtasks", response_model=List[SubTaskSchema])
def get_subtasks(
    task_title: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    limit: int = Query(5, ge=1),
    offset: int = Query(0, ge=0)
):
    queryset = SubTask.objects.select_related('task').all()

    if task_title:
        queryset = queryset.filter(task__title__icontains=task_title)

    if status:
        queryset = queryset.filter(status=status)

    queryset = queryset.order_by('-created_at')[offset:offset + limit]
    return list(queryset)