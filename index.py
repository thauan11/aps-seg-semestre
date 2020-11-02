import os
import csv
from time import sleep
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
from prettytable import from_csv
from prettytable import PrettyTable
from prettytable import from_csv
os.system("cls")

table = PrettyTable

#ORDENA O ARQUIVO USANDO SELECTION SORT
def selection_sort(dicionario, index_to_sort):
    n = len(dicionario)
    for i in range(n-1):
        min_index = i
        for j in range(i, n):
            if dicionario.get(j)[index_to_sort] < dicionario.get(min_index)[index_to_sort]:
                min_index = j
        if dicionario.get(i)[index_to_sort] > dicionario.get(min_index)[index_to_sort]:
            dicionario[i], dicionario[min_index] = dicionario[min_index], dicionario[i]

#ORDENA EM ORDEM DECRESCENTE USANDO SELECTION SORT
def reverso_selection_sort(dicionario, index_to_sort):
    n = len(dicionario)
    for i in range(n-1):
        min_index = i
        for j in range(i, n):
            if dicionario.get(j)[index_to_sort] > dicionario.get(min_index)[index_to_sort]:
                min_index = j
        if dicionario.get(i)[index_to_sort] < dicionario.get(min_index)[index_to_sort]:
            dicionario[i], dicionario[min_index] = dicionario[min_index], dicionario[i]

#TRANSFORMA NUMEROS EM INTEIROS
def converte_int(dicionario, index):
    for i in dicionario:
        dicionario.get(i)[index] = int(dicionario.get(i)[index])

#FUNÇÃO PARA SIMULAR O APLICATIVO PENSANDO
def aguarde():
    sleep(1)
    print("Organizando arquivo, por favor aguarde.")
    sleep(1)
    print("Gerando arquivo ordenado em...")
    for i in range (3,0,-1):
        sleep(1)
        print(i)
    print()
    print("Arquivo organizado!" + "\n")
    sleep(0.5)

