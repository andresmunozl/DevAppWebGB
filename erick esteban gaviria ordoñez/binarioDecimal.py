def decimal_a_binario(decimal):
    return bin(decimal)[2:]


def binario_a_decimal(binario):
    return int(binario, 2)


while True:
    print("\n===== CONVERSOR =====")
    print("1. Decimal a binario")
    print("2. Binario a decimal")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        numero = int(input("Ingrese un número decimal: "))
        resultado = decimal_a_binario(numero)
        print(f"Binario: {resultado}")

    elif opcion == "2":
        numero = input("Ingrese un número binario: ")

        if all(digito in "01" for digito in numero):
            resultado = binario_a_decimal(numero)
            print(f"Decimal: {resultado}")
        else:
            print("Error: ingrese solamente 0 y 1.")

    elif opcion == "3":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")