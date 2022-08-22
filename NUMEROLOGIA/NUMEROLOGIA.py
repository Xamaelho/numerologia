#SOBRE LA CLASE ======================================================================================
class numeros():
    def __init__(self, digito:int, esPar, esta_presente):
        self.digito = digito                
        self.esPar = esPar                  
        self.esta_presente = esta_presente    
    def ausentes(self):
        global dict_datos
        if self.esta_presente != 0:
            return 0
        if self.esta_presente == 0:
            print("El numero ", self.digito, " está ausente")
            return self.digito
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
lst_numeros = [uno1, dos2, tres3, cuatro4, cinco5, seis6, siete7, ocho8, nueve9]
dict_datos = dict()
tlp_numeros_maestros = ("caracter", "corazon", "social")
#INGRESOS ===================================================================================
def ingresarNombre():
    global nombre_en_letras
    control = True
    while control:
        nombre_en_letras = input("Ingrese su nombre completo: ")
        nombre_en_letras = nombre_en_letras.upper()
        for letra in nombre_en_letras:
            if (letra == " " or letra == "A" or letra == "B" or \
                    letra == "C" or letra == "D" or letra == "E" or \
                    letra == "F" or letra == "G" or letra == "H" or \
                    letra == "I" or letra == "J" or letra == "K" or \
                    letra == "L" or letra == "M" or letra == "N" or \
                    letra == "Ñ" or letra == "O" or letra == "P" or \
                    letra == "Q" or letra == "R" or letra == "S" or \
                    letra == "T" or letra == "U" or letra == "V" or \
                    letra == "W" or letra == "X" or letra == "Y" or \
                    letra == "Z" ):
                continue
            else :
                print("Se ha ingresado un caracter especial por error.")
                nombre_en_letras = " "
                break
        if nombre_en_letras != " ":
            control = False

#SOBRE LA FECHA DE NACIMIENTO =================================================
def esBisiesto(year: int):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
def ingresarDiaNacimiento():
    global dict_datos
    control = True
    while control:
        dia = int(input("Ingrese el día: "))
        if dia < 1 or dia > 31 :
            print("Se ha ingresado un número erróneo para el día")
        else:
            control = False
    dict_datos["dia"] = reducirEnDigitos(dia)
def ingresarMesNacimiento():
    global dict_datos
    control = True
    while control:
        mes = int(input("Ingrese el mes de nacimiento en números (1 a 12): "))
        if mes < 1 or mes > 12 :
            print("Se ha ingresado un número erróneo para el mes de nacimiento. \
                Debe ser un número del 1 al 12")
            print("Enero = 1. Febrero = 2. Marzo = 3. Abril = 4. Mayo = 5. \
                Junio = 6.")
            print("Julio = 7. Agosto = 8. Septiembre = 9. Octubre = 10. \
                Noviembre = 11. Dicciembre = 12.")
        else:
            control = False
    dict_datos["mes"] = reducirEnDigitos(mes)
def ingresarAnioNacimiento():
    global dict_datos
    anio = int(input("Ingrese el año: "))
    dict_datos["anio"] = reducirEnDigitos(anio)
def comprobarFecha():
    global dict_datos, control
    if (esBisiesto(dict_datos["anio"][0]) == False and \
            dict_datos["mes"][0] == 2 and dict_datos["dia"][0] > 28 ):
        print("Se ha ingresado mal el día de nacimiento. \
                Febrero en ese año tiene hasta 28 días.")
        control = True
        return control
    if (esBisiesto(dict_datos["anio"][0]) == True and \
            dict_datos["mes"][0] == 2 and dict_datos["dia"][0] > 29 ):
        print("Se ha ingresado mal el día de nacimiento. Febrero en ese año \
                tiene hasta 29 días.")
        control = True
        return control
    if (dict_datos["mes"][0] == 4 or dict_datos["mes"][0] == 6 or \
            dict_datos["mes"][0] == 9 or dict_datos["mes"][0] == 11 and \
            dict_datos["dia"][0] > 30 ):
        print("Se ha ingresado un número erróneo para el día. \
                Ese mes tiene hasta 30 días.")
        control = True
        return control
    control = False
    return control
