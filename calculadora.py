def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

def potencia(a, b):
    return a ** b

def division_entera(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: división por cero"
    
if opcion == "division":
    resultado = division(a, b)
    print("La suma es:", resultado)
elif opcion == "potencia":
    resultado = potencia(a, b)
    print("La resta es:", resultado)
elif opcion == "division entera":
    resultado = division_entera(a, b)
    print("La multiplicación es:", resultado)
else:
    print("Opción no válida")