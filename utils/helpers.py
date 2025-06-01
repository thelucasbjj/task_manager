class Helpers:
    @staticmethod
    def validate_email(email: str) -> bool:
        """Проверяет, валиден ли email."""
        return '@' in email and '.' in email.split("@")[1]

    @staticmethod
    def validate_not_empty(text: str) -> bool:
        """Проверяет, что строка не пустая."""
        return len(text.strip()) > 0