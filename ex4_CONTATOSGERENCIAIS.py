"""
QUESTÃO 4

Enunciado: Você e sua equipe de programadores foram contratados por uma pequena empresa para desenvolver um software de gerenciamento de Contatos Comerciais. Este software deve ter o seguinte menu e opções:

Cadastrar Contato
Consultar Contato
Consultar Todos 
Consultar por Id
Consultar por Atividade
Retornar ao menu
Remover Contato
Encerrar Programa

Elabore um programa em Python que: 
Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui). 
Por exemplo: print(“Bem vindos a lista de contatos do Bruno Kostiuk”)  [EXIGÊNCIA DE CÓDIGO 1 de 8];
Deve-se implementar uma lista com o nome de lista_contatos e a variável id_global com valor inicial igual ao número de seu RU [EXIGÊNCIA DE CÓDIGO 2 de 8];
Deve-se implementar uma função chamada cadastrar_contato(id) que recebe apenas id como parâmetro e que: [EXIGÊNCIA DE CÓDIGO 3 de 8];
Pergunta nome, atividade, telefone do contato;
Armazena o id (este é fornecido via parâmetro da função), nome, atividade, telefone dentro de um dicionário;
Copiar o dicionário para dentro da lista_contatos (utilizar o copy);
Deve-se implementar uma função chamada consultar_contatos() que não recebe parâmetros e que: [EXIGÊNCIA DE CÓDIGO 4 de 8];
Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu):
Se Consultar Todos, apresentar todos os contatos com todos os seus dados cadastrados;
Se Consultar por Id, solicitar ao usuário que informe um id, e apresentar o contato específico (apenas 1) com todos os seus dados cadastrados;
Se Consultar por Atividade, solicitar ao usuário que informe a atividade, e apresentar o(s) contato(s) que exercem aquela atividade com todos os seus dados cadastrados;
Se Retornar ao menu, deve-se retornar ao menu principal (return);
Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta D.a.
Enquanto o usuário não escolher a opção 4, o menu consultar contatos deve se repetir.
Deve-se implementar uma função chamada remover_contato() em que: [EXIGÊNCIA DE CÓDIGO 5 de 8];
Deve-se pergunta pelo id do contato a ser removido;
Remover o contato da lista_contatos;
Se o id fornecido não for de um contato da lista, printar “Id inválido” e repetir a pergunta E.a.
Deve-se implementar uma estrutura de menu no código principal (main), ou seja, não pode estar dentro de função, em que: [EXIGÊNCIA DE CÓDIGO 6 de 8];
Deve-se pergunta qual opção deseja (1. Cadastrar Contato / 2. Consultar Contato / 3. Remover Contato / 4. Encerrar Programa):
Se Cadastrar Contato, incrementar em um id_ global e em seguida, chamar a função cadastrar_contato (id_ global);
Se Consultar Contato, chamar função consultar_contato ();
Se Remover Contato, chamar função remover_ contato ();
Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta F.a.
Enquanto o usuário não escolher a opção 4, o menu deve se repetir.
Deve-se implementar uma lista de dicionários (uma lista contento dicionários dentro) [EXIGÊNCIA DE CÓDIGO 7 de 8];
Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
Deve-se apresentar na saída de console um cadastro do seu contato da seguinte forma: para nome informe seu nome completo (não usar apelidos ou abreviações), para atividade informar como estudante, e para telefone informe sua RU. [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 6];
Deve-se apresentar na saída de console um cadastro de mais 2 contatos com mesmo tipo de atividade (por exemplo: marceneiro, padeiro, pintor, pedreiro) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 6];
Deve-se apresentar na saída de console uma consulta de todos os contatos [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 6];
Deve-se apresentar na saída de console uma consulta por código (id) de um dos contados [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 6];
Deve-se apresentar na saída de console uma consulta por atividade em que 2 contatos exerçam a mesma atividade [EXIGÊNCIA DE SAÍDA DE CONSOLE 5 de 6];
Deve-se apresentar na saída de console uma remoção de um dos contatos e em seguida de uma consulta de todos os contatos, provando que o contato foi removido [EXIGÊNCIA DE SAÍDA DE CONSOLE 6 de 6];

"""
# Questão 4 - CONTATOS GERENCIAIS

