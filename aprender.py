from vocabulario.classes import Practice

print("""\n\t\t Bienvenid@s aprendices al juego de Leitner.\n
\t Tienes como objetivo aprender palabras en ingles, es hora de proceder,
\tcomienza eligiendo que lista de palabras quieres estudiar en esta sesion,
\tte recuerdo que esta es una opcion temporal, eventualmente solo sera una sola.""")
input()

# Definimos la funcion para iniciar el sistema
def start():
    """Funci\'on para inicio del sistema"""
    doc_ref = input("\tIngresa 1 para la primera lista o 2 para la segunda: > ")
    # Comprueba que la informacion ingresada sea la apropiada
    try:
        int(doc_ref)
    except:
        doc_ref = 0
    # Una vez determinada la informacion ingresada, se procede a iniciar el sistema
    if int(doc_ref) in [1,2]:
        Student = Practice(doc_ref)
        Student.working("", Student.results, Student.words) 
    else:
        print("\n\tTu valor ingresado no es valido, prueba otra vez.\n")
        start()

start()