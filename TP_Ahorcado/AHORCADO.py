from typing import Type
import string
import random
import csv


# ETAPA 1


def validar_ingreso(ingreso):
    # si la letra ni es un cararter alfabetico o tiene mas de un elemento no es valido
    if len(ingreso) > 1 or not ingreso.isalpha():
        validar = False
    else:
        validar = True
    return validar


def reemplazar_letras_adivinadas(palabra, palabra_adivinar, letra):
    # se encarga de reemplazar las letras que va ingresando el usuario, dentro de la 'palabra_a_adivinar'
    palabra_a_adivinar = list(palabra_adivinar)
    indice = []
    contar_letras = -1
    cadena = ''
    for l in palabra:
        contar_letras += 1
        if l == letra:
            indice.append(contar_letras)
    for i in indice:
        palabra_a_adivinar[i] = letra
    for x in palabra_a_adivinar:
        cadena += x
    return cadena


def ocultar_palabra(palabra):
    # genera una cadena de '?' con la longitud de la palabra que se quiere adivinar
    palabra_adivinar = "?" * len(palabra)
    return palabra_adivinar


def interaccion(palabra_a_adivinar, ACIERTOS, DESACIERTOS, mensaje, puntos, jugadorActual):
    # funcion que se encarga de imprimir por panatalla el avance del programa a medida que interactua con
    # el usuario
    print("--------------------------------------------------------------")
    print("\n\n", f"jugador actual: {jugadorActual}", "\n\n", mensaje, "puntos:", puntos, "→", palabra_a_adivinar, "\n",
          'Aciertos:', ACIERTOS, 'Desaciertos:',
          len(DESACIERTOS))
    letras = ''
    for i in DESACIERTOS:
        letras += "-" + i
    print(' Letras desacertadas:', letras, "\n\n")


# devuelve las variables palabra_a_adivinar, lista_letras_ingresadas, ACIERTOS
def ciclo(palabra, palabra_a_adivinar, letra, lista_letras_ingresadas, ACIERTOS, jugador):
    lista = configuracion()
    try:
        MAX_DESACIERTOS = int(lista[2][1])
    except:
        MAX_DESACIERTOS = 7
    try:
        PUNTOS_ACIERTOS = int(lista[3][1])
    except:
        PUNTOS_ACIERTOS = 10
    try:
        PUNTOS_DESACIERTOS = int(lista[4][1])
    except:
        PUNTOS_DESACIERTOS = 5
    salida = True
    while len(lista_letras_ingresadas) < MAX_DESACIERTOS and salida and palabra != palabra_a_adivinar:
        # valida la letra ingresada sino es una ingreso invalido
        if validar_ingreso(letra):
            # dentro de esta validacion hay 4 posibilidades
            # si ela letra esta y no esta ingresada
            if letra in palabra:
                if letra not in palabra_a_adivinar:
                    palabra_a_adivinar = reemplazar_letras_adivinadas(palabra, palabra_a_adivinar, letra)
                    ACIERTOS += 1

                    interaccion(palabra_a_adivinar, ACIERTOS, lista_letras_ingresadas, "Muy bien!!! continuas tu turno"
                                + " " +
                                jugador.upper(),
                                len(lista_letras_ingresadas) * (-1) * PUNTOS_DESACIERTOS + ACIERTOS * PUNTOS_ACIERTOS,
                                jugador)
                    letra = input("Ingrese letra: ")
                    letra = letra.lower()
                else:

                    interaccion(palabra_a_adivinar, ACIERTOS, lista_letras_ingresadas,
                                "Letra ya ingresada" + " " + jugador.upper(),
                                len(lista_letras_ingresadas) * (-1) * PUNTOS_DESACIERTOS + ACIERTOS * PUNTOS_ACIERTOS,
                                jugador)
                    letra = input("Ingrese letra: ")
                    letra = letra.lower()
            else:
                if letra not in lista_letras_ingresadas:
                    lista_letras_ingresadas.append(letra)

                    interaccion(palabra_a_adivinar, ACIERTOS, lista_letras_ingresadas, "Lo siento!!! Termino tu turno"
                                + " " + jugador.upper(),
                                len(lista_letras_ingresadas) * (-1) * PUNTOS_DESACIERTOS + ACIERTOS * PUNTOS_ACIERTOS,
                                jugador)
                    salida = False
                else:

                    interaccion(palabra_a_adivinar, ACIERTOS, lista_letras_ingresadas,
                                "letra ya ingresada" + " " + jugador.upper(),
                                len(lista_letras_ingresadas) * (-1) * PUNTOS_DESACIERTOS + ACIERTOS * PUNTOS_ACIERTOS,
                                jugador)
                    letra = input("Ingrese letra: ")
                    letra = letra.lower()
        else:
            if letra == "fin" or str(letra) == "0":
                salida = False
                letra = str(letra)
            else:

                interaccion(palabra_a_adivinar, ACIERTOS, lista_letras_ingresadas, jugador, "Ingreso Inválido" + " " +
                            jugador.upper(), len(lista_letras_ingresadas) * (-1) * PUNTOS_DESACIERTOS + ACIERTOS *
                            PUNTOS_ACIERTOS)
                letra = input("Ingrese letra: ")
                letra = letra.lower()
        # de cualquier manera pide la letra al
        # terminar el siclo a menos que ya este que ganes o pierdas
    return palabra_a_adivinar, lista_letras_ingresadas, ACIERTOS, letra