print("Bem-vindo a Lista de Contatos de Isabelle Tschoeke Volaco")

# Lista que armazena contatos
listaContatos = []

# idglobal contendo meu RU
idGlobal = 4923552

# Função para cadastrar contato
def cadastrarContato(idContato):

    print("MENU CADASTRAR CONTATO")
    print(f"Id do Contato: {idContato}")
    
    nomeContato = input("Por favor entre com o nome do Contato: ")
    atividadeContato = input("Por favor entre com a Atividade do contato: ")
    telefoneContato = input("Por favor entre com o telefone do contato: ")
    
    # Armazena os dados em um dicionário
    contato = {
        'id': idContato,
        'nome': nomeContato,
        'atividade': atividadeContato,
        'telefone': telefoneContato
    }
    
    # Adiciona o contato à lista
    listaContatos.append(contato.copy())  # Usa copy para evitar referências

# Consulta os contatos
def consultarContatos():
    while True:
        # Menu de consulta
        print("MENU CONSULTAR CONTATOS")
        print("Escolha uma opção:")
        print("1 - Consultar Todos")
        print("2 - Consultar por Id")
        print("3 - Consultar por Atividade")
        print("4 - Retornar ao menu")
        opcaoConsulta = input(">> ")
        
        if opcaoConsulta == '1':
            # Exibe todos os contatos
            for contato in listaContatos:
                print(f"ID: {contato['id']}, Nome: {contato['nome']}, Atividade: {contato['atividade']}, Telefone: {contato['telefone']}")
        
        elif opcaoConsulta == '2':
            # Consulta por ID
            idConsulta = input("Informe o ID do contato: ")
            for contato in listaContatos:
                if contato['id'] == int(idConsulta):
                    print(f"ID: {contato['id']}, Nome: {contato['nome']}, Atividade: {contato['atividade']}, Telefone: {contato['telefone']}")
                    break
            else:
                print("Contato não encontrado.")
        
        elif opcaoConsulta == '3':
            # Consulta por atividade
            atividadeConsulta = input("Informe a atividade: ")
            for contato in listaContatos:
                if contato['atividade'].lower() == atividadeConsulta.lower():
                    print(f"ID: {contato['id']}, Nome: {contato['nome']}, Atividade: {contato['atividade']}, Telefone: {contato['telefone']}")
            else:
                print("Nenhum contato encontrado com essa atividade.")
        
        elif opcaoConsulta == '4':
            return  # Retorna pro menu principal
        
        else:
            print("Opção inválida. Tente novamente.")

# Função para remover contato
def removerContato():
    while True:
        idRemover = input("Informe o ID do contato a ser removido: ")
        for contato in listaContatos:
            if contato['id'] == int(idRemover):
                listaContatos.remove(contato)
                print("Contato removido com sucesso.")
                return
        else:
            print("Id inválido. Tente novamente.")

# Menu principal
while True:
    print("MENU PRINCIPAL")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Contato")
    print("2 - Consultar Contato(s)")
    print("3 - Remover Contato")
    print("4 - Sair")
    
    opcaoMenu = input(">> ")
    
    if opcaoMenu == '1':
        idGlobal += 1  # Incrementa o idglobal
        cadastrarContato(idGlobal)  
    
    elif opcaoMenu == '2':
        consultarContatos()  
    
    elif opcaoMenu == '3':
        removerContato()  
    
    elif opcaoMenu == '4':
        print("Programa encerrado.")
        break  # Sai do loop e encerra o programa
    
    else:
        print("Opção inválida. Tente novamente.")