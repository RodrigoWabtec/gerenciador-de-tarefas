from task_manager import TaskManager
from observer import ConsoleObserver, EmailObserver

manager = TaskManager()

# Observers
manager.add_observer(ConsoleObserver())
manager.add_observer(EmailObserver())

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Alterar status")
    print("4 - Remover tarefa")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        status = input("Status (Disponível/Fazendo/Feita): ")
        manager.add_task(nome, descricao, status)

    elif opcao == "2":
        tarefas = manager.list_tasks()
        for t in tarefas:
            print(t)

    elif opcao == "3":
        task_id = int(input("ID da tarefa: "))
        status = input("Novo status: ")
        manager.update_status(task_id, status)

    elif opcao == "4":
        task_id = int(input("ID da tarefa: "))
        manager.remove_task(task_id)

    elif opcao == "0":
        break
