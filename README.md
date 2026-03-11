# 📝 Gerenciador de Tarefas (To-Do List) com SQLite

Um sistema de linha de comando (CLI) simples e eficiente para gerenciar tarefas diárias, permitindo o armazenamento persistente de dados utilizando o banco de dados SQLite.

---

## 🚀 Funcionalidades

O projeto segue as operações básicas de **CRUD** (Create, Read, Update, Delete):

* **Criar Tarefa:** Adiciona novas tarefas com nome e status inicial.
* **Listar Tarefas:** Exibe todas as tarefas cadastradas diretamente do banco de dados.
* **Atualizar Status:** Permite alterar o estado de uma tarefa (Pendente, Em Andamento, Finalizada) via ID.
* **Remover Tarefa:** Exclui permanentemente um registro do sistema.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**: Linguagem principal.
* **SQLite3**: Banco de dados relacional leve e nativo do Python.



---

## 📋 Pré-requisitos

Não é necessário instalar bancos de dados externos ou bibliotecas adicionais, pois o SQLite e o módulo `sqlite3` já vêm integrados ao Python.

🔧 Como Executar o ProjetoClone o repositório: 
Bashgit clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
Navegue até a pasta do projeto:Bashcd nome-do-projeto
Inicie a aplicação:Bashpython nome_do_seu_arquivo.py
Nota: Certifique-se de que a tabela tarefas foi criada no arquivo todoLista.db antes da primeira inserção.

🗄️ Estrutura do Banco de DadosA tabela tarefas utiliza o seguinte esquema:CampoTipoDescriçãoidINTEGERChave primária com AUTOINCREMENT.
nomeTEXTDescrição ou título da tarefa.statusTEXTEstado atual (PENDENTE, EM ANDAMENTO, FINALIZADA).

📜 Exemplo de InteraçãoAo iniciar o programa, o menu interativo guiará o uso:PlaintextEscolha a opção desejada:
  c - Criar nova tarefa
  l - Listar as tarefas
  a - Atualizar a tarefa
  r - Remover a tarefa
  s - Sair

💡 Próximas Melhorias[ ] Implementar tratamento de erros para entradas inválidas (letras onde se espera números).
[ ] Adicionar uma coluna de "Data de Criação".
[ ] Criar uma interface gráfica simples com Tkinter.
[ ] Opção de exportar a lista para um arquivo .txt ou .csv.Desenvolvido com 🐍 e SQLite.


```bash
# Verifique se o Python está instalado
python --version