def lista_de_palabras(dictOrdenado, longitudPalabra):
    listaPalabras = []
    """Creamos una lista para almacenar todas las palabras segun la longitud que queremos"""
    for palabra in dictOrdenado.items():
        """usamos el "dict.items()" para recorrer una lista de tuplas"""
        if len(palabra[0]) == longitudPalabra:
            """Usamos la funcion "len()" y seleccionamos la posicion "0" para seleccionar solo la palabra"""
            listaPalabras.append(palabra[0])
            """Luego de comparar la longitud de la palabra con la longitud que se busca, si estas coinciden se agregan
            a la listaPalabras"""
        elif longitudPalabra == 0:
            """Definimos que pasa si el parametro longitudPalabra es cero, que en este caso, si el parametro es cero,
            se toma todo el diccionario"""
            listaPalabras = list(dictOrdenado)
    return listaPalabras


def seleccion(long, diccionario):
    """si la longitus es menor a 5 redefine la longitud para que elija
    cualquier elemento del diccionario"""
    if long >= 5:
        palabras_candidatas = lista_de_palabras(diccionario, long)
        palabra = random.choice(palabras_candidatas)
    else:
        long = 0
        palabras_candidatas = lista_de_palabras(diccionario, long)
        palabra = random.choice(palabras_candidatas)
    return palabra


# ETAPA 7


def elegir_longitud():
    """Solicita al usuario que ingrese la longitud de la incognita que intentara descubrir.
        la longitud no debe ser mayor al de la palabra mas larga del texto.
        a partir del input del usuario se devuelve una variable de longitud valida"""
    lista = configuracion()
    try:
        LONG_PALABRA_MIN = int(lista[1][1])
        if LONG_PALABRA_MIN < 5:
            print("ha superado la minima longitud de la palabra")
            LONG_PALABRA_MIN = 5
    except:
        LONG_PALABRA_MIN = 5
    longitud = input('Ingrese largo de incognita: ')
    while longitud == "" or longitud.isalpha():
        print('Ingrese un valor numerico')
        longitud = input('Ingrese largo de incognita: ')
    else:
        longitud_int = int(longitud)
        while longitud_int < LONG_PALABRA_MIN or longitud_int > 18:
            print('No hay palabras de tal longitud')
            longitud = input('Ingrese largo de incognita: ')
            longitud_int = int(longitud)
        return longitud_int


def ingresarJugadores():
    lista = configuracion()
    try:  # Valentin Fernandez Y Jose Blanco
        MAX_USUARIOS = int(lista[0][1])
        if MAX_USUARIOS > 10:
            MAX_USUARIOS = 10
    except:
        MAX_USUARIOS = 10
    listaJugadores = []  # se hace una lista vacia
    jugador = input("Ingrese su usuario: ")  # Se pregunta el usuario de lo/s jugador/es
    while jugador != "" and len(
            listaJugadores) < MAX_USUARIOS:  # registra cuantos jugadores se ingresan, si el numero llega al max el
        # ciclo se rompre y continua el proceso
        if jugador not in listaJugadores:  # si el jugador no esta en la lista de jugadores, lo registra
            listaJugadores.append(jugador)
        else:
            print(
                "El usuario ya esta registrado, por favor ingrese otro!")  # si el jugador ya esta en la lista de
            # jugadores, manda este mensaje diciendo que ingrese otro nickname
        if len(listaJugadores) < MAX_USUARIOS:
            jugador = input(
                "para finalizar el ingreso no ingrese nada. \nIngrese otro usuario: ")  # Indica lo que hay que
            # ingresar para terminar la funcion
    print("\n")
    print('COMIENZA LA PARTIDA')
    return listaJugadores


def generar_turnos(jugadores):
    lista_turnos = []
    turno = random.randint(1, len(jugadores))
    while len(lista_turnos) != len(jugadores):
        if turno in lista_turnos:
            turno = random.randint(1, len(jugadores))
        else:
            lista_turnos.append(turno)
    return lista_turnos


