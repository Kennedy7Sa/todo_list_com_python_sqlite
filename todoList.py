import sqlite3 

def conexao():
    banco = sqlite3.connect('todoLista.db')
    cursor = banco.cursor()
    return banco,cursor

def criarTarefa(dicionario):
    try:
        banco,cursor = conexao()
        cursor.execute('insert into tarefas (nome,status)values (?,?)',(dicionario['nome'],dicionario['status']))
        banco.commit()
        print(f'Tarefa {dicionario['nome']} salva com sucesso ! ')
        banco.close()
    except sqlite3.Error as erro:
        print(erro)

def listarTarefas():
    banco,cursor = conexao()
    tarefas = cursor.execute('select * from tarefas')
    for t in tarefas:
        print(f'ID: {t[0]} Nome da tarefa: {t[1]} status: {t[2]}')

def atualizarTarefa():
    banco,cursor = conexao()

    id = input('Digite o id da tarefa que será atualizada o status')
    tarefa = cursor.execute('select id from tarefas where id=?',(id)).fetchone()

    if tarefa is None:
        print('Tarefa não encontrada com esse id')
        return
    
    
    status = input('digite 1 para PENDENTE , 2 para EM ANDAMENTO , 3 para FINALIZADA: ')
    if int(status) == 1:
            status='PENDENTE'
    elif int(status)==2:
            status='EM ANDAMENTO'
    else:
        status='FINALIZADA'
        
        

    cursor.execute('update tarefas set status = ? where id = ?',(status,id))
    banco.commit()
    print(f'tarefa de id {tarefa} atualizada!')    
   
    banco.close()
    return  

def excluirTarefa(id):
    banco,cursor = conexao()

    cursor.execute('delete from tarefas where id = ? ',(id))
    banco.commit()
    print(f' Tarefa com id {id} foi excluida com sucesso')
    banco.close()





banco,cursor = conexao()

#cursor.execute('Create table tarefas(id integer primary key autoincrement, nome text ,status)')

opcao = input('''Escolha a opção desejada
                c - criar nova tarefa
                l - para listar as tarefas
                a - para atualizar a tarefa
                r - para remover a tarefa
                s - para sair
              ''').lower()

while opcao!='s':
    if opcao=='c':
        nome = input('Digite o nome da tarefa ')
        status = input('digite 1 para PENDENTE , 2 para EM ANDAMENTO , 3 para FINALIZADA ')
        if int(status) == 1:
            status='PENDENTE'
        elif int(status)==2:
            status='EM ANDAMENTO'
        else:
            status='FINALIZADA'
        tarefa = {'nome':nome , 'status':status}
        criarTarefa(tarefa)
    if opcao == 'l':
        print('***Lista de tarefas ***\n')
        listarTarefas()
        print('*****************************')
    if opcao == 'a':
        print('*****************************')
        listarTarefas()    
        print('*****************************')    
        atualizarTarefa()
        tarefa = atualizarTarefa()
        print(tarefa)
    
    if opcao == 'r':
        print('*****************************')
        listarTarefas()
        print('*****************************')
        id = input('Digite o id da tarefa a ser excluida ')
        excluirTarefa(id)



        

    opcao = input('''Escolha a opção desejada
                    c - criar nova tarefa
                    l - para listar as tarefas
                    a - para atualizar a tarefa
                    r - para remover a tarefa
                    s - para sair
                ''').lower()