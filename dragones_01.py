#-*-coding:utf8-*-
#Este aplicativo es un juego en su primera version en python
import random
import time
#defino el intro
def mostrarIntroducción():

    print(''' 
    
 █▀▄ █▀▀▄ ▄▀▄ ▄▀▀░ ▄▀▄ █▄░█ █▀▀ ▄▀▀
 █░█ █▐█▀ █▀█ █░▀▌ █░█ █░▀█ █▀▀ ░▀▄
 ▀▀░ ▀░▀▀ ▀░▀ ▀▀▀░ ░▀░ ▀░░▀ ▀▀▀ ▀▀░
    
    ''')

    print("Esta es una tierra llena de Dragones.")
    print("Frente a ti hay dos cuevas. En una de")
    print("ellas el dragon es generoso, amigable")
    print("y compartira su riquesa contigo.")
    time.sleep(2)
    print("El otro dragon es codicioso, esta hambriento")
    print("y te devorara inmediatamente.")

#El jugador debe elegir una cueva a cual entrar

def elegirCueva():
    cueva = ' '
    while cueva != '1' and cueva != '2':
        print('¿A qué cueva quieres entrar?  ( 1 o 2 )')
        cueva = input()

    return cueva

#El juego define cual cueva es la que tiene el dragon amigable, mientras muestra la historia

def explorarCueva(cuevaElegida):
    print('Te aprocimas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print("""
    
━━━╮""''""''"
━━╮╰╮┊┊┊┊┊┊
┊┊╰╮╰━▂▂▂▂┊┊┊┊┊┊
┊▂╱▔╲▔╱┏┳╮╲┊┊ᶤ.╭╮
▂╲▂▂╱╲╲╰┻┛╱▔▔▔▔┃
╲▂▂╱╭╯╱▔▔╱▔▔▔▽▽╯
┊╱╱╭╯╱▔▔▔╲▂▂△▂△╮
━━━╯╱╱╭━━━━━━━━╯



¡Un gran dragon aparece subitamente frente a tí!.
Abre sus fauces.""")
    print()
    time.sleep(2)
    cuevaAmigable = random.randint(1, 2)

#Dependiendo de random, se compara con la opcion de el jugador

    if cuevaElegida == str(cuevaAmigable):
        print('¡Te regala su tesoro!')
    else:
        print('!Te engulle de un bocado!')
  
#Se Le pregunta al jugador si desea jugar de nuevo          
jugarDeNuevo = 'si'
while jugarDeNuevo == 'si' or jugarDeNuevo == 's':

    mostrarIntroducción()

    númeroDeCueva = elegirCueva()

    explorarCueva(númeroDeCueva)

    print('¿Quieres jugar de nuevo? ( sí o no )')
    jugarDeNuevo = input()   