def generar_diccionario(jugadores, dic_palabras, longitud):
    dic_jugadores = {}
    turnos = generar_turnos(jugadores)
    for i in jugadores:
        palabra = seleccion(longitud, dic_palabras)
        # valores de la lista = [0turno,1palabra,2aciertos,3lista de letras,4palabra a adivinar,5puntos,6""]
        dic_jugadores[i] = [turnos[jugadores.index(i) - 1], palabra, 0, [], ocultar_palabra(palabra), 0, ""]
    return dict(sorted(dic_jugadores.items(), key=lambda x: x[1][0]))


def validacion(diccionario):
    # esta funcion valida si alguno de los jugadores hizo termino todas las jugadas
    try:
        MAX_DESACIERTOS = int(lista[2][1])
    except:
        MAX_DESACIERTOS = 7
    suma1 = 0
    suma2 = 0
    validacion = True
    for i in diccionario:
        if validacion:
            # palabra a adivinar es igual a la palabra?
            if diccionario[i][1] == diccionario[i][4]:
                validacion = False
                # letras ingresadas es 7
            if len(diccionario[i][3]) == MAX_DESACIERTOS or diccionario[i][6] == "fin" or diccionario[i][6] == "0":
                suma1 += 1
            if suma1 == len(diccionario.keys()):
                validacion = False
    return validacion


def juego(jugadores):
    lista = configuracion()
    try:
        MAX_DESACIERTOS = int(lista[2][1])
    except:
        MAX_DESACIERTOS = 7
    try:
        PUNTOS_ACIERTOS = int(lista[3][1])
    except:
        PUNTOS_ACIERTOS = 10
    try:
        PUNTOS_DESACIERTOS = int(lista[4][1])
    except:
        PUNTOS_DESACIERTOS = 5
    try:
        PUNTOS_ADIVINA_PALABRA = int(lista[5][1])
    except:
        PUNTOS_ADIVINA_PALABRA = 100
    try:
        PUNTOS_RESTA_GANA_PROGRAMA = int(lista[6][1])
    except:
        PUNTOS_RESTA_GANA_PROGRAMA = 20
    turno = 1
    while validacion(jugadores):
        for i in jugadores:
            if len(jugadores[i][3]) < MAX_DESACIERTOS and jugadores[i][6] != "fin" and jugadores[i][6] != 0:
                # palabra_a_adivinar, ACIERTOS, DESACIERTOS,mensaje,puntos
                interaccion(jugadores[i][4], jugadores[i][2], jugadores[i][3], i.upper(),
                            len(jugadores[i][3]) * (-1) * PUNTOS_DESACIERTOS + jugadores[i][2] * PUNTOS_ACIERTOS, [i])
                letra = input("Ingrese letra: ")
                letra = letra.lower()
                jugadores[i][6] = letra
                # palabra,  palabra_a_adivinar,   letra,   lista_letras_ingresadas,  ACIERTOS, jugador,puntos
                palabra_a_adivinar, lista_Dletras, aciertos, letra = ciclo(jugadores[i][1], jugadores[i][4],
                                                                           jugadores[i][6], jugadores[i][3],
                                                                           jugadores[i][2], i)
                # modificar los aciertos y cambiarlistas y palabra a adivinar
                jugadores[i][6] = letra
                jugadores[i][3] = lista_Dletras
                jugadores[i][4] = palabra_a_adivinar
                jugadores[i][2] = aciertos
        turno += 1
    for i in jugadores:
        jugadores[i][5] += jugadores[i][2] * PUNTOS_ACIERTOS - len(jugadores[i][3]) * PUNTOS_DESACIERTOS
        if jugadores[i][1] == jugadores[i][4]:
            jugadores[i][5] += PUNTOS_ADIVINA_PALABRA
        elif len(lista_Dletras) == MAX_DESACIERTOS:
            jugadores[i][5] -= PUNTOS_RESTA_GANA_PROGRAMA
    return dict(sorted(jugadores.items(), key=lambda x: x[1][5], reverse=True))


def repite_partida():
    respuerta = input("\ndesea jugar otra vez(s/n): ")
    return respuerta == "s"


def partida(dic):
    n = 1
    for i in dic:
        print("posicion:", n, "    usuario: ", i, "palabra:", dic[i][1], "	puntos: ", dic[i][5])
        n += 1


def imprimir_turnos(dic):
    for i in dic:
        print("turno ---", dic[i][0], "   jugador ---", i.upper(), "\n")


