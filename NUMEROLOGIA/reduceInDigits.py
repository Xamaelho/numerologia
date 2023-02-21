"""About the module reduceInDigits.py
    receives an integer and processes it, returning a list of the number
    with the digits that compose it, and the consequent sum of digits 
    until ending with a single digit
    The list returned by the main module has the following order:
        - At location zero, the final digit
        - In location one, a list with the entered number and then its 
        digits
        - In location two, a list that begins with the sum of the digits
        of the number of location one, and the digits that compose it
    Example:
        For the entered number 328 will be returned:
        [4,[328,3,2,8],[13,1,3]]
        Because for 328 = 3+2+8 = 13 = 1+3=4
"""

def reduct_number(entered_number):
    """Reduce a number by adding its digits until it has a single digit.
    
    Args:
        entered_number: Int -> a positive number
    
    Variables:
        lst_output: List -> Contains all the data extracted from each loop. 
                The index 0 will always contain the final digit and the 
                following lists of numbers resulting from its reduction and 
                the digits that compose it. The final format will be:
                [reduced_digit,[first_reduced_number,her_digits][second...]]
        lst_loop: List -> partial list that will take the result of 
                          each loop
        acum: Int -> variable that adds the digits of a number

    Algorithm:
        1_ check if the number is negative
        2_ create a list with the number of the argument and decompose
            it until it is less than 10
    """
    if entered_number < 0:
        print("Se ingresó un número negativo. Será convertido a positivo.")
        entered_number *= -1
    lst_output = [0]
    while entered_number > 9:
        lst_loop = createListDigit(entered_number)
        lst_output.append(lst_loop)
        acum = 0
        for i in lst_loop[1:]:
            acum += i
        entered_number = acum
    lst_output[0] = entered_number
    return lst_output

def countDigits(entered_number: int):
    """Calculate how many digits an integer has
    
    Args:
        entered_number: Int -> a positive number
    
    Variables:
        digit: Int -> accumulator started at 1 because it is the minimum

    Algorithm:
        1_ check if the number is greater than 9
        2_ increase the digit variable by 1
        3_ reduce the entered number by one digit
    """
    digit = 1
    while entered_number > 9:
        digit += 1
        entered_number //= 10
    return digit

def listDigitsOfCompare(digit):
    """Create a list with numbers that represent units, tens, hundreds, etc.
    """
    lst_salida = []
    digit -= 1
    while digit != 0:
        nueves = "9"*digit
        lst_salida.append(int(nueves))
        digit -= 1
    return lst_salida

def createListDigit(number):
    """Creates a list with the entered number and the numbers that compose it
    
    Args:
        number: Int -> a positive number
    
    Variables:
        digit: Int -> number needed to get the comparison list
        lst_number_to_compare: List -> contains comparison units with the arg.
        lst_results_with_digits: List -> contains the resulting number to
                return
        reduced_number: Int -> contains the extracted digit
    """
    digit = countDigits(number)
    lst_number_to_compare = listDigitsOfCompare(digit)
    lst_results_with_digits = [number]
    while number > 9:
        for option_number in lst_number_to_compare:
            reduced_number = number // (option_number + 1)
            lst_results_with_digits.append(reduced_number)
            number -= (reduced_number*(option_number + 1))
        lst_results_with_digits.append(number)
    return lst_results_with_digits

if __name__ == "__main__":
    option = int(input("Elegir una opción:\n1- Testeo por número.\n2- Testeo por rango\n\n"))
    if option == 1:
        numero_prueba = int(input("Ingrese el número de prueba: "))
        cantidad_de_digitos = countDigits(numero_prueba)
        listado_comparativo = listDigitsOfCompare(cantidad_de_digitos)
        list_digits_of_number = reduct_number(numero_prueba)
        print(f"El número ingresado {numero_prueba} tiene {cantidad_de_digitos} dígitos")
        print(f"La lista de comparación de dígitos es: {listado_comparativo}")
        print(f"Los dígitos de {numero_prueba}: {list_digits_of_number}.")
    elif option == 2:
        init = int(input("Ingrese número de inicio: "))
        fin = int(input("Ingrese número de final de rango: "))
        for number in range(init,(fin+1)):
            list_digits_of_number = reduct_number(number)
            print(f"{number} : {list_digits_of_number}.")