def ingresarFechaNacimiento():
    global control, dict_datos
    control = True
    print("Primero, ingrese su fecha de nacimiento...")
    while control:
        ingresarDiaNacimiento()
        ingresarMesNacimiento()
        ingresarAnioNacimiento()
        comprobarFecha()
        if control:
            print("La fecha ingresada es: ",{dict_datos["dia"]},"/",\
                    {dict_datos["mes"]},"/",{dict_datos["mes"]},".")

#CONVERSIONES DEL NOMBRE ==============================================================
def reconocerLetra(letra: str):
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
def esVocal(letra: str):
    if (letra == "A" or letra == "E" or letra == "I" or letra == "O" or \
            letra == "U"):
        return True
    else:
        return False

def convertirNombreANumeros(nombre: str):
    global dict_datos
    dict_datos["lst_nombre_En_Numeros"] = []
    for letra in nombre:
        digito = reconocerLetra(letra)
        dict_datos["lst_nombre_En_Numeros"].append(digito)

#CALCULO DE DIFERENTES NUMEROS =================================================
def reducirEnDigitos(numero_ingresado: int):
    lst_numero_para_comparar = [999, 99, 9]
    lst_salida = [0]
    lst_numero_con_digitos = list()
    numero_reducido = 0
    digito_resultante = 0
    if numero_ingresado < 10:
        lst_salida[0] = numero_ingresado
        return lst_salida
    while numero_ingresado > 9:
        lst_numero_con_digitos.append(numero_ingresado)
        for opcion_comparacion in lst_numero_para_comparar:
            if numero_ingresado > opcion_comparacion:
                numero_reducido = numero_ingresado // (opcion_comparacion + 1)
                lst_numero_con_digitos.append(numero_reducido)
                numero_ingresado -= (numero_reducido * (opcion_comparacion + 1))
            if numero_reducido > 0 and digito_resultante == 0:
                digito_resultante = numero_reducido
                numero_reducido = 0
            if numero_reducido > 0 and digito_resultante > 0:
                digito_resultante += numero_reducido
                numero_reducido = 0
            if numero_ingresado < 10 and digito_resultante > 0:
                lst_numero_con_digitos.append(numero_ingresado)
                lst_salida.append(lst_numero_con_digitos)
                numero_ingresado += digito_resultante
                digito_resultante = 0
                if numero_ingresado > 9:
                    lst_numero_con_digitos = []
                else:
                    lst_salida[0] = numero_ingresado
    return lst_salida    
def calcularNumerosMaestros():
    global dict_datos, nombre_en_letras, tlp_numeros_maestros
    for tipo in tlp_numeros_maestros:
        numero_acumulado = 0
        if tipo == "caracter":
            for numero in dict_datos["lst_nombre_En_Numeros"]:
                if numero == " ":
                    continue
                numero_acumulado += numero
        if tipo == "corazon":
            for letra in nombre_en_letras:
                if esVocal(letra):
                    digito = reconocerLetra(letra)
                    numero_acumulado += digito
        if tipo == "social":
            for letra in nombre_en_letras:
                if esVocal(letra) or letra == " ":
                    continue
                else:
                    digito = reconocerLetra(letra)
                    numero_acumulado += digito
        dict_datos[tipo] = reducirEnDigitos(numero_acumulado)
def calcularNumeroDestino():
    numero = dict_datos["dia"][0] + dict_datos["mes"][0] + dict_datos["anio"][0]
    dict_datos["numero_Destino"] = reducirEnDigitos(numero)
def contarNumeros(nombre_en_numeros):
    for indice in nombre_en_numeros:
        for numero in lst_numeros:
            if indice == numero.digito:
                numero.esta_presente += 1
def contarAusencias():
    global dict_datos
    lst_ausentes = []
    for numero in lst_numeros:
        resultado = int(numero.ausentes())
        if resultado != 0:
            lst_ausentes.append(resultado)
    dict_datos["Ausentes"] = lst_ausentes