#CRIA ORDENAÇÃO ALFABETICA
def ordenacao():
    os.system("cls")
    print("DADOS ORDENATIVOS")
    print("           0 para VOLTAR")
    print("1 para NOME PACIENTE")
    print("2 para IDADE DO PACIENTE")
    print("3 para CPF DO PACIENTE")
    print("4 para MÉDICO")
    print("5 para EXAME" + "\n")
    ond_ordena = input("Qual coluna deseja ordenar? ")
    print("")

    while ond_ordena != "0":
        #NOME
        if ond_ordena == "1":
            print("TIPOS DE ORDEM:")
            print("1 para ordem CRESCENTE")
            print("2 para ordem DECRESCENTE")
            resposta = input("Opção escolhida: ") 
            print("")

            if resposta == "1":
                nomes_file = open('fichas.csv',"r")
                linhas = nomes_file.readlines()

                dicionario = {}

                for i in range(len(linhas)-1):
                    dicionario[i] = linhas[i+1].replace("\n",'')

                #converte_float(dicionario,2)
                selection_sort(dicionario,0)

                aguarde()

                saida_file = open('fichas_ordenadas.csv', 'w')
                saida_file.write(linhas[0])

                for k, v in dicionario.items():
                    saida_file.write(str(v).replace('[','').replace(']','').replace(',',';').replace("'",'') + "\n")
                
                saida_file.close()
                nomes_file.close()
                
                print("1 para VISUALIZAR a lista ORDENADA")
                print("2 para CONTINUAR")
                printar = input("Insira oque deseja fazer: ")
                print("")

                while printar != "2":
                    if printar == "1": 
                        ao = open("fichas_ordenadas.csv", "r")
                        x = from_csv(ao)
                        print(x)
                        print("")
                        ao.close()
                        break
                    elif printar == "2":
                        break
                    else:
                        print("1 para VISUALIZAR a lista ORDENADA")
                        print("2 para CONTINUAR")
                        printar = input("Insira oque deseja fazer: ")
                        print("")   
                break

            elif resposta == "2":
                nomes_file = open('fichas.csv')
                linhas = nomes_file.readlines()

                dicionario = {}

                for i in range(len(linhas)-1):
                    dicionario[i] = linhas[i+1].replace("\n",'').split(';')

                #converte_float(dicionario,2)
                reverso_selection_sort(dicionario,0)

                aguarde()

                saida_file = open('fichas_ordenadas.csv', 'w')
                saida_file.write(linhas[0])

                for k, v in dicionario.items():
                    saida_file.write(str(v).replace('[','').replace(']','').replace(',',';').replace("'",'') + "\n")
                
                saida_file.close()
                nomes_file.close()
                
                print("1 para VISUALIZAR a lista ORDENADA")
                print("2 para CONTINUAR")
                printar = input("Insira oque deseja fazer: ")
                print("")

                while printar != "2":
                    if printar == "1": 
                        ao = open("fichas_ordenadas.csv", "r")
                        x = from_csv(ao)
                        print(x)
                        print("")
                        ao.close()
                        break
                    elif printar == "2":
                        break
                    else:
                        print("1 para VISUALIZAR a lista ORDENADA")
                        print("2 para CONTINUAR")
                        printar = input("Insira oque deseja fazer: ")
                        print("")   
                break

            else:
                break

        #IDADE
        elif ond_ordena == "2":
            print("TIPOS DE ORDEM:")
            print("1 para ordem CRESCENTE")
            print("2 para ordem DECRESCENTE")
            resposta = input("Opção escolhida: ")  
            print("")

            if resposta == "1":
                nomes_file = open('fichas.csv')
                linhas = nomes_file.readlines()

                dicionario = {}

                for i in range(len(linhas)-1):
                    dicionario[i] = linhas[i+1].replace("\n",'').split(';')

                converte_int(dicionario,1)
                selection_sort(dicionario,1)

                aguarde()

                saida_file = open('fichas_ordenadas.csv', 'w')
                saida_file.write(linhas[0])

                for k, v in dicionario.items():
                    saida_file.write(str(v).replace('[','').replace(']','').replace(',',';').replace("'",'') + "\n")
                
                saida_file.close()
                nomes_file.close()
                
                print("1 para VISUALIZAR a lista ORDENADA")
                print("2 para CONTINUAR")
                printar = input("Insira oque deseja fazer: ")
                print("")

                while printar != "2":
                    if printar == "1": 
                        ao = open("fichas_ordenadas.csv", "r")
                        x = from_csv(ao)
                        print(x)
                        print("")
                        ao.close()
                        break
                    elif printar == "2":
                        break
                    else:
                        print("1 para VISUALIZAR a lista ORDENADA")
                        print("2 para CONTINUAR")
                        printar = input("Insira oque deseja fazer: ")
                        print("")   

                break

            elif resposta == "2":
                nomes_file = open('fichas.csv')
                linhas = nomes_file.readlines()

                dicionario = {}

                for i in range(len(linhas)-1):
                    dicionario[i] = linhas[i+1].replace("\n",'').split(';')

                converte_int(dicionario,1)
                reverso_selection_sort(dicionario,1)

                aguarde()

                saida_file = open('fichas_ordenadas.csv', 'w')
                saida_file.write(linhas[0])

                for k, v in dicionario.items():
                    saida_file.write(str(v).replace('[','').replace(']','').replace(',',';').replace("'",'') + "\n")
                
                saida_file.close()
                nomes_file.close()
                
                print("1 para VISUALIZAR a lista ORDENADA")
                print("2 para CONTINUAR")
                printar = input("Insira oque deseja fazer: ")
                print("")

                while printar != "2":
                    if printar == "1": 
                        ao = open("fichas_ordenadas.csv", "r")
                        x = from_csv(ao)
                        print(x)
                        print("")
                        ao.close()
                        break
                    elif printar == "2":
                        break
                    else:
                        print("1 para VISUALIZAR a lista ORDENADA")
                        print("2 para CONTINUAR")
                        printar = input("Insira oque deseja fazer: ")
                        print("")   
                break

            else:
                break

        #CPF
        elif ond_ordena == "3":
            print("TIPOS DE ORDEM:")
            print("1 para ordem CRESCENTE")
            print("2 para ordem DECRESCENTE")
            resposta = input("Opção escolhida: ")  
            print("")

            if resposta == "1":
                nomes_file = open('fichas.csv')
                linhas = nomes_file.readlines()

                dicionario = {}

                for i in range(len(linhas)-1):
                    dicionario[i] = linhas[i+1].replace("\n",'').split(';')

                converte_int(dicionario,2)
                selection_sort(dicionario,2)

                aguarde()

                saida_file = open('fichas_ordenadas.csv', 'w')
                saida_file.write(linhas[0])

                for k, v in dicionario.items():
                    saida_file.write(str(v).replace('[','').replace(']','').replace(',',';').replace("'",'') + "\n")
                
                saida_file.close()
                nomes_file.close()
                
                print("1 para VISUALIZAR a lista ORDENADA")
                print("2 para CONTINUAR")
                printar = input("Insira oque deseja fazer: ")
                print("")

                while printar != "2":
                    if printar == "1": 
                        ao = open("fichas_ordenadas.csv", "r")
                        x = from_csv(ao)
                        print(x)
                        print("")
                        ao.close()
                        break
                    elif printar == "2":
                        break
                    else:
                        print("1 para VISUALIZAR a lista ORDENADA")
                        print("2 para CONTINUAR")
                        printar = input("Insira oque deseja fazer: ")
                        print("")   
                break

            elif resposta == "2":
                nomes_file = open('fichas.csv')
                linhas = nomes_file.readlines()

                dicionario = {}

                for i in range(len(linhas)-1):
                    dicionario[i] = linhas[i+1].replace("\n",'').split(';')

                converte_int(dicionario,2)
                reverso_selection_sort(dicionario,2)

                aguarde()

                saida_file = open('fichas_ordenadas.csv', 'w')
                saida_file.write(linhas[0])

                for k, v in dicionario.items():
                    saida_file.write(str(v).replace('[','').replace(']','').replace(',',';').replace("'",'') + "\n")
                
                saida_file.close()
                nomes_file.close()
                
                print("1 para VISUALIZAR a lista ORDENADA")
                print("2 para CONTINUAR")
                printar = input("Insira oque deseja fazer: ")
                print("")

                while printar != "2":
                    if printar == "1": 
                        ao = open("fichas_ordenadas.csv", "r")
                        x = from_csv(ao)
                        print(x)
                        print("")
                        ao.close()
                        break
                    elif printar == "2":
                        break
                    else:
                        print("1 para VISUALIZAR a lista ORDENADA")
                        print("2 para CONTINUAR")
                        printar = input("Insira oque deseja fazer: ")
                        print("")   
                break

            else:
                break

        #MEDICO
        elif ond_ordena == "4":
            print("TIPOS DE ORDEM:")
            print("1 para ordem CRESCENTE")
            print("2 para ordem DECRESCENTE")
            resposta = input("Opção escolhida: ")  
            print("")

            if resposta == "1":
                nomes_file = open('fichas.csv')
                linhas = nomes_file.readlines()

                dicionario = {}

                for i in range(len(linhas)-1):
                    dicionario[i] = linhas[i+1].replace("\n",'').split(';')

                #onverte_int(dicionario,2)
                selection_sort(dicionario,5)

                aguarde()

                saida_file = open('fichas_ordenadas.csv', 'w')
                saida_file.write(linhas[0])

                for k, v in dicionario.items():
                    saida_file.write(str(v).replace('[','').replace(']','').replace(',',';').replace("'",'') + "\n")
                
                saida_file.close()
                nomes_file.close()
                
                print("1 para VISUALIZAR a lista ORDENADA")
                print("2 para CONTINUAR")
                printar = input("Insira oque deseja fazer: ")
                print("")

                while printar != "2":
                    if printar == "1": 
                        ao = open("fichas_ordenadas.csv", "r")
                        x = from_csv(ao)
                        print(x)
                        print("")
                        ao.close()
                        break
                    elif printar == "2":
                        break
                    else:
                        print("1 para VISUALIZAR a lista ORDENADA")
                        print("2 para CONTINUAR")
                        printar = input("Insira oque deseja fazer: ")
                        print("")   
                break

            elif resposta == "2":
                nomes_file = open('fichas.csv')
                linhas = nomes_file.readlines()

                dicionario = {}

                for i in range(len(linhas)-1):
                    dicionario[i] = linhas[i+1].replace("\n",'').split(';')

                #converte_int(dicionario,2)
                reverso_selection_sort(dicionario,5)

                aguarde()

                saida_file = open('fichas_ordenadas.csv', 'w')
                saida_file.write(linhas[0])

                for k, v in dicionario.items():
                    saida_file.write(str(v).replace('[','').replace(']','').replace(',',';').replace("'",'') + "\n")
                
                saida_file.close()
                nomes_file.close()
                
                print("1 para VISUALIZAR a lista ORDENADA")
                print("2 para CONTINUAR")
                printar = input("Insira oque deseja fazer: ")
                print("")

                while printar != "2":
                    if printar == "1": 
                        ao = open("fichas_ordenadas.csv", "r")
                        x = from_csv(ao)
                        print(x)
                        print("")
                        ao.close()
                        break
                    elif printar == "2":
                        break
                    else:
                        print("1 para VISUALIZAR a lista ORDENADA")
                        print("2 para CONTINUAR")
                        printar = input("Insira oque deseja fazer: ")
                        print("")   
                break

            else:
                break

        #EXAME
        elif ond_ordena == "5":
            print("TIPOS DE ORDEM:")
            print("1 para ordem CRESCENTE")
            print("2 para ordem DECRESCENTE")
            resposta = input("Opção escolhida: ") 
            print("")

            if resposta == "1":
                nomes_file = open('fichas.csv')
                linhas = nomes_file.readlines()

                dicionario = {}

                for i in range(len(linhas)-1):
                    dicionario[i] = linhas[i+1].replace("\n",'').split(';')

                #onverte_int(dicionario,2)
                selection_sort(dicionario,6)

                aguarde()

                saida_file = open('fichas_ordenadas.csv', 'w')
                saida_file.write(linhas[0])

                for k, v in dicionario.items():
                    saida_file.write(str(v).replace('[','').replace(']','').replace(',',';').replace("'",'') + "\n")
                
                saida_file.close()
                nomes_file.close()
                
                print("1 para VISUALIZAR a lista ORDENADA")
                print("2 para CONTINUAR")
                printar = input("Insira oque deseja fazer: ")
                print("")

                while printar != "2":
                    if printar == "1": 
                        ao = open("fichas_ordenadas.csv", "r")
                        x = from_csv(ao)
                        print(x)
                        print("")
                        ao.close()
                        break
                    elif printar == "2":
                        break
                    else:
                        print("1 para VISUALIZAR a lista ORDENADA")
                        print("2 para CONTINUAR")
                        printar = input("Insira oque deseja fazer: ")
                        print("")   
                break

            elif resposta == "2":
                nomes_file = open('fichas.csv')
                linhas = nomes_file.readlines()

                dicionario = {}

                for i in range(len(linhas)-1):
                    dicionario[i] = linhas[i+1].replace("\n",'').split(';')

                #converte_int(dicionario,2)
                reverso_selection_sort(dicionario,6)

                aguarde()

                saida_file = open('fichas_ordenadas.csv', 'w')
                saida_file.write(linhas[0])

                for k, v in dicionario.items():
                    saida_file.write(str(v).replace('[','').replace(']','').replace(',',';').replace("'",'') + "\n")
                
                saida_file.close()
                nomes_file.close()
                
                print("1 para VISUALIZAR a lista ORDENADA")
                print("2 para CONTINUAR")
                printar = input("Insira oque deseja fazer: ")
                print("")

                while printar != "2":
                    if printar == "1": 
                        ao = open("fichas_ordenadas.csv", "r")
                        x = from_csv(ao)
                        print(x)
                        print("")
                        ao.close()
                        break
                    elif printar == "2":
                        break
                    else:
                        print("1 para VISUALIZAR a lista ORDENADA")
                        print("2 para CONTINUAR")
                        printar = input("Insira oque deseja fazer: ")
                        print("")   
                break

            else:
                break

        else:
            print("========* ERRO *========")
            print("Local não encontrado")
            ond_ordena = input("Oque deseja fazer: ") 
            print("")

