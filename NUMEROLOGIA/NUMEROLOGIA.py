#PROYECTO NUMEROLOGÍA CON OPCIONES
"""Pasos a seguir:
A - Generar los siguientes datos:
    1- Ingresar un nombre por teclado
    2- Traducir cada letra en un número considerando los espacios.
    3- Sumar todos los numeros para generar el número del carácter.
    4- Sumar las vocales para generar el numero del corazón.
    5- Sumar las consonantes para generar el número social.
    6- Verificar si hay ausencias de números.
    7- Verificar las repeticiones de números.
B - Reducir espacio en el algoritmo y dar las opciones al usuario para que elija que quiere ver.
    1- Usando definiciones.
    2- Dirigiendo el programa con bucles.
C - Generar nuevos datos que hagan más específico aún los datos.
    1- Agregar al algoritmo el dato de la fecha de nacimiento
D - Crear relaciones y análisis entre los datos.
    1- Numeros predominantes positivos y negativos.
    2- Relación número del carácter y del destino
    3- Aspectos positivos y negativos de la persona.
"""
#SOBRE LA CLASE ======================================================================================

class numeros():
    def __init__(self, digito, esPar, estaPresente):
        self.digito = digito                #el numero escrito en formato int para hacer las comparaciones
        self.esPar = esPar                  #informacion util para comparaciones en las dignidades
        self.estaPresente = estaPresente    #contador para saber la cantidad de veces que se repite cada numero
    
    def ausentes(self):
        global dictDatos
        if self.estaPresente != 0:
            return 0
        if self.estaPresente == 0:
            print("El numero ", self.digito, " está ausente")
            return self.digito

    #esVocal = para saber si es true o false
    #queLetraEs = similar a esVocal OJO
    #dignidad = def para saber la cantidad de importancia de los numeros

uno1 = numeros(1, False, 0)
dos2 = numeros(2, True, 0)
tres3 = numeros(3, False, 0)
cuatro4 = numeros(4, True, 0)
cinco5 = numeros(5, False, 0)
seis6 = numeros(6, True, 0)
siete7 = numeros(7, False, 0)
ocho8 = numeros(8, True, 0)
nueve9 = numeros(9, False, 0)
listNumeros = [uno1, dos2, tres3, cuatro4, cinco5, seis6, siete7, ocho8, nueve9]
dictDatos = dict()
numeroMaestro = ("caracter", "corazon", "social")

#INGRESOS ===================================================================================
def ingresarNombre():
    global nombreEnLetras
    control = True
    while control:
        nombreEnLetras = input("Ingrese su nombre completo: ")
        nombreEnLetras = nombreEnLetras.upper()
        for letra in nombreEnLetras:
            if letra == " " or letra == "A" or letra == "B" or letra == "C" or letra == "D" or letra == "E" or letra == "F" or letra == "G" or letra == "H" or letra == "I" or letra == "J" or letra == "K" or letra == "L" or letra == "M" or letra == "N" or letra == "Ñ" or letra == "O" or letra == "P" or letra == "Q" or letra == "R" or letra == "S" or letra == "T" or letra == "U" or letra == "V" or letra == "W" or letra == "X" or letra == "Y" or letra == "Z" :
                continue
            else :
                print("Se ha ingresado un caracter especial por error.")
                nombreEnLetras = " "
                break
        if nombreEnLetras != " ":
            control = False

