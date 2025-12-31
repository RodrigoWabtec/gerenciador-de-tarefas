from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, mensagem):
        pass


class ConsoleObserver(Observer):
    def update(self, mensagem):
        print(f"[NOTIFICAÇÃO] {mensagem}")


class EmailObserver(Observer):
    def update(self, mensagem):
        print(f"[EMAIL ENVIADO] {mensagem}")
