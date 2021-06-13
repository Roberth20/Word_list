import pyttsx3
from random import randint
import numpy as np
import pandas as pd

speaker = pyttsx3.init()
speaker.setProperty("rate", 130)

Dict = pd.read_excel("Word_list.xlsx", index_col=0)
Dict.fillna("")
QA = Dict.values.tolist()

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

for i in QA:
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
        QA.remove(i)             

def engine(lista_inicial, lista_avance,lista_retraso, positivo=0, negativo=0):
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

A = ""
resultados = ["","","",0,0]
L6 = []
while A != "suficiente por hoy":
    if len(L5) >= 150:
        resultados = engine(L5, L6, L4,resultados[3],resultados[4])
        A = input("Escribe 'suficiente por hoy' si quieres terminar: ")
    elif len(L4) >= 125:
        resultados = engine(L4, L5, L3,resultados[3],resultados[4])
        A = input("Escribe 'suficiente por hoy' si quieres terminar: ")
    elif len(L3) >= 100:
        resultados = engine(L3, L4, L2,resultados[3],resultados[4])
        A = input("Escribe 'suficiente por hoy' si quieres terminar: ")
    elif len(L2) >= 75:
        resultados = engine(L2, L3, L1,resultados[3],resultados[4])
        A = input("Escribe 'suficiente por hoy' si quieres terminar: ")
    elif len(L1) >= 50:
        resultados = engine(L1, L2, L1,resultados[3],resultados[4])
        A = input("Escribe 'suficiente por hoy' si quieres terminar: ")
    else:
        for i in QA:
            if int(i[3]) == 0:
                if len(L1) < 50:
                    L1.append(i) 
                else:
                    pass
            else:
                pass
            

nota = ((resultados[3]) / (resultados[3] + resultados[4])) * 100
		
print("Tu resultado es: ", round(nota), "de 100")
print("Felicidades! Las palabras que has aprendido son: ", L6)

Final = L1 + L2 + L3 + L4 + L5 + l1 + l2 + l3 + l4 + l5
df = pd.DataFrame(Final)
df.to_excel("Word_list0.xlsx")
print("Guardado tus resutados con exito")