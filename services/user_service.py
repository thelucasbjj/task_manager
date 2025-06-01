from models.user import User
import json
from typing import List

class UserService:
    @staticmethod
    def create_user(name: str, email: str) -> User:
        """Создает нового пользователя"""
        return User(name, email)

    @staticmethod
    def assign_task_to_user(user: User, task):
        """Назначает задачу пользователю"""
        user.asssign_task(task)

    @staticmethod
    def save_users_to_json(users: List["User"], filename: str = "data.json"):
        data = {
            "user": [
                {"name": user.name, "email": user.email}
                for user in users
            ]
        }
        with open(filename, "w") as f:
            json.dump(data, f)

    @staticmethod
    def load_users_from_json(filename: str = 'data.json') -> List['User']:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return [User(user["name"], user["email"]) for user in data["users"]]
        except FileNotFoundError:
            return []