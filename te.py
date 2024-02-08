print("\n" * 5)
import webbrowser
import datetime
import os
import msvcrt as m
import numpy as np 
import matplotlib.pyplot as plt
import tkinter as tk
import pygame
import time


os.system("cls" if os.name == "nt" else "clear")

def wait():
    print("Aperte qualquer tecla para continuar")
    m.getch()
    os.system("cls" if os.name == "nt" else "clear")

    
#from playsound import playsound



#Variáveis / Listas
um = "https://www.youtube.com/watch?v=x9NQFIYPjUw"
nininho = "https://youtu.be/LX-BvWDaCC4?feature=shared"
bj = "https://www.youtube.com/watch?v=uzWO7O-qHWI&pp=ygUYYm9uIGpvdmkgaGF2ZSBhIG5pY2UgZGF5"

lista_comida = []
lista_comidap = []                 
lista_funcionarios = []   
lista_bebidas = []
lista_bebidasp = []                   
lista_servicos = []
lista_servicosp = []      
lista_item = []
lista_qt = []
lista_preco = []
lista_stocks = []
lista_stockb = []
lista_stockc = []
lista_stockmc = []
lista_stockmb = []
lista_stockms = []
lista_candidaturas = []
lista_users = []
lista_candidaturas2 = []
grafx = []
grafy = []
total = 0
qt = 0
valor = 0
saldoemp = 0
qtf = 0
salario = 10
totsal = 0
mc = 0
delete = 0
exp = 0
cargoc = 0
ps = 1
class TerminalColors:  
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    ROSA = '\033[95m'
    ROXO = '\033[35m'
    CINZENTO = '\033[37m'
    ENDC = '\033[0m'

#def def_login():
#    import os

def def_default():
    global lista_bebidas, lista_comida, lista_servicos, lista_item, lista_preco, total, lista_qt, qt, valor, lista_funcionarios, saldoemp, lista_stocks, lista_stockc, lista_stockb
    global lista_stockmc, lista_stockmb, lista_stockms, mc, mb, ms,lista_comidap, lista_bebidasp, lista_servicosp, data_res, qtp,nomer, lista_candidaturas,nomec,idadec,cargoc,exp
    global lista_users,delete,lista_candidaturas2,grafx,grafy,ps

def_default()  





def def_sempreco():
    file_semp = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\lista_comidasemprec.fsd", "r", encoding='utf-8') 
    for i in file_semp:
        lista_comidap.append(str(i.strip()))
    file_semp.close()
    i=0
    file_semp = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\lista_bebidasemprec.fsd", "r", encoding='utf-8') 
    for i in file_semp:
        lista_bebidasp.append(str(i.strip()))
    file_semp.close()
    i=0
    file_semp = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\lista_servicossemprec.fsd", "r", encoding='utf-8') 
    for i in file_semp:
        lista_servicosp.append(str(i.strip()))
    file_semp.close()


def users():
    file_login = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\login.fsd", "r", encoding='utf-8') 
    for i in file_login:
        lista_users.append(i.strip().split(':'))
    file_login.close()

def rcandidaturas2():
    
    file_cand = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\candidaturas2.fsd", "r", encoding='utf-8') 
    for i in file_cand:
        lista_candidaturas2.append(i.strip())
    file_cand.close()




def rcandidaturas():
    
    file_cand = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\candidaturas.fsd", "r", encoding='utf-8', errors='ignore') 
    for i in file_cand:
        lista_candidaturas.append(i.strip().split(':'))
    file_cand.close()

def registar_candidaturas():
    global nomec,idadec,cargoc,exp
    with open('C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\candidaturas.fsd', 'a') as file:
        file.write('{}:{}:{}:{}\n'.format(nomec,cargoc,idadec,exp))

def reg_cand2():
    global nomec,idadec,cargoc,exp
    with open('C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\candidaturas2.fsd', 'a') as file:
        file.write('{} {} {} {}\n'.format(nomec,cargoc,idadec,exp))


def def_stockm():
    file_stockmc = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\stockmc.fsd", "r", encoding='utf-8') 
    for i in file_stockmc:
        lista_stockmc.append(str(i.strip()))
    file_stockmc.close()
    i=0
    file_stockmb = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\stockmb.fsd", "r", encoding='utf-8') 
    for i in file_stockmb:
        lista_stockmb.append(str(i.strip()))
    file_stockmb.close()
    i=0
    file_stockms = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\stockms.fsd", "r", encoding='utf-8') 
    for i in file_stockms:
        lista_stockms.append(str(i.strip()))
    file_stockms.close()



def def_wstocks():
    with open('C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\stocks.fsd', 'w') as file:
        for ss in lista_stocks:
            file.write(str(ss) + "\n")

def def_wreserva():
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\reservas.fsd', 'a') as file:
        file.write('{} {} {}\n'.format( nomer,data_res,qtp,data ))


def def_wstockc():
    with open('C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\stockc.fsd', 'w') as file:
        for sc in lista_stockc:
            file.write(str(sc) + "\n")


def def_wstockb():
    with open('C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\stockb.fsd', 'w') as file:
        for sb in lista_stockb:
            file.write(str(sb) + "\n")
def reg_saldo():
    with open('C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\saldo.fsd', 'w') as file:
        file.write('{}\n'.format(saldoemp))


def registar_funcionarios(nome, cargo):
    with open('C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\funcionarios.fsd', 'a') as file:
        file.write('{} {}\n'.format(nome, cargo))


def def_lersaldo():
    global saldoemp
    with open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\saldo.fsd", "r") as f:
        for s in f:
            try:
            # Tenta converter a string para um número inteiro
                saldoemp = int(s.strip())
            except ValueError:
            # Caso não seja possível converter para inteiro, imprima um aviso
             print("O conteúdo do ficheiro não é um número inteiro.")

def registar_usuario(username, password):
    with open('C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\login.fsd', 'a') as file:
        file.write('{}:{}\n'.format(username, password))

def verificar_credenciais(username, password):
    with open('C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\login.fsd', 'r') as file:
        for line in file:
            credentials = line.strip().split(':')
            if len(credentials) == 2:
                stored_username, stored_password = credentials
                if username == stored_username and password == stored_password:
                    return True
    return False



