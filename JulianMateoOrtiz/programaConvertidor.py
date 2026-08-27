def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    return binario


def binario_a_decimal(binario):
    decimal = 0
    potencia = 0
    for digito in reversed(binario):
        if digito == "1":
            decimal += 2 ** potencia
        elif digito != "0":
            raise ValueError("Entrada invalida: solo se permiten 0 y 1.")
        potencia += 1
    return decimal


while True:
    print("\n=== CONVERTIDOR DECIMAL - BINARIO ===")
    print("1. Decimal a binario")
    print("2. Binario a decimal")
    print("3. Salir")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        numero = int(input("Ingrese un numero decimal: "))
        print(f"El numero {numero} en binario es: {decimal_a_binario(numero)}")

    elif opcion == "2":
        numero_binario = input("Ingrese un numero binario: ")
        print(f"El numero binario {numero_binario} en decimal es: {binario_a_decimal(numero_binario)}")

    elif opcion == "3":
        print("Hasta luego!")
        break

    else:
        print("Opcion invalida. Intenta de nuevo.")