#SOBRE LA FECHA DE NACIMIENTO =================================================
def esBisiesto(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def ingresarDiaNacimiento():
    global dictDatos
    control = True
    while control:
        dia = int(input("Ingrese el día: "))
        if dia < 1 or dia > 31 :
            print("Se ha ingresado un número erróneo para el día")
        else:
            control = False
    dictDatos["dia"] = reducirEnDigitos(dia)

def ingresarMesNacimiento():
    global dictDatos
    control = True
    while control:
        mes = int(input("Ingrese el mes de nacimiento en números (1 a 12): "))
        if mes < 1 or mes > 12 :
            print("Se ha ingresado un número erróneo para el mes de nacimiento. Debe ser un número del 1 al 12")
            print("Enero = 1. Febrero = 2. Marzo = 3. Abril = 4. Mayo = 5. Junio = 6.")
            print("Julio = 7. Agosto = 8. Septiembre = 9. Octubre = 10. Noviembre = 11. Dicciembre = 12.")
        else:
            control = False
    dictDatos["mes"] = reducirEnDigitos(mes)

def ingresarAnioNacimiento():
    global dictDatos
    anio = int(input("Ingrese el año: "))
    dictDatos["anio"] = reducirEnDigitos(anio)

def comprobarFecha():
    global dictDatos, control
    if esBisiesto(dictDatos["anio"][0]) == False and dictDatos["mes"][0] == 2 and dictDatos["dia"][0] > 28 :
        print("Se ha ingresado mal el día de nacimiento. Febrero en ese año tiene hasta 28 días.")
        control = True
        return control
    if esBisiesto(dictDatos["anio"][0]) == True and dictDatos["mes"][0] == 2 and dictDatos["dia"][0] > 29 :
        print("Se ha ingresado mal el día de nacimiento. Febrero en ese año tiene hasta 29 días.")
        control = True
        return control
    if dictDatos["mes"][0] == 4 or dictDatos["mes"][0] == 6 or dictDatos["mes"][0] == 9 or dictDatos["mes"][0] == 11 and dictDatos["dia"][0] > 30 :
        print("Se ha ingresado un número erróneo para el día. Ese mes tiene hasta 30 días.")
        control = True
        return control
    control = False
    return control

def ingresarFechaNacimiento():
    global control, dictDatos
    control = True
    print("Primero, ingrese su fecha de nacimiento...")
    while control:
        ingresarDiaNacimiento()
        ingresarMesNacimiento()
        ingresarAnioNacimiento()
        comprobarFecha()
        if control:
            print("La fecha ingresada es: ",{dictDatos["dia"]},"/",{dictDatos["mes"]},"/",{dictDatos["mes"]},".")

#CONVERSIONES DEL NOMBRE ==============================================================
def reconocerLetra(letra):
    if letra == "A" or letra == "J" or letra == "S":
        return 1
    if letra == "B" or letra == "K" or letra == "T":
        return 2
    if letra == "C" or letra == "L" or letra == "U":
        return 3
    if letra == "D" or letra == "M" or letra == "V":
        return 4
    if letra == "E" or letra == "N" or letra == "Ñ" or letra == "W":
        return 5
    if letra == "F" or letra == "O" or letra == "X":
        return 6
    if letra == "G" or letra == "P" or letra == "Y":
        return 7
    if letra == "H" or letra == "Q" or letra == "Z":
        return 8
    if letra == "I" or letra == "R":
        return 9
    if letra == " ":
        return " "

def esVocal(letra):
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        return True
    else:
        return False

def convertirNombreANumeros(nombre):
    global dictDatos
    dictDatos["nombreEnNumeros"] = []
    for letra in nombre:
        digito = reconocerLetra(letra)
        dictDatos["nombreEnNumeros"].append(digito)

#CALCULO DE DIFERENTES NUMEROS =================================================
def reducirEnDigitos(numeroParaReducir):
    numeroParaComparar = [999, 99, 9]
    listaPrincipal = [0]
    listaDeNivel = list()
    digitoObtenido = 0
    digitoResultante = 0
    while numeroParaReducir > 9:
        listaDeNivel.append(numeroParaReducir)
        for opcionComparacion in numeroParaComparar:
            if numeroParaReducir > opcionComparacion:
                digitoObtenido = numeroParaReducir // (opcionComparacion + 1)
                listaDeNivel.append(digitoObtenido)
                numeroParaReducir -= (digitoObtenido * (opcionComparacion + 1))
            if digitoObtenido > 0 and digitoResultante == 0:
                digitoResultante = digitoObtenido
                digitoObtenido = 0
            if digitoObtenido > 0 and digitoResultante > 0:
                digitoResultante += digitoObtenido
                digitoObtenido = 0
            if numeroParaReducir < 10 and digitoResultante > 0:
                listaDeNivel.append(numeroParaReducir)
                listaPrincipal.append(listaDeNivel)
                numeroParaReducir += digitoResultante
                digitoResultante = 0
                if numeroParaReducir > 9:
                    listaDeNivel = []
                else:
                    listaPrincipal[0] = numeroParaReducir
    return listaPrincipal    

def calcularNumerosMaestros():
    global dictDatos, nombreEnLetras, numeroMaestro
    for tipo in numeroMaestro:
        acumularNumero = 0
        if tipo == "caracter":
            for numero in dictDatos["nombreEnNumeros"]:
                if numero == " ":
                    continue
                acumularNumero += numero
        if tipo == "corazon":
            for letra in nombreEnLetras:
                if esVocal(letra):
                    digito = reconocerLetra(letra)
                    acumularNumero += digito
        if tipo == "social":
            for letra in nombreEnLetras:
                if esVocal(letra) or letra == " ":
                    continue
                else:
                    digito = reconocerLetra(letra)
                    acumularNumero += digito
        dictDatos[tipo] = reducirEnDigitos(acumularNumero)

def contarNumeros(nombreHechoNumeros):
    for indice in nombreHechoNumeros:
        for numero in listNumeros:
            if indice == numero.digito:
                numero.estaPresente += 1

def contarAusencias():
    global dictDatos
    listAusentes = []
    for numero in listNumeros:
        resultado = int(numero.ausentes())
        if resultado != 0:
            listAusentes.append(resultado)
    dictDatos["Ausentes"] = listAusentes

def contarRepeticiones(numeroMayor: int, esPrimero):
    global dictDatos
    listMasRepetido = []
    listDigitos = []
    if esPrimero:
        for numero in listNumeros:
            if numero.estaPresente > numeroMayor:
                numeroMayor = int(numero.estaPresente)
        dictDatos["digitoMasRepetido"] = numeroMayor     
    control = 0
    for numero in listNumeros:
        if numeroMayor == numero.estaPresente:
            control = 1
            listDigitos.append(int(numero.digito))
    listMasRepetido.append(listDigitos)
    if esPrimero:
        dictDatos["listaMasRepetidos"] = listMasRepetido
        return numeroMayor
    if control == 0:
        return 0
    dictDatos["segundoDigitoMasRepetido"] = numeroMayor
    dictDatos["listaSegundosMasRepetidos"] = listMasRepetido

#IMPRESIONES =======================================================
def mostrarNombreEnNumeros(lista):
    for digito in lista:
        print(digito,end="")

def mostrarNumerosMaestros():
    global dictDatos, nombreEnLetras, numeroMaestro
    for tipo in numeroMaestro:
        if tipo == "caracter":
            for numero in dictDatos["nombreEnNumeros"]:
                print(numero,end="")
        if tipo == "corazon":
            for letra in nombreEnLetras:
                if esVocal(letra):
                    digito = reconocerLetra(letra)
                    print(digito,end="")
                else:
                    print(" ",end="")
        if tipo == "social":
            for letra in nombreEnLetras:
                if esVocal(letra) or letra == " ":
                    print(" ",end="")
                else:
                    digito = reconocerLetra(letra)
                    print(digito,end="")
        contador = 0
        for reduccion in dictDatos[tipo]:
            print(" = ",end="")
            if contador == 0:
                digitoMaestro = reduccion
                contador += 1
                continue
            if contador != 0:
                print(" -> ",dictDatos[tipo][contador][0] ,end="")
                contador += 1
        print(" -> ",digitoMaestro,"    Numero de ", tipo, "    ")
    print("")

def impresionRepeticiones(lista, digito):
    lenLista = len(lista)
    if lenLista > 1:
        print("Los numeros ",end="")
        for numero in lista:
            print(numero, end=", ")
        print("se repiten ",digito, " veces.")
    else:
        numeroUnico = lista[0]
        print("El numero ", numeroUnico, " se repite ", digito, " veces.")

def mostrarRepeticiones():
    global dictDatos
    contarAusencias()
    numeroMayor = int(listNumeros[0].estaPresente)
    numeroMayor = contarRepeticiones(numeroMayor, True)
    numeroMayor -= 1
    consulta = contarRepeticiones(numeroMayor, False)
    impresionRepeticiones(dictDatos["listaMasRepetidos"][0], dictDatos["digitoMasRepetido"])
    if consulta == 0 and numeroMayor != 2:
        numeroMayor -= 1
        consulta = contarRepeticiones(numeroMayor, False)
        if consulta == 0 or numeroMayor == 1:
            return
        impresionRepeticiones(dictDatos["listaSegundosMasRepetidos"][0], dictDatos["segundoDigitoMasRepetido"])        
    print("")

#APLICACIONES GENERALES =======================================================
def ingresarDatos():
    print("Bienvenido al programa de numerología.")
    ingresarNombre()
    ingresarFechaNacimiento()

def calcularDatos():
    global nombreEnLetras
    convertirNombreANumeros(nombreEnLetras)
    calcularNumerosMaestros()
    contarNumeros(dictDatos['nombreEnNumeros'])
    
def mostrarTramaDelNombre():
    print(nombreEnLetras)
    mostrarNumerosMaestros()

def mostrarDictDatos():
    mostrarTramaDelNombre()

    #for x,y in dictDatos.items():
    #    print("{} = {}".format(x, y))

ingresarDatos()
calcularDatos()
