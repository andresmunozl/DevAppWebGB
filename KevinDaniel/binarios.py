print("================================")
print("   CONVERSOR DECIMAL - BINARIO")
print("================================")

print("1. Decimal a Binario")
print("2. Binario a Decimal")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    decimal = int(input("Ingrese un número decimal: "))
    
    binario = bin(decimal)[2:]
    
    print("El número", decimal, "en binario es:", binario)

elif opcion == 2:
    binario = input("Ingrese un número binario: ")
    
    decimal = int(binario, 2)
    
    print("El número", binario, "en decimal es:", decimal)

else:
    print("Opción no válida")