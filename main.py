# Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def add_task(tasks, description, deadline):
        task = Task(description, deadline)
        tasks.append(task)

    def get_pending_tasks(tasks):
        return [task for task in tasks if not task.is_completed]

    def show_tasks(tasks):
        for task in tasks:
            status = "Выполнено" if task.is_completed else "Не выполнено"
            print(f"Задача: {task.description}, Срок: {task.deadline}, Статус: {status}")

# Пример использования
tasks = []

# Добавляем задачи
Task.add_task(tasks, "Купить продукты", "2024-08-01")
Task.add_task(tasks, "Закончить проект", "2024-08-15")

# Выводим все задачи
print("Все задачи:")
Task.show_tasks(tasks)

# Отмечаем первую задачу как выполненную
tasks[0].mark_completed()

# Выводим все задачи
print("Все задачи:")
Task.show_tasks(tasks)

# Выводим список невыполненных задач
print("\nНевыполненные задачи:")
pending_tasks = Task.get_pending_tasks(tasks)
Task.show_tasks(pending_tasks)
