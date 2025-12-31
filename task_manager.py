import sqlite3
from task import Task

class TaskManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
            cls._instance._observers = []
            cls._instance._init_db()
        return cls._instance

    def _init_db(self):
        self.conn = sqlite3.connect("tasks.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                descricao TEXT,
                status TEXT
            )
        """)
        self.conn.commit()

    # Observer methods
    def add_observer(self, observer):
        self._observers.append(observer)

    def notify(self, mensagem):
        for observer in self._observers:
            observer.update(mensagem)

    # Funcionalidades
    def add_task(self, nome, descricao, status):
        self.cursor.execute(
            "INSERT INTO tasks (nome, descricao, status) VALUES (?, ?, ?)",
            (nome, descricao, status)
        )
        self.conn.commit()

    def list_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        return self.cursor.fetchall()

    def update_status(self, task_id, new_status):
        self.cursor.execute(
            "UPDATE tasks SET status=? WHERE id=?",
            (new_status, task_id)
        )
        self.conn.commit()
        self.notify(f"Tarefa {task_id} alterada para status '{new_status}'")

    def remove_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        self.conn.commit()
