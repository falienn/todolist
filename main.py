import json
import os


def menu():
    print("1. Додати задачу")
    print("2. Позначити задачу як виконану")
    print("3. Видалити задачу")
    print("4. Показати список задач")
    print("5. Вийти")


def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print("Задача додана.")


def mark_as_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        save_tasks(tasks)
        print("Задачу позначено як виконану.")
    else:
        print("Неправильний індекс задачі.")


def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Задачу '{deleted_task['task']}' видалено.")
    else:
        print("Неправильний індекс задачі.")


def show_tasks(tasks):
    if tasks:
        print("Список задач:")
        for index, task in enumerate(tasks):
            status = "[Done]" if task['done'] else "[Pending]"
            print(f"{index + 1}. {status} {task['task']}")
    else:
        print("Список задач порожній.")


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)


def load_tasks():
    tasks = []
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    return tasks


def main():
    tasks = load_tasks()

    while True:
        menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            task_text = input("Введіть нову задачу: ")
            new_task = {'task': task_text, 'done': False}
            add_task(tasks, new_task)
        elif choice == "2":
            index = int(input("Введіть індекс виконаної задачі: ")) - 1
            mark_as_done(tasks, index)
        elif choice == "3":
            index = int(input("Введіть індекс задачі для видалення: ")) - 1
            delete_task(tasks, index)
        elif choice == "4":
            show_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Дякую за використання To-Do List. До побачення!")
            break
        else:
            print("Неправильний вибір. Будь ласка, виберіть вірну опцію.")


if __name__ == "__main__":
    main()