def contarRepeticiones(numero_mayor: int, es_primero):
    global dict_datos
    lst_mas_repetidos = []
    lst_digitos = []
    if es_primero:
        for numero in lst_numeros:
            if numero.esta_presente > numero_mayor:
                numero_mayor = int(numero.esta_presente)
        dict_datos["digito_mas_repetido"] = numero_mayor     
    control = 0
    for numero in lst_numeros:
        if numero_mayor == numero.esta_presente:
            control = 1
            lst_digitos.append(int(numero.digito))
    lst_mas_repetidos.append(lst_digitos)
    if es_primero:
        dict_datos["lst_mas_repetidos"] = lst_mas_repetidos
        return numero_mayor
    if control == 0:
        return 0
    dict_datos["segundo_digito_mas_repetido"] = numero_mayor
    dict_datos["lst_segundos_mas_repetidos"] = lst_mas_repetidos

#IMPRESIONES =======================================================
def mostrarNombreEnNumeros(lista):
    for digito in lista:
        print(digito,end="")
def mostrarNumerosMaestros():
    global dict_datos, nombre_en_letras, tlp_numeros_maestros
    for tipo in tlp_numeros_maestros:
        if tipo == "caracter":
            for numero in dict_datos["lst_nombre_En_Numeros"]:
                print(numero,end="")
        if tipo == "corazon":
            for letra in nombre_en_letras:
                if esVocal(letra):
                    digito = reconocerLetra(letra)
                    print(digito,end="")
                else:
                    print(" ",end="")
        if tipo == "social":
            for letra in nombre_en_letras:
                if esVocal(letra) or letra == " ":
                    print(" ",end="")
                else:
                    digito = reconocerLetra(letra)
                    print(digito,end="")
        contador = 0
        for reduccion in dict_datos[tipo]:
            print(" = ",end="")
            if contador == 0:
                digito_maestro = reduccion
                contador += 1
                continue
            if contador != 0:
                print(" -> ",dict_datos[tipo][contador][0] ,end="")
                contador += 1
        print(" -> ",digito_maestro,"    Numero de ", tipo, "    ")
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
    global dict_datos
    contarAusencias()
    numero_mayor = int(lst_numeros[0].esta_presente)
    numero_mayor = contarRepeticiones(numero_mayor, True)
    numero_mayor -= 1
    consulta = contarRepeticiones(numero_mayor, False)
    impresionRepeticiones(dict_datos["lst_mas_repetidos"][0], \
        dict_datos["digito_mas_repetido"])
    if consulta == 0 and numero_mayor != 2:
        numero_mayor -= 1
        consulta = contarRepeticiones(numero_mayor, False)
        if consulta == 0 or numero_mayor == 1:
            return
        impresionRepeticiones(dict_datos["lst_segundos_mas_repetidos"][0], \
            dict_datos["segundo_digito_mas_repetido"])        
    print("")

#APLICACIONES GENERALES =======================================================
def ingresarDatos():
    print("Bienvenido al programa de numerología.")
    ingresarNombre()
    ingresarFechaNacimiento()
def calcularDatos():
    global nombre_en_letras
    convertirNombreANumeros(nombre_en_letras)
    calcularNumerosMaestros()
    contarNumeros(dict_datos['lst_nombre_En_Numeros'])
    calcularNumeroDestino()
def mostrarTramaDelNombre():
    print(nombre_en_letras)
    mostrarNumerosMaestros()

def mostrarDiccionario():
    print("Numero de carácter: ", dict_datos["caracter"][0])
    print("Numero de corazon: ", dict_datos["corazon"][0])
    print("Numero de lo social: ", dict_datos["social"][0])
    print("Numero de destino: ", dict_datos["numero_Destino"][0])
    mostrarRepeticiones()

    #for x,y in dict_datos.items():
    #    print("{} = {}".format(x, y))

ingresarDatos()
calcularDatos()
mostrarTramaDelNombre()
mostrarDiccionario()