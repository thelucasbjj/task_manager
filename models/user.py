from typing import List
from models.task import Task

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.tasks: List[Task] = []

    def asssign_task(self, task: Task):
        """Назначает задачу пользователю"""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Возвращает список задач"""
        return self.tasks

    def __str__(self):
        return f'User: {self.name} ({self.email})'


