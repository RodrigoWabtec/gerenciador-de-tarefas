# 📋 Lista de Tarefas (Console)

## 📌 Descrição do Projeto
Este projeto consiste no desenvolvimento de um **aplicativo de Lista de Tarefas em modo console**, no qual o usuário pode cadastrar, listar, remover e alterar o status de tarefas.  

O objetivo principal do projeto é aplicar **padrões de projeto (Design Patterns)** estudados em sala de aula, utilizando uma aplicação simples, porém bem estruturada.

O sistema foi desenvolvido em **Python**, com persistência de dados utilizando **SQLite**.

---

## ⚙️ Funcionalidades Implementadas

### 1️⃣ Adicionar Tarefa
- Permite cadastrar uma tarefa informando:
  - Nome
  - Descrição
  - Status
- Status disponíveis:
  - **Disponível**
  - **Fazendo**
  - **Feita**
- As tarefas são armazenadas em um banco de dados SQLite.

---

### 2️⃣ Listar Tarefas
- Exibe todas as tarefas cadastradas.
- Mostra:
  - ID
  - Nome
  - Descrição
  - Status atual

---

### 3️⃣ Remover Tarefa
- Permite remover uma tarefa informando seu ID.
- A tarefa é excluída do banco de dados.

---

### 4️⃣ Alterar Status da Tarefa
- Permite alterar o status de uma tarefa selecionada.
- Ao alterar o status, o sistema dispara notificações automaticamente.

---

## 🗄️ Armazenamento de Dados
- O sistema utiliza **SQLite** como banco de dados local.
- O banco de dados é criado automaticamente na primeira execução.
- Todas as operações de cadastro, listagem, atualização e remoção são persistidas.

---

## 🧩 Padrões de Projeto Utilizados

### 🔹 Singleton

#### 📌 Onde foi aplicado?
- Classe **TaskManager** (Gerenciador de Tarefas)

#### 📌 Como foi aplicado?
- O padrão Singleton garante que exista **apenas uma instância** do gerenciador de tarefas durante toda a execução da aplicação.
- Essa instância é responsável por:
  - Gerenciar a lista de tarefas
  - Controlar a conexão com o banco de dados
  - Centralizar as regras do sistema

#### 📌 Benefícios
- Evita múltiplas instâncias do gerenciador.
- Garante consistência dos dados.
- Facilita o controle do sistema.

---

### 🔹 Observer

#### 📌 Onde foi aplicado?
- No processo de **alteração do status das tarefas**.

#### 📌 Como foi aplicado?
- O **TaskManager** atua como o **Subject**.
- Observadores são registrados para receber notificações quando ocorre uma mudança.
- Foram implementados dois tipos de observers:
  - **ConsoleObserver**: exibe mensagens no console.
  - **EmailObserver (simulado)**: simula o envio de e-mail através de mensagens no console.

#### 📌 Exemplo prático
Quando o status de uma tarefa é alterado:
- Todos os observers registrados são notificados automaticamente.
- Cada observer executa sua ação de forma independente.

#### 📌 Benefícios
- Reduz acoplamento entre as classes.
- Facilita a adição de novas notificações no futuro.
- Segue boas práticas de design orientado a objetos.

---

## ▶️ Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado.
2. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
3. Execute o programa:
   ```bash
    python main.py
4. Utilize o menu apresentado no console para interagir com o sistema.
