from pydantic import BaseModel
from datetime import datetime
from typing import List

class CategorySchema(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True

class TaskSchema(BaseModel):
    title: str
    description: str
    status: str
    deadline: datetime
    created_at: datetime
    categories: List[CategorySchema] = []

    class Config:
        orm_mode = True

#Создай Pydantic-схему для подзадачи
class SubTaskSchema(BaseModel):
    title: str
    description: str
    status: str
    deadline: datetime
    created_at: datetime

    class Config:
        orm_mode = True