def rreservas():
    with open('C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\reservas.fsd', 'r') as file:
        for line in file:
            nomev, datav, qtv = line.strip().split(' ')
            print(TerminalColors.AZUL + f"Nome da reserva {nomev} Data da reserva {datav} Quantidade de pessoas {qtv}" + TerminalColors.ENDC) 

def def_login():
    
    while True:   
        users()
        l=-1
        print(TerminalColors.AMARELO + "1. Criar nova conta" + TerminalColors.ENDC)
        print(TerminalColors.VERDE + "2. Fazer login" + TerminalColors.ENDC)
        print(TerminalColors.VERMELHO + "3. Sair" + TerminalColors.ENDC)

        escolha = input(TerminalColors.CINZENTO + "Escolha uma opção: " + TerminalColors.ENDC)

        match escolha:
            case '1':
                username = input(TerminalColors.ROSA + "Digite um novo nome de usuário: " + TerminalColors.ENDC)
                password = input(TerminalColors.ROXO + "Digite uma nova senha: " + TerminalColors.ENDC)
                if lista_users == []:
                    registar_usuario(username, password)
                    print(TerminalColors.AZUL + "Conta criada com sucesso!\n" + TerminalColors.ENDC)
                    wait()
                else:
                    for u in lista_users:
                        u=u
                        l=l+1
                        usernamet, passwordt = lista_users[l]   
                        if username == usernamet:
                            print(TerminalColors.VERMELHO + "Ja existe esse user" + TerminalColors.ENDC)
                            def_login()
                        else:
                            registar_usuario(username, password)
                            print(TerminalColors.AZUL + "Conta criada com sucesso!\n" + TerminalColors.ENDC)
                            wait()
                            break
                def_login()
            case '2':
                username = input(TerminalColors.ROSA + "Digite o seu user: " + TerminalColors.ENDC)
                password = input(TerminalColors.ROXO + "Digite a sua senha: " + TerminalColors.ENDC)
                if verificar_credenciais(username, password):
                    print(TerminalColors.AZUL + "Login bem-sucedido. Bem-vindo, {}!\n".format(username) + TerminalColors.ENDC)
                    wait()
                    def_staff()
                    break
                else:
                    print(TerminalColors.VERMELHO + "Credenciais incorretas. Tente novamente.\n" + TerminalColors.ENDC)
                    wait()
            case '3':
                print("A sair ...")
                os.system("cls" if os.name == "nt" else "clear")
                def_main()
            case _:
                print(TerminalColors.VERMELHO + "Opção inválida. Tente novamente.\n" + TerminalColors.ENDC)
                
        

            
    
# Chama a função de login
#login()

# Funções (Files)
def def_read_files():
  
  file_com = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\lista_comida.fsd","r", encoding='utf-8')
  for i in file_com:
    lista_comida.append(str(i.strip()))
  file_com.close()

  file_beb = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\lista_bebidas.fsd", "r", encoding='utf-8') 
  for i in file_beb:
    lista_bebidas.append(str(i.strip()))
  file_beb.close()

  file_serv = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\lista_servicos.fsd", "r", encoding='utf-8') 
  for i in file_serv:
    lista_servicos.append(str(i.strip()))
  file_serv.close()

  

  i = 0
  while i <= (len(lista_comida) - 1): 
        if '$' in lista_comida[i]:
            lista_comida[i] = str(lista_comida[i][:lista_comida[i].index('$') - 1]) + ' ' * (20 - (lista_comida[i].index('$') - 1)) + str(lista_comida[i][lista_comida[i].index('$'):])
        i += 1

  i = 0
  while i <= (len(lista_bebidas) - 1):
        if '$' in lista_bebidas[i]:
            lista_bebidas[i] = str(lista_bebidas[i][:lista_bebidas[i].index('$') - 1]) + ' ' * (20 - (lista_bebidas[i].index('$') - 1)) + str(lista_bebidas[i][lista_bebidas[i].index('$'):])
        i += 1

  i = 0
  while i <= (len(lista_servicos) - 1):
        if '$' in lista_servicos[i]:
            lista_servicos[i] = str(lista_servicos[i][:lista_servicos[i].index('$') - 1]) + ' ' * (20 - (lista_servicos[i].index('$') - 1)) + str(lista_servicos[i][lista_servicos[i].index('$'):])
        i += 1

  


def_read_files()
def_lersaldo()
def def_read_stockc():
    global lista_stockc
    lista_stockc = []
    if lista_stockc == []:
        file_stockc = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\stockc.fsd", "r", encoding='utf-8') 
        for i in file_stockc:
            lista_stockc.append(str(i.strip()))
        file_stockc.close()

def def_read_stockb():
    global lista_stockb
    lista_stockb = []
    if lista_stockb == []:
        file_stockb = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\stockb.fsd", "r", encoding='utf-8') 
        for i in file_stockb:
            lista_stockb.append(str(i.strip()))
        file_stockb.close()

def def_read_stocks():
    global lista_stocks
    lista_stocks = []
    if lista_stocks == []:
        file_stocks = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\stocks.fsd", "r", encoding='utf-8') 
        for i in file_stocks:
            lista_stocks.append(str(i.strip()))
        file_stocks.close()

def def_graficoss():
    def_read_stocks()
    global grafx
    global grafy
    global lista_stocks

   
    lista_f = ['0']
    
    
    grafx = ['Inicio','Mesas', 'Toalhas', 'Cartão presente Refeição (30 d)', 'Cartão presente Refeição (10 d)', 'Cartão presente Refeição (7 d)']
    

    grafy = [lista_f[0],lista_stocks[0], lista_stocks[1], lista_stocks[2], lista_stocks[3], lista_stocks[4]]


    plt.bar(grafx, grafy, width=0.8, align='center', alpha=0.7, color='yellow', edgecolor='white', label='Stock')


    plt.title('Stock dos Serviços')
    plt.xlabel('Produtos')
    plt.ylabel('Quantidade em Stock')
    plt.legend()
    plt.grid(True)


    plt.show()




