from services.task_service import TaskService
from services.user_service import UserService
from models.project import Project
from utils.logger import Logger
from utils.helpers import Helpers
from colorama import Fore, Style, init
init()

class CLI:
    def __init__(self):
        self.project = Project('My Project')
        self.current_user = None
        self.users = UserService.load_users_from_json()
        self.project.tasks = TaskService.load_from_json()
    def start(self):
        while True:
            print(f"\n{Fore.CYAN}=== Task Manager ==={Style.RESET_ALL}")
            print(f"{Fore.YELLOW}1.{Style.RESET_ALL} Создать пользователя")
            print(f"{Fore.YELLOW}2.{Style.RESET_ALL} Создать задачу")
            print(f"{Fore.YELLOW}3.{Style.RESET_ALL} Показать все задачи")
            print(f"{Fore.YELLOW}4.{Style.RESET_ALL} Поиск задач")
            print(f"{Fore.YELLOW}5.{Style.RESET_ALL} Выход")

            choice = input(f"{Fore.GREEN}Выберите действие:{Style.RESET_ALL} ").strip()

            if choice == '1':
                self.create_user()
            if choice == '2':
                self.create_task()
            if choice == '3':
                self.show_task()
            if choice == '4':
                self.search_task()
            elif choice == "5":
                TaskService.save_to_json(self.project.tasks)
                print('Данные сохранены. Выход')
                break
            elif choice == '6':
                title = input("Введите название задачи для удаления: ")
                if TaskService.delete_task(self.project.tasks, title):
                    print("Задача удалена!")
                else:
                    print("Задача не найдена!")

    def search_task(self):
        print("\n=== Поиск задач ===")
        print("1. По статусу")
        print("2. По тегу")
        print("3. По названию")
        search_choice = input("Выберите тип поиска: ")

        if search_choice == "1":
            status = input("Введите статус (To Do/In Progress/Done): ")
            tasks = TaskService.filter_by_status(self.project.get_tasks(), status)
        elif search_choice == "2":
            tag = input("Введите тег: ")
            tasks = TaskService.filter_by_tag(self.project.get_tasks(), tag)
        elif search_choice == "3":
            keyword = input("Введите ключевое слово: ")
            tasks = TaskService.search_by_title(self.project.get_tasks(), keyword)
        else:
            print("Неверный ввод!")
            return

        print("\nРезультаты поиска:")
        for task in tasks:
            print(f"- {task}")


    def create_user(self):
        while True:
            name = input("Введите имя: ")
            if Helpers.validate_not_empty(name):
                break
            print("Имя не может быть пустым!")

        while True:
            email = input("Введите email: ")
            if Helpers.validate_email(email):
                break
            print("Некорректный email!")

        self.current_user = UserService.create_user(name, email)
        Logger.log(f"Создан пользователь: {self.current_user}")


    def create_task(self):
        if not self.current_user:
            print("Сначала создайте пользователя!")
            return

        title = input("Введите название задачи: ")
        description = input("Введите описание: ")
        task = TaskService.create_task(title, description)
        self.project.add_task(task)
        UserService.assign_task_to_user(self.current_user, task)
        Logger.log(f"Задача создана: {task}")

        while True:
            tag = input("Добавить тег (или Enter чтобы пропустить): ")
            if not tag:
                break
            TaskService.add_tag_to_task(task, tag)

    def show_task(self):
        if not self.project.get_tasks():
            print("Нет задач")
            return

        print("\nСписок задач: ")
        for task in self.project.get_tasks():
            print(f"- {task}")


    def exit(self):
        UserService.save_users_to_json(self.users)
        TaskService.save_users_to_json(self.project.get_tasks())
        print("Данные сохранены. Выход ...")
        exit()

if __name__ == "__main__":
    CLI().start()
