from typing import List
class Task:
    def __init__(self, title: str, description: str, status: str = 'To Do', tags: List[str] = None):
        self.title = title
        self.description = description
        self.status = status #Варианты "To Do", "In Progress", "Done"
        self.tags = tags or []

    def add_tag(self, tag: str):
        """Добавляем тег к задаче."""
        if tag not in self.tags:
            self.tags.append(tag)

    def update_status(self, new_status: str):
        """Меняет статус задачи"""
        self.status = new_status

    def __str__(self):
        """Возвращает информауию о задаче и виде строки"""
        tags_str = ", ".join(self.tags) if self.tags else "нет тегов"
        return f'{self.title} [{self.status}], теги: {tags_str}\n Описание: {self.description}'
