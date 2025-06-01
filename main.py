from models.task import Task
from models.user import User
from models.project import Project
from services.task_service import TaskService
from services.user_service import UserService
from utils.logger import Logger

def main():
    # 1. Создаем пользователя
    user = UserService.create_user("Alice", "alice@example.com")
    Logger.log(f'Created user: {user}')

    # 2. Создаем задачу
    task = TaskService.create_task("Fix bug", "Critical bug in login page")
    Logger.log(f"Created task: {task}")

    # 3. Назначаем задачу пользователю
    UserService.assign_task_to_user(user, task)
    Logger.log(f'Assigned task to user. User tasks: {len(user.get_tasks())}')

    # 4. Меняем статус задачи
    TaskService.change_task_status(task, 'In Progress')
    Logger.log(f'Task status updated: {task}')

    # 5. Создаем проект и добавляем задачу
    project = Project("Wed App")
    project.add_task(task)
    Logger.log(f'Project: {project}')

if __name__ == "__main__":
    main()