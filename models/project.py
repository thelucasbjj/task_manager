from typing import List
from models.task import Task

class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Добавляет задачу в проект"""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Возвращает список задач"""
        return self.tasks

    def __str__(self):
        return f"Project: {self.name} ({len(self.tasks)} tasks)"
