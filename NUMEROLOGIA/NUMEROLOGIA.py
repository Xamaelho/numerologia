from IngresarFecha import *

#SOBRE LA CLASE ===================================================
class numeros():
    """
    Almacena la informacion de los digitos.

    Partes
    digito -- número de type int para comparaciones con variables.
    es_par -- característica de la instancia.
    esta_presente -- contador de repeticiones en lst_nombre_en_numeros.
    dignidad -- almacena los usos de cada instancia.
    """
    def __init__(self, digito:int, es_par, esta_presente, dignidad:int):
        self.digito = digito                
        self.es_par = es_par                 
        self.esta_presente = esta_presente
        self.dignidad = dignidad
    def ausentes(self):
        global dict_datos
        if self.esta_presente != 0:
            return 0
        if self.esta_presente == 0:
            print("El numero ", self.digito, " está ausente")
            return self.digito
    #dignidad = def para saber la cantidad de importancia de los numeros

uno1 = numeros(1, False, 0, 0)
dos2 = numeros(2, True, 0, 0)
tres3 = numeros(3, False, 0, 0)
cuatro4 = numeros(4, True, 0, 0)
cinco5 = numeros(5, False, 0, 0)
seis6 = numeros(6, True, 0, 0)
siete7 = numeros(7, False, 0, 0)
ocho8 = numeros(8, True, 0, 0)
nueve9 = numeros(9, False, 0, 0)
lst_numeros = [uno1, dos2, tres3, cuatro4, cinco5, seis6, siete7, ocho8, nueve9]
dict_datos = dict()
tlp_numeros_maestros = ("caracter", "corazon", "social")
#INGRESOS ========================================================
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

#SOBRE LA FECHA DE NACIMIENTO ============================================
def implemetarFecha():
    global dict_datos
    dict_Fecha = ingresarFechaNacimiento()
    dict_datos["dia"] = reducirEnDigitos(dict_Fecha["dia"])
    dict_datos["mes"] = reducirEnDigitos(dict_Fecha["mes"])
    dict_datos["anio"] = reducirEnDigitos(dict_Fecha["año"])

#CONVERSIONES DEL NOMBRE ================================================
def reconocerLetra(letra: str):
    """Convertir la letra ingresada en un número."""
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
    return False
def convertirNombreANumeros(nombre: str):
    """Convertir la cadena en una lista de números."""
    global dict_datos
    dict_datos["lst_nombre_en_numeros"] = []
    for letra in nombre:
        digito = reconocerLetra(letra)
        dict_datos["lst_nombre_en_numeros"].append(digito)

#CALCULO DE DIFERENTES NUMEROS ========================================
def reducirEnDigitos(numero_ingresado: int):
    """Reducir el argumento hasta obtener un número de un solo dígito.
    
    Argumentos:
    numero_ingresado -- numero menor a 10.000 (funcion creada para usar solo
        con este tipo de análisis)
    """
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
                numero_ingresado -=(numero_reducido*(opcion_comparacion + 1))
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
    """Calcular numeros importantes segun la lista lst_nombre_en_numeros."""
    global dict_datos, nombre_en_letras, tlp_numeros_maestros
    for tipo in tlp_numeros_maestros:
        numero_acumulado = 0
        if tipo == "caracter":
            for numero in dict_datos["lst_nombre_en_numeros"]:
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
    numero = dict_datos["dia"][0]+dict_datos["mes"][0]+dict_datos["anio"][0]
    dict_datos["destino"] = reducirEnDigitos(numero)
def contarNumeros(nombre_en_numeros):
    """Cargar las ocurrencias de cada numero en la clase <<numeros>>."""
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
    dict_datos["ausentes"] = lst_ausentes
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

#CALCULO DE DIGNIDADES===================================
def otorgarValorADignidad(nombre_llave):
    if nombre_llave == "caracter":
        return 12
    if nombre_llave == "corazon":
        return 11
    if nombre_llave == "social":
        return 10
    if nombre_llave == "destino":
        return 12
    if nombre_llave == "ausentes":
        return -10
    if nombre_llave == "lst_mas_repetidos":
        return 7
    if nombre_llave == "lst_segundos_mas_repetidos":
        return 5
    if nombre_llave == "compuesto":
        return 4
    if nombre_llave == "reducto":
        return -6

def calcular_dignidad():
    global dict_datos
    for key, value in dict_datos.items():
        valor_dignidad = 0
        if key == "dia" or key == "mes" or key == "anio" or \
            key == "lst_nombre_en_numeros" or key == "digito_mas_repetido" or \
            key == "segundo_digito_mas_repetido":
            continue
        valor_dignidad = otorgarValorADignidad(key)
        if key == "lst_mas_repetidos":
            for digito in value[0]:
                ubicarDigito(digito, valor_dignidad)
            continue
        if key == "lst_segundos_mas_repetidos":
            for digito in value[0]:
                ubicarDigito(digito, valor_dignidad)
            continue
        ubicarDigito(value[0], valor_dignidad)
        cantidad_externa = len(value)
        listas_en_key = 1
        while listas_en_key < cantidad_externa:
            if value[listas_en_key][0] < 20:
                valor_dignidad = otorgarValorADignidad("reducto")
                ubicarDigito(value[listas_en_key][2], valor_dignidad)
                listas_en_key += 1
                continue
            cantidad_interna = len(value[listas_en_key])
            listas_internas = 1
            valor_dignidad = otorgarValorADignidad("compuesto")
            while listas_internas < cantidad_interna:
                ubicarDigito(value[listas_en_key][listas_internas], \
                valor_dignidad)
                listas_internas += 1
            listas_en_key += 1
def ubicarDigito(number: int, dignidad: int):
    for opcion_numero in lst_numeros:
        if number == opcion_numero.digito:
            opcion_numero.dignidad += dignidad
            break

#IMPRESIONES =======================================================
def mostrarNombreEnNumeros(lista):
    for digito in lista:
        print(digito,end="")
def mostrarNumerosMaestros():
    global dict_datos, nombre_en_letras, tlp_numeros_maestros
    for tipo in tlp_numeros_maestros:
        if tipo == "caracter":
            for numero in dict_datos["lst_nombre_en_numeros"]:
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
        print(" -> ",digito_maestro)
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

#APLICACIONES GENERALES ==========================================
def ingresarDatos():
    print("Bienvenido al programa de numerología.")
    ingresarNombre()
    implemetarFecha()
def calcularDatos():
    global nombre_en_letras
    convertirNombreANumeros(nombre_en_letras)
    calcularNumerosMaestros()
    contarNumeros(dict_datos['lst_nombre_en_numeros'])
    calcularNumeroDestino()
def mostrarTramaDelNombre():
    print(nombre_en_letras)
    mostrarNumerosMaestros()

def mostrarDiccionario():
    print("Numero de carácter: ", dict_datos["caracter"][0])
    print("Numero de corazon: ", dict_datos["corazon"][0])
    print("Numero de lo social: ", dict_datos["social"][0])
    print("Numero de destino: ", dict_datos["destino"][0])
    mostrarRepeticiones()
    for x,y in dict_datos.items():
        print("{} = {}".format(x, y))
    calcular_dignidad()
    for numero in lst_numeros:
        print("Dignidad del ", numero.digito, ": ", numero.dignidad)

ingresarDatos()
calcularDatos()
mostrarTramaDelNombre()
mostrarDiccionario()