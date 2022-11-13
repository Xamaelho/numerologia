"""Encargarse del ingreso y la comprobación de una fecha determinada."""
error_day = "Se ha ingresado un número erróneo para el dia. "
error_month = "Se ha ingresado un número erróneo para el mes. "
meses = {1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",
        6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",
        11:"Noviembre",12:"Dicciembre"}
def esBisiesto(year: int):
    """Return True if a year is leap-year
    
    Parameters:
        year: int   -> A number to be analized
    Algorithm:
        For the function to be true, the year must be divisible by four
        and four hundred, and its division by one hundred must be nonzero.
    """
    return year%4 == 0 and year%100 != 0 or year%400 == 0
def add_day():
    control = True
    while control:
        day = int(input("Ingrese el día: "))
        if day < 1 or day > 31 :
            print(error_day)
            continue
        control = False
    return day
def add_month():
    control = True
    while control:
        month = int(input("\nIngrese el mes de nacimiento en números (1 a 12): "))
        if not month in meses:
            print(error_month,"Debe ser un número del 1 al 12.")
            for key, value in meses.items():
                print(f"{value}: {key}. ",end="")
                if value in ("Junio","Dicciembre"): 
                    print("")
            continue
        control = False
    return month
def add_year(month:int, day:int):
    """Return the ingresed number if is a correct date.
    
    Parameters:
        month:int   -> A number that represents a month
        day:int     -> A number that represents a day
    Algorithm:
        With the parameters it is determined if the day and month correspond
        to a real day.
        The first two If's check that the year agrees with leap years.
        The third If checks that the number of days for the selected month 
        is correct.
        If the entered data is wrong, it returns 0.
    """
    anio = int(input("\nIngrese el año: "))
    control = False
    if esBisiesto(anio)==False and month==2 and day>28:
        print(error_day, "Febrero en ese año tiene hasta 28 días.")
        control = True
    if esBisiesto(anio)==True and month==2 and day>29:
        print(error_day, "Febrero en ese año tiene hasta 29 días.")
        control = True
    if month in (4,6,9,11) and day > 30:
        print(error_day,"Ese mes tiene hasta 30 días.")
        control = True
    if control:
        print(f"La fecha ingresada es: {day}/{month}/{anio}. Reingrese.\n")
        return 0
    return anio
def ingresarFechaNacimiento():
    year = 0
    while year == 0:
        day = add_day()
        month = add_month()
        year = add_year(month, day)
    fecha = {"dia":day, "mes":month, "año":year}
    return fecha

if __name__ == "__main__":
    print (ingresarFechaNacimiento())