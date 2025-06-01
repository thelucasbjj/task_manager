class Logger:
    @staticmethod
    def log(message: str):
        """Печатает сообщение с префиксом [LOG]."""
        print(f'[LOG] {message}')
