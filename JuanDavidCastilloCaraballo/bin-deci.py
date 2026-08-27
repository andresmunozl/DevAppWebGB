def decimal_a_binario(decimal):
    return bin(decimal)[2:]


def binario_a_decimal(binario):
    return int(binario, 2)


print("=== Conversor Decimal ↔ Binario ===")
print("1. Decimal a binario")
print("2. Binario a decimal")

opcion = input("Elige una opción (1 o 2): ")

if opcion == "1":
    decimal = int(input("Ingresa un número decimal: "))
    print("Binario:", decimal_a_binario(decimal))

elif opcion == "2":
    binario = input("Ingresa un número binario: ")
    print("Decimal:", binario_a_decimal(binario))

else:
    print("Opción no válida.")
