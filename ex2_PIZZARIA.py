"""
QUESTÃO 2

Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma Pizzaria que vende sabores de Pizzas Doces e Pizzas Salgadas. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.

A Loja possui seguinte relação:
Tamanho P: Pizza Salgada (PS) custa 30 reais e a Pizza Doce (PD) custa 34 reais;
Tamanho M: Pizza Salgada (PS) custa 45 reais e a Pizza Doce (PD) custa 48 reais;
Tamanho G: Pizza Salgada (PS) custa 60 reais e a Pizza Doce (PD) custa 66 reais;

Elabore um programa em Python que: 
Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui). 
Por exemplo: print(“Bem-vindos a Pizzaria do Bruno Kostiuk”) 
Além do seu nome completo, deve-se implementar um print com um Menu para o cliente. [EXIGÊNCIA DE CÓDIGO 1 de 8];
Deve-se implementar o input do sabor (PS/PD) e o print “Sabor inválido. Tente novamente" se o usuário entra com valor diferente de PS e PD [EXIGÊNCIA DE CÓDIGO 2 de 8];
Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P, M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8];
Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula 3 – Tema 4) com cada uma das combinações de sabor e tamanho [EXIGÊNCIA DE CÓDIGO 4 de 8];
Deve-se implementar um acumulador para somar os valores dos pedidos (valor total do pedido) [EXIGÊNCIA DE CÓDIGO 5 de 8];
Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8];
Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8];
Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
Deve-se apresentar na saída de console uma mensagem com o seu nome completo e o menu para o cliente conhecer as opções  [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4]; 
Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];  

Figura 2.1: Exemplo de saída de console que o aluno deve fazer. Em que se perguntar o sabor e o tamanho. Há uma tentativa de pedido que se errou o sabor e outra que se errou o tamanho. Há também um pedido com dois itens com sabores e tamanhos diferentes.

"""
# Questão 2 - PIZZARIA

print("Bem-vindos à Pizzaria de Isabelle Tschoeke Volaco")

# Função que mostra o menu do cardápio para o cliente
def mostrarCardapio():
    print("\n--- Cardápio ---")
    print("Pizza Salgada (PS)")
    print("Tamanho P: R$ 30.00")
    print("Tamanho M: R$ 45.00")
    print("Tamanho G: R$ 60.00")
    print("Pizza Doce (PD)")
    print("Tamanho P: R$ 34.00")
    print("Tamanho M: R$ 48.00")
    print("Tamanho G: R$ 66.00")
    print("-------------------")

# Escolher o sabor da pizza
def escolherSabor():
    while True:
        sabor = input("Entre com o sabor desejado (PS/PD): ").upper()
        if sabor in ['PS', 'PD']:
            return sabor
        else:
            print("Sabor inválido. Tente novamente.")
            

# Escolher o tamanho da pizza
def escolherTamanho():
    while True:
        tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()
        if tamanho in ['P', 'M', 'G']:
            return tamanho
        else:
            print("Tamanho inválido. Tente novamente.")

# Calcula o valor da pizza
def calcularValor(sabor, tamanho):
    if sabor == 'PS':  
        if tamanho == 'P':
            return 30.00
        elif tamanho == 'M':
            return 45.00
        elif tamanho == 'G':
            return 60.00
    elif sabor == 'PD':  
        if tamanho == 'P':
            return 34.00
        elif tamanho == 'M':
            return 48.00
        elif tamanho == 'G':
            return 66.00

# Essa variável armazena o total do pedido
total_pedido = 0

# Loop while para o pedido
while True:
    mostrarCardapio()

    # Chamando a função que escolhe sabor e tamanho
    saborEscolhido = escolherSabor()
    tamanhoEscolhido = escolherTamanho()

    # Calcula e armazena o valor do pedido
    valor = calcularValor(saborEscolhido, tamanhoEscolhido)
    total_pedido += valor

    # Mostra no console o pedido feito pelo cliente
    if saborEscolhido == 'PS':
        print(f"Você pediu uma Pizza Salgada no tamanho {tamanhoEscolhido}: R$ {valor}")
    else:
        print(f"Você pediu uma Pizza Doce no tamanho {tamanhoEscolhido}: R$ {valor}")

    # Pergunta se deseja fazer outro pedido
    repetirPedido = input("Deseja mais alguma coisa? (S/N): ").upper()
    if repetirPedido == 'N':
        break  # Isso acaba com o loop se não quiser mais nada

# Mostra o valor total do pedido
print(f"Valor total a ser pago: R$ {total_pedido}")