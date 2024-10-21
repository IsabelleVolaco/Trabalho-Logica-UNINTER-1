"""
QUESTÃO 3

Enunciado: Você foi contratado para desenvolver um sistema de Venda de uma Empresa Y que vende toras de arvore para outras empresas que vendem madeira. Você ficou com a parte de desenvolver a interface com o cliente.
A Empresa Y opera as vendas da seguinte maneira:

Tora de Pinho (PIN), o valor do metro cúbico (m³) é de cento e cinquenta reais e quarenta centavos;
Tora de Peroba (PER), o valor do metro cúbico (m³) é de cento e setenta reais e vinte centavos;
Tora de Mogno (MOG), o valor do metro cúbico (m³) é de cento e noventa reais e noventa centavos;
Tora de Ipê (IPE), o valor do metro cúbico (m³) é de duzentos e dez reais e dez centavos; 
Tora de Imbuia (IMB), o valor do metro cúbico (m³) é de duzentos e vinte reais e setenta centavos;

Se a quantidade (em m³) de toras for menor que 100 não há desconto na venda (0/100);
Se a quantidade (em m³) de toras for igual ou maior que 100 e menor que 500, o desconto será de 4% (4/100);
Se a quantidade (em m³) de toras for igual ou maior que 500 e menor que 1000, o desconto será de 9% (9/100);
Se a quantidade (em m³) de toras for igual ou maior que 1000 e menor ou igual que 2000, o desconto será de 16% (16/100);
Se a quantidade (em m³) de toras for maior que 2000, não é aceito pedidos com essa quantidade de toras;
	
Para o adicional de transporte rodoviário (1) é cobrado um valor extra de 1000 reais;
Para o adicional de transporte ferroviário (2) é cobrado um valor extra de 2000 reais;
Para o adicional de transporte hidroviário (3) é cobrado um valor extra de 2500 reais;

O valor final da conta é calculado da seguinte maneira:

total = ((tipoMadeira * qtdToras)*(1-desconto)) + transporte

Elabore um programa em Python que: 
Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui). 
Por exemplo: print(“Bem-vindos a Madeireira do Lenhador Bruno Kostiuk”)  [EXIGÊNCIA DE CÓDIGO 1 de 7];
Deve-se implementar a função escolha_tipo() que não recebe parâmetros e que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
Pergunta o tipo de madeira desejado;
Retorna o VALOR do tipo de madeira com base na escolha do usuário (use return);
Repete a pergunta do item B.a se digitar uma opção diferente de: PIN/PER/MOG/IPE/IMB;
Deve-se implementar a função qtd_toras() que não recebe parâmetros e que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
Pergunta a quantidade de toras;
Retorna (use return) a quantidade de toras E o valor do desconto (os dois valores) seguindo a regra do enunciado;
Repete a pergunta do item C.a se digitar um valor acima de 2000 ou valor não numérico (use try/except para não numérico)
Deve-se implementar a função transporte() que não recebe parâmetros e que: [EXIGÊNCIA DE CÓDIGO 4 de 7];
Pergunta pelo serviço adicional de transporte;
Retorna (use return) o valor de apenas uma das opções de transporte;
Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/3;
Deve-se implementar o total a pagar no código principal (main), ou seja, não pode estar dentro de função, conforme o enunciado [EXIGÊNCIA DE CÓDIGO 5 de 7];
Deve-se implementar try/except [EXIGÊNCIA DE CÓDIGO 6 de 7];
Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 7 de 7];
Deve-se apresentar na saída de console uma mensagem com o seu nome completo [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
Deve-se apresentar na saída de console um pedido no qual o usuário errou a opção de tipo de madeira [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];
Deve-se apresentar na saída de console um pedido no qual o usuário digitou um valor que ultrapasse a quantidade máxima de toras aceitas (2000) [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
Deve-se apresentar na saída de console um pedido com opção de tipo de madeira, quantidade de toras e transporte válidos [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];


"""
# Questão 3 - MADEIREIRA

print("Bem-vindos à Madeireira da Lenhadora Isabelle Tschoeke Volaco")

# Função que escolhe o tipo de madeira e retorna o valor
def escolhaMadeira():
    while True:
        print("Entre com o Tipo de Madeira desejado:")
        print("PIN - Tora de Pinho: R$ 150.40")
        print("PER - Tora de Peroba: R$ 170.20")
        print("MOG - Tora de Mogno: R$ 190.90")
        print("IPE - Tora de Ipê: R$ 210.10")
        print("IMB - Tora de Imbuia: R$ 220.70")
        
        tipoMadeiraEscolhido = input("Digite o tipo (PIN/PER/MOG/IPE/IMB): ").upper()
        if tipoMadeiraEscolhido == 'PIN':
            return 150.40
        elif tipoMadeiraEscolhido == 'PER':
            return 170.20
        elif tipoMadeiraEscolhido == 'MOG':
            return 190.90
        elif tipoMadeiraEscolhido == 'IPE':
            return 210.10
        elif tipoMadeiraEscolhido == 'IMB':
            return 220.70
        else:
            print("Escolha inválida, entre com o modelo novamente.")

# Função que pergunta a quantidade de toras e retorna a quantidade e o valor do desconto
def qtToras():
    while True:
        try:
            qtTorasEscolhida = float(input("Entre com a quantidade de toras (m³): "))
            if qtTorasEscolhida < 100:
                return qtTorasEscolhida, 0  
            elif 100 <= qtTorasEscolhida < 500:
                return qtTorasEscolhida, 0.04  
            elif 500 <= qtTorasEscolhida < 1000:
                return qtTorasEscolhida, 0.09  
            elif 1000 <= qtTorasEscolhida <= 2000:
                return qtTorasEscolhida, 0.16  
            else:
                print("Não aceitamos pedidos com essa quantidade de toras.")
        except ValueError:
            print("Entrada inválida. Por favor, entre um número.")

# Pergunta pelo tipo de transporte e retorna o valor do transporte
def transporte():
    while True:
        print("Escolha o tipo de Transporte:")
        print("1 - Transporte Rodoviário - R$ 1000.00")
        print("2 - Transporte Ferroviário - R$ 2000.00")
        print("3 - Transporte Hidroviário - R$ 2500.00")
        
        tipoTransporteEscolhido = input("Digite o tipo (1/2/3): ")
        if tipoTransporteEscolhido == '1':
            return 1000.00
        elif tipoTransporteEscolhido == '2':
            return 2000.00
        elif tipoTransporteEscolhido == '3':
            return 2500.00
        else:
            print("Opção inválida. Tente novamente.")

# Variáveis que chamam os métodos
tipoMadeiraValor = escolhaMadeira()
qtTorasEscolhida, desconto = qtToras()
tipoTransporteValor = transporte()

# Total a pagar
total = ((tipoMadeiraValor * qtTorasEscolhida) * (1 - desconto)) + tipoTransporteValor
print(f"Total: R$ {total}")