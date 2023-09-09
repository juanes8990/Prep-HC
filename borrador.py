def Factorial(numero):
    # Verificar si el número es de tipo entero y mayor o igual a 1
    if type(numero) == int and numero >= 1:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial
    else:
        return None


resultado = Factorial(4)
print(resultado)

resultado1 = Factorial(-1)
print(resultado1)