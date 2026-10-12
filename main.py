def show_menu():
    print("\n=== Список задач ===")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Удалить задачу")
    print("4. Выход")


def add_task(tasks):
    text = input("Введите текст задачи: ").strip()
    if text:
        tasks.append(text)
        print("Задача добавлена.")
    else:
        print("Пустую задачу добавить нельзя.")


def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
        return

    print("\nВаши задачи:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        number = int(input("Введите номер задачи для удаления: "))
    except ValueError:
        print("Введите целое число.")
        return

    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        print(f"Задача удалена: {removed}")
    else:
        print("Задачи с таким номером нет.")


def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Выберите пункт меню (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный пункт. Выберите число от 1 до 4.")


if __name__ == "__main__":
    main()
