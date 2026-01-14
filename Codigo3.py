#---------------------- CABEÇALHO ------------------
#Autor: Isaac de Sá da Silva
#Data:11/01/2026
#
#Descrição: Esse programa representa um banco onde é possivel depositar, retirar
#Ver saldo e ver transações para uma determinada conta.
#
#----------------------------------------------------


#biblioteca
import os

#funcao limpar tela
def limpa_terminal():
    return os.system('clear')

#variaveis
saldo_atual = 0.0
operacoes = []
texto = '''
            
        SALDO EM CONTA: %g
    
1 - Cadastrar uma receita

2 - Cadastrar uma despesa

3 - Listar todas as transações cadastradas

4 - Exibir o saldo atual

5 - Encerrar o programa

OPÇÃO: '''

#entrada de dados
while(1):
    #Declarando e limpando variaveis
    operacao_atual = ''
    valor = 0.0
    descricao = ''
    opcao = 0

    try:
        opcao = int(input(texto %saldo_atual))

        if (opcao < 1 or opcao > 5):
            raise Exception
    except ValueError:
        limpa_terminal()
        print("ERROR: Insira uma opçao válida!")
    
    #Adicionando dinheiro ao banco
    if(opcao == 1):
        limpa_terminal()
        operacao_atual = 'Receita'
        try:
            valor = float(input("Insira o valor a ser depositado: "))
            if(valor <= 0):
                raise Exception
        except:
            limpa_terminal()
            print("ERROR: INSERÇÃO INVÁLIDA!")
            continue

        descricao = input("Insira a Descrição: ")
        
        operacoes.append([operacao_atual, valor, descricao])
        saldo_atual = saldo_atual + valor
        limpa_terminal()
    
    #Retirando dinheiro do banco
    if(opcao == 2):
        limpa_terminal()
        operacao_atual = 'despesa'
        try:
            valor = float(input("Insira o valor a ser Retirado: "))
            descricao = input("Insira a Descrição: ")
            if(valor <= 0):
                raise Exception
            if((saldo_atual - valor) < 0):
                limpa_terminal()
                print("ERROR: Não há esse valor em conta! ")
            else:
                operacoes.append([operacao_atual, valor, descricao])
                saldo_atual = saldo_atual - valor
                limpa_terminal()
        except:
            limpa_terminal()
            print("ERROR: INSERÇÃO INVÁLIDA!")
        
    #Imprimindo Transações
    if(opcao == 3):
        limpa_terminal()
        aux = 0
        
        print("-------------------- TRANSAÇÕES -----------------------------------\n") 
        
        for idx, operacao in enumerate(operacoes, start=1):
            print(f"{idx}° Operação: {operacao[0]} | {operacao[1]} | {operacao[2]}")

        print("\n-------------------------------------------------------------------\n\n") 
    
    #Mostrando Saldo em Conta
    if(opcao == 4):
        limpa_terminal()
        print("Seu saldo é:{} ".format(saldo_atual))
    
    #Encerrando o Programa
    if(opcao == 5):
        limpa_terminal()
        print("PROGRAMA ENCERRADO!!!")
        break