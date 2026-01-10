#---------------------- CABEÇALHO ------------------
#Autor: Isaac de Sá da Silva
#Data:10/01/2026
#Descrição: Primeiro programa da minha jornada trabalhar nos EUA
#
#----------------------------------------------------

#Variaveis
texto = '''
\n
------------------------------ MENSAGEM -----------------------------------
Olá, este é a mensagem deixada por mim, isaac. Atualmente sou Analista de TI
e estou estudando programação pois quero me tornar um programador renomado e
um dia poder ir morar e trabalhar nos estados unidos.
-----------------------------------------------------------------------------
'''

opcao = 0

#Entrada de dados
print("Olá, esse é um programa desenvolvido por Isaac. Ele deixou uma mensagem escrita no dia 10 de janeiro de 2026, às 17:50, na Parquelândia, em Fortaleza. Desejas ver?")
print("\n1 - SIM\n2 - Não")
opcao = int(input("\nDigite a opção: "))

#Processamento e Saída de dados
if(opcao == 1):
    print(texto)
else:
    print("Tudo bem, até a proxima!")

