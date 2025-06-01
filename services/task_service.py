from models.task import Task
import json
from typing import List
class TaskService:
    @staticmethod
    def create_task(title: str, description: str, tags: list = None) -> Task:
        """Создаёт задачу с возможностью указания тегов."""
        return Task(title, description, tags=tags)

    @staticmethod
    def add_tag_to_task(task: Task, tag: str):
        """Добавляет тег к задаче."""
        task.add_tag(tag)

    @staticmethod
    def change_task_status(task: Task, new_status: str):
        """Меняет статус задачи"""
        task.update_status(new_status)

    @staticmethod
    def save_users_to_json(users: List['User'], filename: str = "data.json"):
        data = {
            "users": [
                {"name": user.name, "email": user.email}
                for user in users
            ]
        }
        with open(filename, "w") as f:
            json.dump(data, f)

    @staticmethod
    def load_users_from_json(filename: str = "data.json") -> List['User']:
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                return [User(user["name"], user["email"]) for user in data["users"]]
        except FileNotFoundError:
            return []

    @staticmethod
    def filter_tasks_by_status(tasks: List[Task], status: str) -> List[Task]:
        return [task for task in tasks if task.status == status]

    @staticmethod
    def filter_by_status(tasks:list, status: str) -> list:
        """Фильтрует задачи по статусу."""
        return [task for task in tasks if task.status == status]

    @staticmethod
    def filter_by_tag(tasks: list, tag: str) -> list:
        """Фильтрует задачи по тегу."""
        return [task for task in tasks if tag in task.tags]

    @staticmethod
    def search_by_title(tasks: list, keyword: str) -> list:
        """Ищет задачи по ключевому слову в названии."""
        return [task for task in tasks if keyword.lower() in task.title.lower()]

    @staticmethod
    def save_to_json(tasks: list, filename: str = 'tasks.json'):
        data = [{"title": t.title, "description": t.description, 'status': t.status}
                for t in tasks ]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_from_json(filename: str = 'tasks.json') -> list:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return [Task(t["title"], t["description"], t["status"]) for t in data]
        except FileNotFoundError:
            return []

    @staticmethod
    def delete_task(tasks: list, task_title: str) -> bool:
        """Удаляет задачу по названию. Возвращает True, если удаление прошло успешно."""
        for i, task in enumerate(tasks):
            if task.title == task_title:
                tasks.pop(i)
                return True
            return False