def reinicio_parametros(dic, dic_palabras, longitud):
    turnos = generar_turnos(dic.keys())
    for i in dic:
        palabra = seleccion(longitud, dic_palabras)
        dic[i] = [turnos[list(dic.keys()).index(i) - 1], palabra, 0, [], ocultar_palabra(palabra), dic[i][5], ""]
    return dict(sorted(dic.items(), reverse=True, key=lambda x: x[1][0]))


# ETAPA 8


def acento(cadena):
    """entra al texto entero en cada letra con acento
    la cambia por la misma letra sin acento
    repitiendo el ciclo por cada letra"""
    reemplazo = (
        ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), ("-", ""), ("_", ""), ("!", ""), (";", ""),
        ("«", ""),
        ("»", ""), ("¡", ""), ("ü", ""), ("¿", ""), ("►", ""))
    for a, b in reemplazo:
        cadena = cadena.replace(a, b).replace(a.upper(), b.upper())
    return cadena


def generar_diccionario_de_archivos():
    """funcion que genera un diccionario a partir de los archivos indicando palabras como claves, y su valor siendo
    las apariciones de la palabra en cada archivo"""
    dic = {}

    with open('La araña negra - tomo 1.txt', "r") as f:
        for linea in f:
            palabras = linea.rstrip("\n").split()
            for palabra in palabras:
                if palabra.isalpha() and len(palabra) >= 5:
                    palabra_modificada = acento(palabra).lower()
                    if palabra_modificada in dic:
                        dic[palabra_modificada][0] += 1
                    else:
                        dic[palabra_modificada] = [1, 0, 0]
    with open('Las 1000 Noches y 1 Noche.txt', "r") as f:
        for linea in f:
            palabras = linea.rstrip("\n").split()
            for palabra in palabras:
                if palabra.isalpha() and len(palabra) >= 5:
                    palabra_modificada = acento(palabra).lower()
                    if palabra_modificada in dic:
                        dic[palabra_modificada][1] += 1
                    else:
                        dic[palabra_modificada] = [0, 1, 0]
    with open('Cuentos.txt', "r") as f:
        for linea in f:
            palabras = linea.rstrip("\n").split()
            for palabra in palabras:
                if palabra.isalpha() and len(palabra) >= 5:
                    palabra_modificada = acento(palabra).lower()
                    if palabra_modificada in dic:
                        dic[palabra_modificada][2] += 1
                    else:
                        dic[palabra_modificada] = [0, 0, 1]
    """Se genera un archivo palabras.csv con el diccionario"""
    with open('palabras.csv', 'w') as f:
        writer = csv.writer(f)
        for k, v in dic.items():
            writer.writerow([k, v])
    return dic


def configuracion():
    """Lee el archivo de configuracion y crea una lista con las variables y lista_de_palabras
    respectivos valores de configuracion.csv"""
    with open('configuraciones.csv') as f:
        archivo = f.read()
        variables = archivo.split('\n')
        lista = []
        for i in variables:
            lista.append(i.split(','))
        return lista


def imprimir(lista):
    """Imprime las configuraciones del juego"""
    print("Acontinuacion las reglas:")
    try:
        print("Maxima cantidad de usuarios:", int(lista[0][1]))
    except:
        print("Maxima cantidad de usuarios: 10")
    try:
        print("Longitud minima de palabra:", int(lista[1][1]))
    except:
        print("Longitud minima de palabra: 5")
    try:
        print("Desaciertos Maximos:", int(lista[2][1]))
    except:
        print("Desaciertos Maximos: 7")
    try:
        print("Puntos por acierto:", int(lista[3][1]))
    except:
        print("Puntos por acierto: 10")
    try:
        print("Puntos por desacierto:", int(lista[4][1]))
    except:
        print("Puntos por desacierto: 5")
    try:
        print("Puntos por adivinar la palabra:", int(lista[5][1]))
    except:
        print("Puntos por adivinar la palabra: 100")
    try:
        print("Puntos restados:", int(lista[6][1]))
    except:
        print("Puntos restados: 20")


# ETAPA 4(MAIN)


def main():
    lista = configuracion()
    imprimir(lista)
    palabras = generar_diccionario_de_archivos()
    longitud = elegir_longitud()
    jugadores = generar_diccionario(ingresarJugadores(), palabras, longitud)
    """imprime los turnos de los jugadores"""
    print("\n")
    print('TURNOS DE LOS JUGADORES: ', "\n")
    imprimir_turnos(jugadores)
    """inicia la partida"""
    jugadores = juego(jugadores)
    """muestra las posiciones de los jugadores"""
    partida(jugadores)
    """tengo q reiniciar las variables"""
    while repite_partida():
        longitud = elegir_longitud()
        jugadores = reinicio_parametros(jugadores, palabras, longitud)
        imprimir_turnos(jugadores)
        jugadores = juego(jugadores)
        partida(jugadores)


main()
