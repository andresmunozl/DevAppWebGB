print("=== CONVERSOR DECIMAL <-> BINARIO ===")

opcion = input("Escribe 1 para Decimal a Binario o 2 para Binario a Decimal: ")

if opcion == "1":
    decimal = int(input("Ingresa un numero decimal: "))
    binario = bin(decimal)[2:]
    print("Resultado en binario:", binario)

elif opcion == "2":
    binario = input("Ingresa un numero binario: ")
    decimal = int(binario, 2)
    print("Resultado en decimal:", decimal)

else:
    print("Opcion no valida")