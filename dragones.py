
import random
import time

def mostrarIntroducción():
    print("Esta es una tierra llena de Dragones.")
    print("Frente a ti hay dos cuevas. En una de")
    print("ellas el dragon es generoso, amigable")
    print("y compartira su riquesa contigo.")
    time.sleep(2)
    print("El otro dragon es codicioso, esta hambriento")
    print("y te devorara inmediatamente.")

def elegirCueva():
    cueva = ' '
    while cueva != '1' and cueva != '2':
        print('¿A qué cueva quieres entrar?  ( 1 o 2 )')
        cueva = input()

    return cueva

def explorarCueva(cuevaElegida):
    print('Te aprocimas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print("""¡Un gran dragon aparece subitamente frente a tí!.
Abre sus fauces.""")
    print()
    time.sleep(2)
    cuevaAmigable = random.randint(1, 2)

    if cuevaElegida == str(cuevaAmigable):
        print('¡Te regala su tesoro!')
    else:
        print('!Te engulle de un bocado!')
            
jugarDeNuevo = 'si'
while jugarDeNuevo == 'si' or jugarDeNuevo == 's':

    mostrarIntroducción()

    númeroDeCueva = elegirCueva()

    explorarCueva(númeroDeCueva)

    print('¿Quieres jugar de nuevo? ( sí o no )')
    jugarDeNuevo = input()   
