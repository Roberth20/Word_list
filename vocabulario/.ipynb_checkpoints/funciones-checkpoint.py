from random import randint
import numpy as np
import pandas as pd
import datetime as dt

def download(lista):
    """Distribucion de todas las palabras."""
    L1 = []
    L2 = []
    L3 = []
    L4 = []
    L5 = []
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []

    for i in lista:
        if int(i[3]) == 0:
            if len(L1) < 50:
                L1.append(i) 
            else:
                l1.append(i)
        elif int(i[3]) == 1:
            if len(L2) < 75:
                L2.append(i) 
            else:
                l2.append(i)
        elif int(i[3]) == 2:
            if len(L3) < 100:
                L3.append(i) 
            else:
                l3.append(i)
        elif int(i[3]) == 3:
            if len(L4) < 125:
                L4.append(i) 
            else:
                l4.append(i)
        elif int(i[3]) == 4:
            if len(L1) < 150:
                L1.append(i) 
            else:
                l5.append(i)
        else:
            i[3] = 5
            lista.remove(i)
    
    return [L1,L2,L3,L4,L5,l1,l2,l3,l4,l4,l5]

def engine(lista_inicial, lista_avance,lista_retraso, positivo=0, negativo=0):
    """Realiza la dinamica de estudio"""
    vueltas = len(lista_inicial)
    for i in range(vueltas+1):
        n = randint(0, len(lista_inicial) - 1)
        word = lista_inicial.pop(n)
        speaker.say(word[0])
        speaker.runAndWait()
        print("Numero:",i)
        print("Write the translate for: ", word[0])
        key = input("Traduccion: > ").lower()
        if key == word[1]:
            print("Es correcto.")
            if word[2] != "":
                print("Otra traduccion es: ", word[2])
            else:
                pass
            positivo += 1
            word[3] += 1
            lista_avance.append(word)
            input()
        elif key == word[2] and word[2] != "":
            print("Es correcto.")
            print("Otra traduccion es: ", word[1])
            positivo += 1
            word[3] += 1
            lista_avance.append(word)
            input()
        else:
            print("Te equivocaste, la traduccion es: ", word[1]," o ",word[2])
            negativo += 1
            lista_retraso.append(word)
            if lista_retraso == L1:
                pass
            else:
                word[3] -= 1
            input()
    return [lista_inicial,lista_avance,lista_retraso,positivo,negativo]

def abrir(documento):
    """Abre el archivo excel y lo transforma en una lista"""
    Dict = pd.read_excel(documento, index_col=0)
    Dict.fillna("")
    return Dict.values.tolist()

def guardar(lista, resultados):
    df = pd.DataFrame(lista)
    df.to_excel("docs/Word_list.xlsx")
    dfr = pd.read_excel("docs/Resultados.xlsx")
    listar = dfr.values.tolist()
    resul = [pd.to_datetime(dt.date.today()), resultados]
    listar.append(resul)
    listar.to_excel("docs/Resultados.xlsx")
    print("Guardado tus resutados con exito")
