"""Importamos todos los paquetes a utilizar, puede referirse a 
setup.py para informacion de los modulos utilizados."""

from random import randrange
import numpy as np
import pandas as pd
import datetime as dt
import pyttsx3

# Iniciamos el motor de speech y se estable la velocidad del habla
speaker = pyttsx3.init()
speaker.setProperty("rate", 130)

class Practice(object):
    """La clase Practice contiene las variables relacionadas a las palabras
    que el estudiante ha aprendido, almacena las palabras que conforman 
    la lista para aprender, las notas obtenidas en cada nivel de juego,
    el resultado final de la sesion y las variables intermedias de cada proceso.
    
    """
    def __init__(self, doc_ref):
        self.banks = {1:"/docs/Word_list.xlsx", 2:"docs/Word_list2.xlsx"}
        self.L6 = []
        self.download = abrir(self.banks.get(int(doc_ref)))
        self.words = download(self.download)
        self.nota = []
        self.final = []
        self.results = {
            "L1":[0,0],"L2":[0,0],"L3":[0,0],"L4":[0,0],"L5":[0,0]
            }

    def working(self, answer, results, words):
        if not("alto" in answer):
            if len(words[4]) >= 150:
                print("\t\t Nivel 5\n")
                results["L5"] = engine(words[4], self.L6, words[3],results["L5"])
                answer = input("\tEscribe 'alto' si quieres terminar: ")
                self.working(answer, results, words)
            elif len(words[3]) >= 125:
                print("\t\t Nivel 4\n")
                results["L4"] = engine(words[3], words[4], words[2],results["L4"])
                answer = input("\tEscribe 'alto' si quieres terminar: ")
                self.working(answer, results, words)
            elif len(words[2]) >= 100:
                print("\t\t Nivel 3\n")
                results["L3"] = engine(words[2], words[3], words[1],results["L3"])
                answer = input("\tEscribe 'alto' si quieres terminar: ")
                self.working(answer, results, words)
            elif len(words[1]) >= 75:
                print("\t\t Nivel 2\n")
                results["L2"] = engine(words[1], words[2], words[0],results["L2"])
                answer = input("\tEscribe 'alto' si quieres terminar: ")
                self.working(answer, results, words)
            elif len(words[0]) >= 50:
                print("\t\t Nivel 1\n")
                results["L1"] = engine(words[0], words[1], words[0],results["L1"])
                answer = input("\tEscribe 'alto' si quieres terminar: ")
                self.working(answer, results, words)
            else:
                for i in self.download:
                    if int(i[3]) == 0:
                        if len(self.words[0]) < 50:
                            self.words[0].append(i)
                            self.working(answer, results, words)
                        else:
                            print("Repeticion de metodo working por nivel 1 mayor a 50")
                            self.working(answer, results, words)
                    else:
                        print("En la lista de palabras no hay mas palabras nuevas")
                        
        else:
            for value in results:
                if results[value] != [0,0]:
                    self.nota.append(round((results[value][0]/ np.asarray(results[value]).sum())*100))
                else:
                    self.nota.append(0.0)
            c = 0
            n = 0
            for i in self.nota:
                if i != 0.0:
                    c += i
                    n +=1
                else:
                    pass        

            self.final = words[0] + words[1] + words[2] + words[3] + words[4] + words[5] + words[6] + words[7] + words[8] + words[9]
            print("\tTu resultado es: ", round(c/n), "de 100\n")
            if self.L6 != []:
                print("\tFelicidades! Las palabras que has aprendido son: ", self.L6)
            guardar(self.final, self.nota, round(c/n))


def download(lista):
    """Distribucion de todas las palabras en listas para trabajar."""
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
                L5.append(i) 
            else:
                l5.append(i)
        else:
            i[3] = 5
            lista.remove(i)
    
    return [L1,L2,L3,L4,L5,l1,l2,l3,l4,l5]

def engine(lista_inicial, lista_avance,lista_retraso, dict_resul):
    """Realiza la dinamica de estudio """
    vueltas = len(lista_inicial)    
    for i in range(vueltas):
        n = randrange(0, len(lista_inicial))
        word = lista_inicial.pop(n)
        speaker.say(word[0])
        speaker.runAndWait()
        print(f"\t{i+1}) Write the translate for: {word[0]}")
        key = input("\tTraduccion: > ").lower()
        if key == word[1]:
            print("""\tEs correcto.""")
            if str(word[2]) != "nan":
                print("\tOtra traduccion es: ", word[2])
            else:
                pass
            dict_resul[0] += 1
            word[3] += 1
            lista_avance.append(word)
            input()
        elif key == word[2] and str(word[2]) != "nan":
            print("\tEs correcto.")
            print("\tOtra traduccion es: ", word[1])
            dict_resul[0] += 1
            word[3] += 1
            lista_avance.append(word)
            input()
        else:
            if str(word[2]) != "nan":
                print("\tTe equivocaste, la traduccion es: ", word[1]," o ", word[2])
            else:
                print("\tTe equivocaste, la traduccion es: ", word[1])
                
            dict_resul[1] += 1
            lista_retraso.append(word)
            if word[3] == 0:
                pass
            else:
                word[3] -= 1
            input()
    return dict_resul

def abrir(documento):
    """Abre el archivo excel y lo transforma en una lista"""
    Dict = pd.read_excel(documento, index_col="ID")
    Dict.fillna("")
    return Dict.values.tolist()

def guardar(lista, resultados, final):
    df_lista = pd.DataFrame(lista)
    df_lista.to_excel(self.banks.get(int(doc_ref)),index_label="ID")
    dfr = pd.read_excel("docs/Resultados.xlsx", index_col="Fecha")
    resul = [[pd.to_datetime(dt.date.today()), resultados[0], resultados[1], resultados[2], resultados[3], resultados[4],final]]
    inter_df = pd.DataFrame(resul, columns = ["Fecha","Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Final"])
    inter_df = inter_df.set_index("Fecha")
    dfr = dfr.append(inter_df)
    dfr.to_excel("docs/Resultados.xlsx")
    print("\tGuardado tus resutados con exito")