#MENU DE ENTRADA
print("             MENU               ")
print("Digite:")
print("                     0 para SAIR")
print("1 para CONSULTAR OS REGISTROS")
print("2 para CADASTRAR EXAME")
print("3 para PESQUISAR DADO ESPECÍFICO")
print("4 para ORDENAR DADOS")
print(" ")

resp = input("Oque deseja fazer: ")
print(" ")

#OPÇÕES
while resp != "0":
    #IMPRIME TUDO QUE TEM NA FICHA DO PACIENTE
    if resp == "1":
        os.system("cls")
        sleep(0.5)
        
        ficha = open('fichas.csv', "r")
        x = from_csv(ficha)
        x.padding_width = 1
        print(x)
        print(" ")
        
        ficha.close()
    
    #ORDENA O ARQUIVO
    elif resp == "4":
        ordenacao()

    #ADICIONA UMA FRASE SEM APAGAR TODA A FICHA
    elif resp == "2":
        os.system("cls")
        sleep(0.5)
        manipulador = open('fichas.csv', "a")
        manipulador.write("\n")
        texto = input("Insira o nome do paciente: ")
        manipulador.write(texto + ";")
        texto6 = input("Insira a idade do paciente: ")
        manipulador.write(texto6 + ";")
        texto1 = input("Insira o CPF do paciente (11 dígitos): ")
        manipulador.write(texto1 + ";")
        texto2 = input("Insira a data da consulta (00/00/0000): ")
        manipulador.write(texto2 + ";")
        texto3 = input("Insira o horario da consulta (00:00): ")
        manipulador.write(texto3 + ";")
        texto4 = input("Insira o nome do medico: ")
        manipulador.write(texto4 + ";")
        texto5 = input("Insira o nome do exame: ")
        manipulador.write(texto5)
        print(f"Texto adicionado no {manipulador.name}." + "\n")
        manipulador.close()

    #PESQUISA UMA PALAVRA ESPECIFICA NA FICHA DO PACIENTE
    elif resp == "3":
        os.system("cls")
        sleep(0.5)
        contador_linhas = 0
        procurando = input("Oque deseja procurar? ")
        print(" ")
        ficha = csv.reader(open('fichas.csv', "r"), delimiter=";")
        
        #print("NOME   IDADE   CPF   DATA   HORARIO   MEDICO   EXAME")
        for linha in ficha:
            if procurando in linha:
                contador_linhas = contador_linhas + 1
                x = table(linha)
                x.set_style(MSWORD_FRIENDLY)
                print(x)

        print(" ")
        print(f"Foram encontradas {contador_linhas} linhas.")        
        print(" ")

    #TERMINA A WHILE E VOLTA A ABRIR
    else:
        sleep(0.5)
    
    #FICA PERGUNTANDO OQUE O USUARIO QUER FAZER ATÉ ELE SAIR
    print("Digite '0' para sair | '1' para ler | '2' para escrever | '3' para pesquisar | '4' para organizar")
    #print("Digite 'info' caso precise de ajuda")
    print(" ")
    resp = input("Oque deseja fazer: ") 
       
print("Terminando o programa.")
#666