def def_graficosc():
    def_read_stockc()
    global grafx
    global grafy
    global lista_stockc

    # Assuming lista_stocks has at least 5 elements
    lista_f = ['0']
    
    # Dados para o gráfico (pode ajustar conforme necessário)
    grafx = ['Inicio','1-Pastel de bacalhau', '2-Amêijoas', '3-Cozido', '4-Leitão', '5-Francesinha','6-Bacalhau','7-Polvo','8-Pato','9-Alheira','10-Sopa']
    
    # Subtrair o valor inicial (lista_stocks[0]) de todos os valores em grafy
    grafy = [lista_f[0],lista_stockc[0], lista_stockc[1], lista_stockc[2], lista_stockc[3], lista_stockc[4],lista_stockc[5],lista_stockc[6],lista_stockc[7],lista_stockc[8],lista_stockc[9]]

    # Criar o gráfico de barras
    plt.bar(grafx, grafy, width=0.8, align='center', alpha=0.7, color='green', edgecolor='white', label='Stock')

    # Configurações do gráfico
    plt.title('Stock de Comida')
    plt.xlabel('Produtos')
    plt.ylabel('Quantidade em Stock')
    
    #plt.grid(True)

    # Exibir o gráfico
    plt.show()

def def_graficosb():
    def_read_stockb()
    global grafx
    global grafy
    global lista_stockb

    # Assuming lista_stocks has at least 5 elements
    lista_f = ['0']
    
    # Dados para o gráfico (pode ajustar conforme necessário)
    grafx = ['Inicio', '1-Verde', '2-Maduro', '3-alta gama', '4-Fraga', '5-Veuve-Cliquot', '6-Cola', '7-Seven-Up', '8-Ice Tea', '9-Ginja', '10-Beirão', '11-Porto', '12-Moscatel', '13-Aguardente', '14-Aperol', '15-Gin']
    
    # Subtrair o valor inicial (lista_stocks[0]) de todos os valores em grafy
    grafy = [lista_f[0],lista_stockb[0], lista_stockb[1], lista_stockb[2], lista_stockb[3], lista_stockb[4],lista_stockb[5],lista_stockb[6],lista_stockb[7],lista_stockb[8],lista_stockb[9], lista_stockb[10], lista_stockb[11], lista_stockb[12], lista_stockb[13], lista_stockb[14]]

    # Criar o gráfico de barras
    plt.bar(grafx, grafy, width=0.8, align='center', alpha=0.7, color='blue', edgecolor='white', label='Stock')

    # Configurações do gráfico
    plt.title('Stock de Bebidas')
    plt.xlabel('Produtos')
    plt.ylabel('Quantidade em Stock')
    
    #plt.grid(True)
    
    # Exibir o gráfico
    plt.show()

def def_read_func():
    global lista_funcionarios
    lista_funcionarios = []
    if lista_funcionarios == []:
        file_func = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\funcionarios.fsd", "r", encoding='utf-8') 
        for i in file_func:
            lista_funcionarios.append(str(i.strip()))
        file_func.close()

def delete_linha(candidatura):
    global delete
    file_path = 'C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\candidaturas.fsd'

    # Read existing lines
    with open(file_path, 'r', encoding='utf-8') as file:
        orig_lines = [line.strip() for line in file]

    # Check if candidatura is in the list
    if candidatura in orig_lines:
        orig_lines.remove(candidatura)

        # Save the updated list back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(orig_lines))

    else:
        print(f"Candidatura '{candidatura}' not found in the list222.")


def delete_linha2(candidatura):
    global delete
    file_path = 'C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\candidaturas2.fsd'

    # Read existing lines
    with open(file_path, 'r', encoding='utf-8') as file:
        orig_lines = [line.strip() for line in file]

    # Check if candidatura is in the list
    if candidatura in orig_lines:
        orig_lines.remove(candidatura)

        # Save the updated list back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(orig_lines))

    else:
        print(f"Candidatura '{candidatura}' not found in the list.")

