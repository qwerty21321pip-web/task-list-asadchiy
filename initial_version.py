tasks = []

print("Список задач")
task = input("Введите задачу: ")
tasks.append(task)

print("\nВаши задачи:")
for task in tasks:
    print("-", task)
