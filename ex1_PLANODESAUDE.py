# Isabelle Tschoeke Volaco

"""
QUESTÃO 1

Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app para uma empresa X que vende Planos de Saúde. Uma das estratégias dessa empresa X é cobrar um valor diferente com base na idade do cliente, conforme a listagem abaixo:

Se a idade for maior ou igual que 0 e menor que 19, o valor será de 100% do valor base do plano (100 / 100);
Se a idade for maior ou igual que 19 e menor que 29, o valor será de 150% do valor base do plano (150 / 100);
Se a idade for maior ou igual que 29 e menor que 39, o valor será de 225% do valor base do plano (225 / 100);
Se a idade for maior ou igual que 39 e menor que 49, o valor será de 240% do valor base do plano (240 / 100);
Se a idade for maior ou igual que 49 e menor que 59, o valor será de 350% do valor base do plano (350 / 100);
Se a idade for maior ou igual que 59, o valor será de 600% do valor base do plano (600 / 100);

O valor mensal do plano é calculado da seguinte maneira:

valorMensal = valorBase * porcentagem

Elabore um programa em Python que:

Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui). 
Por exemplo: print(“Sistema desenvolvido por Bruno K******”) [EXIGÊNCIA DE CÓDIGO 1 de 6];
Deve-se implementar o input do valorBase do plano e da idade do cliente [EXIGÊNCIA DE CÓDIGO 2 de 6];
Deve-se implementar as regras de valores conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6];
Deve-se implementar o valorMensal [EXIGÊNCIA DE CÓDIGO 4 de 6];
Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];  
Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
Deve-se apresentar na saída de console uma mensagem com seu nome completo [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];
Deve-se apresentar na saída de console a utilização do sistema informando uma idade maior ou igual a 29 anos, apresentando na saída de console o valorMensal do plano [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2];  

"""
# Questão 1 - PLANOS DE SAÚDE 

print("Sistema desenvolvido por Isabelle Tschoeke Volaco")

# Função que pega a idade do usuário e retorna a porcentagem respectiva na forma decimal (convertida)
def taxaPlano(idade):
    if 0 <= idade < 19:
        return 1.0   
    elif 19 <= idade < 29:
        return 1.5 
    elif 29 <= idade < 39:
        return 2.25  
    elif 39 <= idade < 49:
        return 2.4 
    elif 49 <= idade < 59:
        return 3.5  
    else:  
        return 6.0  

# Calcula o valor mensal do plano com base na fórmula: valorMensal = valorBase * porcentagem
def valorPlano(valorBase, idade):
    taxa = taxaPlano(idade)  
    valorMensal = valorBase * taxa  
    return valorMensal

# input (entrada) do valor base e idade do cliente
valorBasePlano = float(input("Digite o valor base do plano ------ R$ "))
idadeCliente = int(input("Digite a idade do cliente ----- "))

# Cálculo do valor mensal e resultado
valorMensalPlano = valorPlano(valorBasePlano, idadeCliente)
print(f"Valor mensal do plano: R$ {valorMensalPlano}")