def def_comida():

    global total
    global lista_qt
    global saldoemp
    global lista_stockc
    def_read_stockc()
    print(TerminalColors.AMARELO + "11-Voltar" + TerminalColors.ENDC)
    opcaomc=input(TerminalColors.CINZENTO + 'Qual e a sua escolha: ' + TerminalColors.ENDC)    
    match opcaomc:
    
        case '1':
            print(TerminalColors.AZUL + 'Escolheu pastel de bacalhau' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockc[0]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=1*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Pastel de bacalhau' + TerminalColors.ENDC)
                lista_preco.append('1')
                
                if qt.isdigit():
                    lista_stockc[0] = str(int(lista_stockc[0]) - int(qt))
                    def_wstockc()
                total+=valor
                saldoemp += valor
                wait()
        case '2':
            print(TerminalColors.AZUL + 'Escolheu Amêijoas à Bulhão Pato' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockc[1]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=12*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Amêijoas à Bulhão Pato' + TerminalColors.ENDC)
                lista_preco.append('12')
                 
                if qt.isdigit():
                    lista_stockc[1] = str(int(lista_stockc[1]) - int(qt))
                    def_wstockc() 
                total+=valor
                saldoemp += valor
                wait()
        case '3':
            print(TerminalColors.AZUL + 'Escolheu Cozido à portuguesa' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockc[2]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=18*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)    
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Cozido à portuguesa' + TerminalColors.ENDC)
                lista_preco.append('18')
                 
                if qt.isdigit():
                    lista_stockc[2] = str(int(lista_stockc[2]) - int(qt))
                    def_wstockc()
                total+=valor
                saldoemp += valor
                wait()
        case '4':
            print(TerminalColors.AZUL + 'Escolheu Leitão da Bairrada' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockc[3]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=30*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)    
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Leitão da Bairrada' + TerminalColors.ENDC)
                lista_preco.append('30')
                 
                if qt.isdigit():
                    lista_stockc[3] = str(int(lista_stockc[3]) - int(qt)) 
                    def_wstockc()
                total+=valor
                saldoemp += valor
                wait()
        case '5':
            print(TerminalColors.AZUL + 'Escolheu Francesinha' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockc[4]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=10*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)    
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Francesinha' + TerminalColors.ENDC)    
                lista_preco.append('10')
                 
                if qt.isdigit():
                    lista_stockc[4] = str(int(lista_stockc[4]) - int(qt))
                    def_wstockc()
                total+=valor
                saldoemp += valor
                wait()
        case '6':
            print(TerminalColors.AZUL + 'Escolheu Bacalhau à Brás' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockc[5]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=8*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Bacalhau à brás' + TerminalColors.ENDC)
                lista_preco.append('8')
                 
                if qt.isdigit():
                    lista_stockc[5] = str(int(lista_stockc[5]) - int(qt))
                    def_wstockc()
                total+=valor
                saldoemp += valor
                wait()
        case '7':
            print(TerminalColors.AZUL + 'Escolheu Polvo à lagareiro' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockc[6]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=25*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Polvo à lagareiro' + TerminalColors.ENDC)
                lista_preco.append('25')
                 
                if qt.isdigit():
                    lista_stockc[6] = str(int(lista_stockc[6]) - int(qt))
                    def_wstockc()
                total+=valor
                saldoemp += valor
                wait()
        case '8':
            print(TerminalColors.AZUL + 'Escolheu Arroz de pato' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockc[7]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=9*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Arroz de pato' + TerminalColors.ENDC)
                lista_preco.append('9')
                 
                if qt.isdigit():
                    lista_stockc[7] = str(int(lista_stockc[7]) - int(qt))
                    def_wstockc()
                total+=valor
                saldoemp += valor
                wait()
        case '9':
            print(TerminalColors.AZUL + 'Escolheu Alheira de Mirandela' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos quer?'  + TerminalColors.ENDC)
            if int(qt) > int(lista_stockc[8]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=6*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Alheira de Mirandela' + TerminalColors.ENDC)
                lista_preco.append('6')
                 
                if qt.isdigit():
                    lista_stockc[8] = str(int(lista_stockc[8]) - int(qt))
                    def_wstockc()
                total+=valor
                saldoemp += valor
                wait()
        case '10': 
            print(TerminalColors.AZUL + 'Escolheu Sopa da pedra' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos quer?' + TerminalColors.ENDC)  
            if int(qt) > int(lista_stockc[9]): 
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait() 
            else:
                valor=5*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Sopa da pedra' + TerminalColors.ENDC)
                lista_preco.append('5')
                if qt.isdigit():
                    lista_stockc[9] = str(int(lista_stockc[9]) - int(qt))
                    def_wstockc()
                total+=valor
                saldoemp += valor
                wait()
        case '11':
            print(TerminalColors.AZUL + "A voltar para o menu anterior..." + TerminalColors.ENDC)
            def_main()
        case _:
            print(TerminalColors.VERMELHO + "Escolha não encontrada" + TerminalColors.ENDC)
        
def def_bebidas():
    global total
    global lista_qt
    global saldoemp
    def_read_stockb()
    opcaomb=input(TerminalColors.CINZENTO + 'Qual e a sua escolha: ' + TerminalColors.ENDC)    
    match opcaomb:
        case '1':
            print(TerminalColors.AZUL + 'Escolheu Vinho Verde (casa)' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[0]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=15*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Vinho Verde (casa)' + TerminalColors.ENDC)
                lista_preco.append('15')
                
                if qt.isdigit():
                    lista_stockb[0] = str(int(lista_stockb[0]) - int(qt))
                    def_wstockb()
                total+=valor
                saldoemp += valor
                wait()
        case '2':
            print(TerminalColors.AZUL + 'Escolheu Vinho Maduro (casa)' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[1]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=15*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Vinho Maduro (casa)' + TerminalColors.ENDC)
                lista_preco.append('15')
                
                if qt.isdigit():
                    lista_stockb[1] = str(int(lista_stockb[1]) - int(qt))
                    def_wstockb()
                total+=valor
                saldoemp += valor
                wait()
        case '3':
            print(TerminalColors.AZUL + 'Escolheu Vinhos de alta gama' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[2]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=250*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Vinhos de alta gama' + TerminalColors.ENDC)
                lista_preco.append('250')
                
                if qt.isdigit():
                    lista_stockb[2] = str(int(lista_stockb[2]) - int(qt))
                    def_wstockb()
                total+=valor
                saldoemp += valor
                wait()
        case '4':
            print(TerminalColors.AZUL + 'Escolheu Vinho Espumante Fraga da Pena' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[3]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=70*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Vinho Espumante Fraga da Pena' + TerminalColors.ENDC)
                lista_preco.append('70')
                
                if qt.isdigit():
                    lista_stockb[3] = str(int(lista_stockb[3]) - int(qt))
                    def_wstockb()
                total+=valor
                saldoemp += valor
                wait()
        case '5':
            print(TerminalColors.AZUL + 'Escolheu Champagne Veuve-Cliquot' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[4]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=150*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Champagne Veuve-Cliquot' + TerminalColors.ENDC)
                lista_preco.append('150')
                
                if qt.isdigit():
                    lista_stockb[4] = str(int(lista_stockb[4]) - int(qt))
                    def_wstockb()
                total+=valor
                saldoemp += valor
                wait()
        case '6':
            print(TerminalColors.AZUL + 'Escolheu Coca-Cola' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[5]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=2*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Coca-Cola' + TerminalColors.ENDC)
                lista_preco.append('2')
                
                if qt.isdigit():
                    lista_stockb[5] = str(int(lista_stockb[5]) - int(qt))
                    def_wstockb()
                total+=valor
                saldoemp += valor
                wait()
        case '7':
            print(TerminalColors.AZUL + 'Escolheu Seven-Up' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[6]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=2*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)    
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Seven-Up' + TerminalColors.ENDC)
                lista_preco.append('2')
                
                if qt.isdigit():
                    lista_stockb[6] = str(int(lista_stockb[6]) - int(qt))
                    def_wstockb()
                total+=valor
                saldoemp += valor
                wait()
        case '8':
            print(TerminalColors.AZUL + 'Escolheu Ice Tea' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[7]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=2*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Seven-Up' + TerminalColors.ENDC)
                lista_preco.append('2')
                
                if qt.isdigit():
                    lista_stockb[7] = str(int(lista_stockb[7]) - int(qt))
                    def_wstockb()
                total+=valor
                saldoemp += valor
                wait()
        case '9':
            print(TerminalColors.AZUL + 'Escolheu Ginja' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[8]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=15*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Ginja' + TerminalColors.ENDC)
                lista_preco.append('15')
                
                if qt.isdigit():
                    lista_stockb[8] = str(int(lista_stockb[8]) - int(qt))
                    def_wstockb()
                total+=valor
                saldoemp += valor
                wait()
        case '10':
            print(TerminalColors.AZUL + 'Escolheu Licor Beirão'+ TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[9]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=13*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Licor Beirão' + TerminalColors.ENDC)
                lista_preco.append('13')
                
                if qt.isdigit():
                    lista_stockb[9] = str(int(lista_stockb[9]) - int(qt))    
                    def_wstockb()
                total+=valor
                saldoemp += valor
                wait()
        case '11':
            print(TerminalColors.AZUL + 'Escolheu Porto tonic' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[10]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=16*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Porto tonic' + TerminalColors.ENDC)
                lista_preco.append('16')
                
                if qt.isdigit():
                    lista_stockb[10] = str(int(lista_stockb[10]) - int(qt))   
                    def_wstockb() 
                total+=valor
                saldoemp += valor
                wait()
        case '12':
            print(TerminalColors.AZUL + 'Escolheu Moscatel de Setúbal' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[11]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=10*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Moscatel de Setúbal' + TerminalColors.ENDC)
                lista_preco.append('10')
                
                if qt.isdigit():
                    lista_stockb[11] = str(int(lista_stockb[11]) - int(qt))   
                    def_wstockb()
                total+=valor
                saldoemp += valor
                wait()
                
        case '13':
            print(TerminalColors.AZUL + 'Escolheu Aguardente de medronho' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO +'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[12]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=25*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)   
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Aguardente de medronho' + TerminalColors.ENDC)
                lista_preco.append('25')
                
                if qt.isdigit():
                    lista_stockb[12] = str(int(lista_stockb[12]) - int(qt))
                    def_wstockb() 
                total+=valor
                saldoemp += valor   
                wait()
        case '14':
            print(TerminalColors.AZUL + 'Escolheu Aperol Spritz' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[13]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=15*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)    
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Aperol Spritz' + TerminalColors.ENDC)
                lista_preco.append('15')
                
                if qt.isdigit():
                    lista_stockb[13] = str(int(lista_stockb[13]) - int(qt))    
                    def_wstockb()
                total+=valor
                saldoemp += valor
                wait()

        case '15':
            print(TerminalColors.AZUL + 'Escolheu Gin Tonic' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantas quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stockb[14]):
                print(TerminalColors.VERMELHO + "Nao há stock suficiente" + TerminalColors.ENDC)
                wait()
            else:
                valor=15*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append(TerminalColors.AZUL + 'Gin Tonic' + TerminalColors.ENDC)
                lista_preco.append('15')
                
                if qt.isdigit():
                    lista_stockb[14] = str(int(lista_stockb[14]) - int(qt))
                    def_wstockb()
                total+=valor
                saldoemp += valor 
                wait()
        case '16':
            print(TerminalColors.AZUL + "A voltar para o menu anterior..." + TerminalColors.ENDC)
            os.system("cls" if os.name == "nt" else "clear")
            def_main()
        case _:
            print(TerminalColors.VERMELHO +"Escolha não encontrada" + TerminalColors.ENDC)
            wait()

def def_talao():
    global lista_item, lista_qt, lista_preco, total

    with open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\report.fsd", "a", encoding="utf-8") as file:
        file.write("\nDetalhes da compra:\n")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formatação sem milissegundos
        for item, qt, preco in zip(lista_item, lista_qt, lista_preco):
            file.write(f"Item: {item}, Quantidade: {qt}, Preço: {preco}, {current_time}\n")
        file.write(f"Total: {total}")
        
def def_pagamento():
    global ps
    for z, y, x in zip(lista_item, lista_preco, lista_qt):
        print(f"Item: {z}, Preço: {y} * Quantidade: {x}")
    print(TerminalColors.AZUL + "O seu valor total é " + str(total) + TerminalColors.ENDC)
    dec = input("Quer pagar agora S/N")
    if dec.lower() in ['s']:
        reg_saldo()
        def_talao()
        print("Foi efetuado o seu pagamento")
        wait()
    else:
        p = 1
        def_main()
    


def def_pags():
    global saldoemp
    def_lersaldo()
    totsal = qtf * salario
    if saldoemp >= totsal:
        saldoemp -= totsal
        print(TerminalColors.VERDE + "Pagamento efetuado" + TerminalColors.ENDC)
        reg_saldo()
        wait()
        
    else:
        print(TerminalColors.VERMELHO + "Não tem saldo suficiente para o pagamento" + TerminalColors.ENDC)
        wait()
        
    
def def_mostrartalao():
    file_talao = open("C:\\Users\\hemoura\\Desktop\\Food Ordering System\\Projeto\\files\\report.fsd", "r", encoding='utf-8').read()
    print(f'\n{file_talao}')
    wait()

def def_freserva():
    global data_res,qtp,nomer
    print(TerminalColors.VERDE + "Faça a sua reserva aqui" + TerminalColors.ENDC)
    nomer=input(TerminalColors.AMARELO + "Em que nome fica a reserva?" + TerminalColors.ENDC)
    data_res=input(TerminalColors.AZUL + "Data da Reserva (DD/MM/AAAA): " + TerminalColors.ENDC)
    comp = len(data_res)
    if comp != 10:
        print("Data invalida")
    else:
        qtp=input(TerminalColors.CINZENTO + "Para quantas pessoas vai ser a reserva?: " + TerminalColors.ENDC)
        print(TerminalColors.ROSA + "Reserva efetuada!" + TerminalColors.ENDC)
        def_wreserva()
        wait()
def def_reserva():
    print(TerminalColors.VERDE + "1-Fazer Reserva" + TerminalColors.ENDC)
    print(TerminalColors.AMARELO + "2-Ver Reservas" + TerminalColors.ENDC)
    opc3=input(TerminalColors.AZUL + "Digite a Opção: " + TerminalColors.ENDC)

    match opc3:
        case '1':
            def_freserva()
        case '2':
            rreservas()
            wait()



def def_servicos():
    
    global total
    global qt 
    global saldoemp
    global lista_stock    
    def_read_stocks()
    opcaosv=input(TerminalColors.VERDE + 'Qual e a sua escolha: ' + TerminalColors.ENDC)    

    match opcaosv:
     
        case '1':
            print(TerminalColors.AZUL + 'Escolheu show de abertura de garrafa (Vinhos/Espumantes)' + TerminalColors.ENDC)
            valor=25
            qt=1
            print (TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
            lista_qt.append(qt)
            lista_item.append('Show abertura de garrafa')
            lista_preco.append('25')
            total+=valor
            saldoemp += valor
            wait()
        case '2':
            print(TerminalColors.AZUL + 'Show de confeção de cocktail' + TerminalColors.ENDC)
            valor=10
            qt = 1
            print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
            lista_qt.append(qt)
            lista_item.append('Show Cocktail')
            lista_preco.append('10')
            total+=valor
            saldoemp += valor 
            wait()
        case '3':
            print(TerminalColors.AZUL + 'Mesas (10 unidades)' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos packs quer?' + TerminalColors.ENDC)
            if qt.isdigit():
                if lista_stocks and int(qt) > int(lista_stocks[0]):
                    print(TerminalColors.VERMELHO + "Nao ha stock suficiente" + TerminalColors.ENDC)
                else:
                    valor=50*int(qt)
                    print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                    #wait()
                    lista_qt.append(qt)
                    lista_item.append('Mesas')
                    lista_preco.append('50')
                
                    lista_stocks[0] = str(int(lista_stocks[0]) - int(qt))
                    def_wstocks()
                    total+=valor
                    saldoemp += valor 
                    wait()
        case '4':
            print(TerminalColors.AZUL + 'Toalhas de mesa (10 unidades)' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos packs quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stocks[1]):
                print(TerminalColors.VERMELHO + "Nao ha stock suficiente" + TerminalColors.ENDC)
            else:
                valor=20*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)    
                lista_qt.append(qt)
                lista_item.append('Toalhas')
                lista_preco.append('20')
                if qt.isdigit():
                    lista_stocks[1] = str(int(lista_stocks[1]) - int(qt))
                    def_wstocks()
                total+=valor
                saldoemp += valor
                wait()
        case '5':
            print(TerminalColors.AZUL + 'Entrega de comida' + TerminalColors.ENDC)
            valor=10

            print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)    
            total+=valor
            lista_qt.append('1')
            lista_item.append('Entrega de comida')
            lista_preco.append('10')
            saldoemp += valor
            wait()
            
            
        case '6':
            print(TerminalColors.AZUL + 'Dedicatória de música' + TerminalColors.ENDC)
            valor=50
            qt=1
            print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
            total+=valor 
            lista_qt.append(qt)
            lista_item.append('Musica')
            lista_preco.append('50')
            saldoemp += valor
            wait()
            import musicplayer
            import subprocess
            musicplayer.root.mainloop()
            #subprocess.run(["python", "musiclplayer.py"])
            def_main()

            
        case '7':
            print(TerminalColors.AZUL + 'Escolheu Cartão presente Refeição (30 d)' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stocks[2]):
                print(TerminalColors.VERMELHO + "Nao ha stock suficiente" + TerminalColors.ENDC)
            else:
                valor=500*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append('Cartão 30d')
                lista_preco.append('500$')
                if qt.isdigit():
                    lista_stocks[2] = str(int(lista_stocks[2]) - int(qt))
                    def_wstocks()
                total+=valor
                saldoemp += valor
                wait()
        case '8':
            print(TerminalColors.AZUL + 'Escolheu Cartão presente Refeição (10 d)' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos quer?' + TerminalColors.ENDC)
            if int(qt) > int(lista_stocks[3]):
                print(TerminalColors.VERMELHO + "Nao ha stock suficiente" + TerminalColors.ENDC)
            else:
                valor=220*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append('Cartão 10d')
                lista_preco.append('220$')
                if qt.isdigit():
                    lista_stocks[3] = str(int(lista_stocks[3]) - int(qt))
                    def_wstocks()
                total+=valor
                saldoemp += valor
                wait()
        case '9':
            print(TerminalColors.AZUL + 'Escolheu Cartão presente Refeição (7 d)' + TerminalColors.ENDC)
            qt=input(TerminalColors.CINZENTO + 'Quantos quer?' + TerminalColors.ENDC) 
            if int(qt) > int(lista_stocks[4]):
                print(TerminalColors.VERMELHO + "Nao ha stock suficiente" + TerminalColors.ENDC)
            else:
                valor=200*int(qt)
                print(TerminalColors.AMARELO + f'O preço é {valor}' + TerminalColors.ENDC)
                lista_qt.append(qt)
                lista_item.append('Cartão 7d')
                lista_preco.append('200$')
                if qt.isdigit():
                    lista_stocks[4] = str(int(lista_stocks[4]) - int(qt))
                    def_wstocks()
                total+=valor
                saldoemp += valor
                wait()
        case '10':
            print(TerminalColors.AZUL + "A voltar para o menu anterior..." + TerminalColors.ENDC)
            def_main()
        case _:
            print(TerminalColors.VERMELHO + "Escolha não encontrada" + TerminalColors.ENDC)
            
def def_stockmc():
    global mc
    global saldoemp
    global valor
    if lista_stockmc[mc] == lista_stockc[mc]:
        print(TerminalColors.VERMELHO + "Já esta com o stock maximo" + TerminalColors.ENDC)
        wait()
    else:
        qtm = str(int(lista_stockmc[mc]) - int(lista_stockc[mc]))
        lista_stockc[mc] = str(int(lista_stockc[mc]) + int(qtm))
        valor = int(qtm) * 5
        saldoemp = int(saldoemp) - int(valor)
        print(TerminalColors.VERDE + "Stock novamente ao maximo" + TerminalColors.ENDC)
        def_wstockc()
        reg_saldo()
def def_stockmb():
    global mb
    global saldoemp
    global valor
    if lista_stockmb[mb] == lista_stockb[mb]:
        print(TerminalColors.AZUL + "Já esta com o stock maximo" + TerminalColors.ENDC)
    else:
        qtm = str(int(lista_stockmb[mb]) - int(lista_stockb[mb]))
        lista_stockb[mb] = str(int(lista_stockb[mb]) + int(qtm))
        valor = int(qtm) * 5
        saldoemp = int(saldoemp) - int(valor)
        print(TerminalColors.VERDE + "Stock novamente ao maximo" + TerminalColors.ENDC)
        def_wstockb()
        reg_saldo()
     
def def_stockms():
    global ms
    global saldoemp
    global valor
    if lista_stockms[ms] == lista_stocks[ms]:
        print(TerminalColors.AZUL + "Já esta com o stock maximo" + TerminalColors.ENDC)
    else:
        qtm = str(int(lista_stockms[ms]) - int(lista_stocks[ms]))
        lista_stocks[ms] = str(int(lista_stocks[ms]) + int(qtm))
        valor = int(qtm) * 5 #5 custo da mercadoria
        saldoemp = int(saldoemp) - int(valor)
        print(TerminalColors.VERDE + "Stock novamente ao maximo" + TerminalColors.ENDC)
        reg_saldo()
        def_wstocks()
        
def def_apresentarstock():
    def_read_stockc()
    def_read_stockb()
    def_read_stocks()
    def_sempreco()
    for j, p in zip(lista_comidap, lista_stockc):
        print(f"Tem {p} de {j}")
    wait()
    for j, p in zip(lista_bebidasp, lista_stockb):
        print(f"Tem {p} de {j}")
    wait()
    for j, p in zip(lista_servicosp, lista_stocks):
        print(f"Tem {p} de {j}")
    wait()
def def_stock():
    global mc
    global mb
    global ms
    def_stockm()
    def_sempreco()
    print(TerminalColors.VERDE + "1-Stock Comida" + TerminalColors.ENDC)
    print(TerminalColors.AZUL + "1-Stock Bebidas" + TerminalColors.ENDC)
    print(TerminalColors.AMARELO + "3-Stock Serviços" + TerminalColors.ENDC)
    print(TerminalColors.CINZENTO + "4-Verificar Stock Existente" + TerminalColors.ENDC)
    opcao = input(TerminalColors.VERMELHO + "Digite a opção desejada ou sair para encerrar o programa\n" + TerminalColors.ENDC)
    match opcao:
        case '1':
            print(TerminalColors.VERDE + "Stock comida" + TerminalColors.ENDC)
            def_read_stockc()
            def_graficosc()
            opc = input(TerminalColors.CINZENTO + "Que comida quer repor: " + TerminalColors.ENDC)
            match opc:
                case '1':
                    mc = 0
                    def_stockmc()
                case '2':
                    mc = 1
                    def_stockmc()
                case '3':
                    mc = 2
                    def_stockmc()
                case '4':
                    mc = 3
                    def_stockmc()
                case '5':
                    mc = 4
                    def_stockmc()
                case '6': 
                    mc = 5
                    def_stockmc()
                case '7':
                    mc = 6
                    def_stockmc()
                case '8':
                    mc = 7
                    def_stockmc()
                case '9':
                    mc = 8
                    def_stockmc()
                case '10':  
                    mc = 9
                    def_stockmc()
        case '2':
            print(TerminalColors.AZUL + "Stock bebidas" + TerminalColors.ENDC)
            def_graficosb()
            opc = input(TerminalColors.CINZENTO + "Que bebida quer repor: " + TerminalColors.ENDC)
            match opc:
                case '1':
                    mb = 0 
                    def_stockmb()
                case '2':
                    mb = 1
                    def_stockmb()
                case '3':
                    mb = 2 
                    def_stockmb()
                case '4':
                    mb = 3 
                    def_stockmb()
                case '5':
                    mb = 4 
                    def_stockmb()
                case '6':
                    mb = 5 
                    def_stockmb()
                case '7':
                    mb = 6 
                    def_stockmb()
                case '8':                     
                    mb = 7 
                    def_stockmb()
                case '9':
                    mb = 8 
                    def_stockmb()
                case '10':
                    mb = 9 
                    def_stockmb()
                case '11':                     
                    mb = 10 
                    def_stockmb()
                case '12':                     
                    mb = 11 
                    def_stockmb()
                case '13':
                    mb = 12 
                    def_stockmb()
                case '14':
                    mb = 13     
                    def_stockmb()
                case '15':
                    mb = 14 
                    def_stockmb()
        case '3':
            print(TerminalColors.AMARELO + "Stock serviços" + TerminalColors.ENDC)
            def_graficoss()
            opc = input(TerminalColors.CINZENTO + "Que serviços quer repor: " + TerminalColors.ENDC)
            match opc:
                case '1':
                    ms = 0  
                    def_stockms()
                case '2':                     
                    ms = 1 
                    def_stockms()
                case '3':                     
                    ms = 2 
                    def_stockms()
                case '4':                     
                    ms = 3 
                    def_stockms()
                case '5':                     
                    ms = 4 
                    def_stockms()
        case '4':
            def_apresentarstock()
    


def def_staff():
    global qtf
    global totsal
    global nomec,idadec,cargoc,exp,delete
    #lista_candidaturas = []
    #rcandidaturas()
    #def_read_func()
    while True:
        print(TerminalColors.ROXO + "Menu Staff" + TerminalColors.ENDC)
        print(TerminalColors.VERDE + "1-Adicionar funcionarios" + TerminalColors.ENDC)
        print(TerminalColors.AMARELO + "2-Gestão de funcionarios" + TerminalColors.ENDC)
        print(TerminalColors.AZUL + "3-Verificar saldo da empresa" + TerminalColors.ENDC)
        print(TerminalColors.ROSA + "4-Ver candidaturas" + TerminalColors.ENDC)
        print("5-Atualizar stock")
        print(TerminalColors.VERMELHO + "6-Voltar" + TerminalColors.ENDC)
        opc = input(TerminalColors.CINZENTO + "Digite a opção desejada: " + TerminalColors.ENDC)
        match opc:
            case '1':
                nome = input(TerminalColors.VERDE + "Qual e o nome do funcionario" + TerminalColors.ENDC)
                print("1-Gerente de loja")
                print("2-Gerente")
                print("3-Cozinheiro")
                print("4-Chefe de cozinha")
                print("5-Chefe de sala")
                print("6-Funcionario")
                funcao = input(TerminalColors.CINZENTO + "Digite a opção" + TerminalColors.ENDC)
                os.system("cls" if os.name == "nt" else "clear")
                match funcao:
                    case '1':
                        cargo = 'Gerente de loja'
                        registar_funcionarios(nome,cargo)
                    case '2':
                        cargo = 'Gerente'
                        registar_funcionarios(nome,cargo)
                    case '3':
                        cargo = 'Cozinheiro'
                        registar_funcionarios(nome,cargo)
                    case '4':
                        cargo = 'Chefe de cozinha'
                        registar_funcionarios(nome,cargo)
                    case '5':
                        cargo = 'Chefe de sala'
                        registar_funcionarios(nome,cargo)
                    case '6':
                        cargo = 'Funcionario'
                        registar_funcionarios(nome,cargo)
                wait()
            case '2':
            
                print(TerminalColors.AMARELO + "Gestão de funcionarios" + TerminalColors.ENDC)
                def_read_func()
                for k in lista_funcionarios:
                    qtf+=1
                    print(k)
                print(TerminalColors.AZUL + f"A empresa atualmente tem: {qtf}" + TerminalColors.ENDC) 
                dec = input(TerminalColors.VERDE + "Quer fazer o pagamento dos salários? S/N:" + TerminalColors.ENDC)
                if dec == 'S' or dec == "SIM" or dec == "sim" or dec == "s":
                    def_pags()
                    qtf = 0
                else:
                    print(TerminalColors.VERMELHO + "Pagamento nao efetuado" + TerminalColors.ENDC)
                    qtf = 0
                wait()
            case '3':
                print(TerminalColors.AZUL + "O saldo da empresa é o seguinte: ",saldoemp)
                wait()
            case '4':
                    cont=-1
                    for candidatura in lista_candidaturas2:
                        print(candidatura)
                        esc = input(TerminalColors.ROSA + "Quer contratar?: " + TerminalColors.ENDC)
                        cont=cont+1
                        if esc.lower() in ['s', 'sim']:
                            
                            nome, cargo, idade, exp = lista_candidaturas[cont]
                            registar_funcionarios(nome, cargo)
                            delete_linha(candidatura)
                            delete_linha2(candidatura)
                        else:
                            delete_linha(candidatura)
                            delete_linha2(candidatura)
                    wait()
                # Convertendo a lista para uma string para deletar no arquivo
                
                
                # Chamando a função delete_linha com os argumentos corretos
                
            case '5':
                def_stock()
                wait()
            case '6':
                os.system("cls" if os.name == "nt" else "clear")
                def_main()


def candidaturas():
    global nomec,idadec,cargoc,exp
    nomec = input(TerminalColors.AZUL + "Qual é o seu nome: " + TerminalColors.ENDC)
    os.system("cls" if os.name == "nt" else "clear")
    idadec = input(TerminalColors.AMARELO + "Qual é a sua idade: " + TerminalColors.ENDC)
    os.system("cls" if os.name == "nt" else "clear")
    exp = input(TerminalColors.VERDE + "Qual é a sua experiencia na area (0 a 10): " + TerminalColors.ENDC)
    if exp.isdigit():
        os.system("cls" if os.name == "nt" else "clear")
        print("1-Gerente de loja")
        print("2-Gerente")
        print("3-Cozinheiro")
        print("4-Chefe de cozinha")
        print("5-Chefe de sala")
        print("6-Funcionario")
        cargoc = input(TerminalColors.ROSA + "Qual é o seu cargo que se deseja candidatar: " + TerminalColors.ENDC)
        os.system("cls" if os.name == "nt" else "clear")
        if cargoc == '1':
            cargoc = 'Gerente de loja'
        elif cargoc == '2':
            cargoc = 'Gerente'
        elif cargoc == '3':
            cargoc = 'Cozinheiro'
        elif cargoc == '4':
            cargoc = 'Chefe de cozinha'
        elif cargoc == '5':
            cargoc = 'Chefe de sala'
        elif cargoc == '6':
            cargoc = 'Funcionario'
        else:
            print(TerminalColors.VERMELHO + "Escolha invalida" + TerminalColors.ENDC)
            candidaturas()
    else:
        print(TerminalColors.VERMELHO + "A experiencia indicada nao e um numero" + TerminalColors.ENDC)

    registar_candidaturas()
    reg_cand2()
    
def def_main():
    while True:
        global ps,total
        rcandidaturas()
        rcandidaturas2()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(current_time)
        print('Bem vindo ao nosso menu')
        print(TerminalColors.VERDE + '1-Comida' + TerminalColors.ENDC)
        print(TerminalColors.AZUL + '2-Bebida' + TerminalColors.ENDC)
        print(TerminalColors.AMARELO + '3-Serviço' + TerminalColors.ENDC)
        print(TerminalColors.ROSA + '4-Pagar' + TerminalColors.ENDC)
        print(TerminalColors.CINZENTO + '5-Talões' + TerminalColors.ENDC)
        #print(TerminalColors.ROXO + '6-Area staff' + TerminalColors.ENDC)
        print(TerminalColors.ROXO + '6-Reservas' + TerminalColors.ENDC)
        print('7-Trabalha connosco')
        print(TerminalColors.VERMELHO + '8-Sair' + TerminalColors.ENDC)
        opcao = input("Digite a opção desejada ou sair para encerrar o programa\n")
        if opcao == 'staff' or opcao == 'Staff':
            print("A entrar na área staff")
            opcao = '99'
        match opcao:
            case '1':
                print(TerminalColors.VERDE + 'Menu de Comida' + TerminalColors.ENDC)
                os.system("cls" if os.name == "nt" else "clear")
                for i in lista_comida:
                    print(i)
                
                def_comida()
            case '2':
                print(TerminalColors.AZUL + 'Menu de Bebidas' + TerminalColors.ENDC)
                os.system("cls" if os.name == "nt" else "clear")
                for i in lista_bebidas:
                    print(i)
                def_bebidas()
            case '3':
                print(TerminalColors.AMARELO + 'Servicos' + TerminalColors.ENDC)
                os.system("cls" if os.name == "nt" else "clear")
                for i in lista_servicos:
                    print(i)
                print("10-Voltar")
                def_servicos()           
            case '4':
                print(TerminalColors.ROSA + "Pagamento" + TerminalColors.ENDC)
                os.system("cls" if os.name == "nt" else "clear")
                def_pagamento()
            case '5':
                print(TerminalColors.CINZENTO + "Taloes" + TerminalColors.ENDC)
                os.system("cls" if os.name == "nt" else "clear")
                def_mostrartalao()
            case '6':
                print(TerminalColors.ROXO + 'Reservas' + TerminalColors.ENDC)
                os.system("cls" if os.name == "nt" else "clear")
                def_reserva()
            case '7':
                candidaturas()
            case '8':
                if total == 0:
                    print("Volte Sempre!")
                    exit(0)
                else:
                    if ps == 1:
                            def_pagamento()
                            print(TerminalColors.VERMELHO + 'Volte sempre!' + TerminalColors.ENDC)
                            exit(0)
            case '99':
                print(TerminalColors.ROXO + 'Area da staff' + TerminalColors.ENDC)
                os.system("cls" if os.name == "nt" else "clear")
                def_login()
            case _:
                print(TerminalColors.VERMELHO + "Escolha não encontrada" + TerminalColors.ENDC)
def_main()