"""Encargarse del ingreso y la comprobación de una fecha determinada."""

def esBisiesto(year: int):
    """retornar True si el año es bisiesto."""
    return year%4 == 0 and year%100 != 0 or year%400 == 0
def ingresarDiaNacimiento():
    control = True
    while control:
        dia = int(input("Ingrese el día: "))
        if dia < 1 or dia > 31 :
            print("Se ha ingresado un número erróneo para el día")
            continue
        control = False
    return dia
def ingresarMesNacimiento():
    control = True
    while control:
        mes = int(input("Ingrese el mes de nacimiento en números (1 a 12): "))
        if mes<1 or mes>12 :
            print("Se ha ingresado un número erróneo para el mes de \
                nacimiento. Debe ser un número del 1 al 12")
            print("Enero = 1. Febrero = 2. Marzo = 3. Abril = 4. Mayo = 5. \
                Junio = 6.")
            print("Julio = 7. Agosto = 8. Septiembre = 9. Octubre = 10. \
                Noviembre = 11. Dicciembre = 12.")
            continue
        control = False
    return mes
def ingresarAnioNacimiento(mes:int, dia:int):
    anio = int(input("Ingrese el año: "))
    control = False
    if esBisiesto(anio)==False and mes==2 and dia>28:
        print("Se ha ingresado mal el día de nacimiento. \
                Febrero en ese año tiene hasta 28 días.")
        control = True
    if esBisiesto(anio)==True and mes==2 and dia>29:
        print("Se ha ingresado mal el día de nacimiento. Febrero en ese año \
                tiene hasta 29 días.")
        control = True
    if mes==4 or mes==6 or mes==9 or mes==11 and dia>30:
        print("Se ha ingresado un número erróneo para el día. \
                Ese mes tiene hasta 30 días.")
        control = True
    if control:
        print(f"La fecha ingresada es: {dia}/{mes}/{anio}. Reingrese.")
        return 0
    return anio
def ingresarFechaNacimiento():
    year = 0
    while year == 0:
        dia = ingresarDiaNacimiento()
        mes = ingresarMesNacimiento()
        year = ingresarAnioNacimiento(mes, dia)
    fecha = {"dia":dia, "mes":mes, "año":year}
    return fecha

if __name__ == "__main__":
    print (ingresarFechaNacimiento())