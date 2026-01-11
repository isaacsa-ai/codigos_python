#---------------------- CABEÇALHO ------------------
#Autor: Isaac de Sá da Silva
#Data:11/01/2026
#Descrição: Calculadora Simples com dois números
#
#----------------------------------------------------

#Variáveis
opcao = 0
resultado = 0
texto = '''Insira qual operação deseja realizar: 
                    
1 - Adição
2 - Multiplicação
3 - Divisão
4 - Potenciação

'''



#Entrada de Dados
while(1):

    #Escolhendo operação
    while(1):
        opcao = int(input(texto))
        
        if(opcao > 0 and opcao < 5):
            break
    
    #Recebendo numeros
    while(1):
        try:   
            num1 = float(input("Insira o primeiro numero: "))
            num2 = float(input("Insira o segundo numero: "))

            break

        except ValueError:
            print("Error: Insira valores válidos.")
            
    
    #Realizando operação
    #SOMA
    if(opcao == 1):
        resultado  = num1 + num2

    if(opcao == 2):
        resultado  = num1 * num2

    if(opcao == 3):
        resultado  = num1 / num2
    
    if(opcao == 4):
        resultado  = num1 ** num2


    #Saída de dados
    print("\n\nO resultado da operação é:"+ str(resultado))
    sair = int(input("\n\nDeseja finalizar? \n\n 1 - SIM \n 2 - Nao\n"))
    if(sair == 1):
        break



