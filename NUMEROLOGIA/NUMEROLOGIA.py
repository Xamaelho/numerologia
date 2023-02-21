from IngresarFecha import ingresarFechaNacimiento
from reduceInDigits import reduct_number

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
lst_numeros = [uno1,dos2,tres3,cuatro4,cinco5,seis6,siete7,ocho8,nueve9]
dict_datos = dict()
tlp_numeros_maestros = ("caracter", "corazon", "social")
translated_digits = {1:("J","A","S"),2:("B","K","T"),3:("C","L","U"),
              4:("D","M","V"),5:("E","N","Ñ","W"),6:("F","O","X"),
              7:("G","P","Y"),8:("H","Q","Z"),9:("I","R")," ":" "}
dignity_dict = {12:("caracter","destino"),11:"corazon",10:"social",
                -10:"ausentes",7:"lst_mas_repetidos",4:"compuesto",
                5:"lst_segundos_mas_repetidos",-6:"reducto"}

def analize_dict(dict_arg:dict,var_arg):
    for key,value in dict_arg.items():
        if var_arg in value:
            return key
#INGRESOS ========================================================
def ingresarNombre():
    global nombre_en_letras
    control = True
    while control:
        nombre_en_letras = input("Ingrese su nombre completo: ")
        nombre_en_letras = nombre_en_letras.upper()
        options = (" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N",
                    "Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")
        for letra in nombre_en_letras:
            if letra in options:
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
    dict_datos["dia"] = reduct_number(dict_Fecha["dia"])
    dict_datos["mes"] = reduct_number(dict_Fecha["mes"])
    dict_datos["anio"] = reduct_number(dict_Fecha["año"])

#CONVERSIONES DEL NOMBRE ================================================
def esVocal(letra: str):
    return letra in ("A","E","I","O","U")
def convertirNombreANumeros(nombre: str):
    """Convertir la cadena en una lista de números."""
    global dict_datos
    dict_datos["lst_nombre_en_numeros"] = []
    for letra in nombre:
        digito = analize_dict(translated_digits,letra)
        dict_datos["lst_nombre_en_numeros"].append(digito)

#CALCULO DE DIFERENTES NUMEROS ========================================
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
                    digito = analize_dict(translated_digits,letra)
                    numero_acumulado += digito
        if tipo == "social":
            for letra in nombre_en_letras:
                if esVocal(letra) or letra == " ":
                    continue
                else:
                    digito = analize_dict(translated_digits,letra)
                    numero_acumulado += digito
        dict_datos[tipo] = reduct_number(numero_acumulado)
def calcularNumeroDestino():
    numero = dict_datos["dia"][0]+dict_datos["mes"][0]+dict_datos["anio"][0]
    dict_datos["destino"] = reduct_number(numero)
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
def calcular_dignidad():
    global dict_datos
    for key, value in dict_datos.items():
        valor_dignidad = 0
        if key in ("dia","mes","anio","lst_nombre_en_numeros",
                "digito_mas_repetido","segundo_digito_mas_repetido"):
            continue
        valor_dignidad = analize_dict(dignity_dict,key)
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
                valor_dignidad = analize_dict(dignity_dict,"reducto")
                ubicarDigito(value[listas_en_key][2], valor_dignidad)
                listas_en_key += 1
                continue
            cantidad_interna = len(value[listas_en_key])
            listas_internas = 1
            valor_dignidad = analize_dict(dignity_dict,"compuesto")
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
                    digito = analize_dict(translated_digits,letra)
                    print(digito,end="")
                else:
                    print(" ",end="")
        if tipo == "social":
            for letra in nombre_en_letras:
                if esVocal(letra) or letra == " ":
                    print(" ",end="")
                else:
                    digito = analize_dict(translated_digits,letra)
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