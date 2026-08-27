def decimal_a_binario_con_formato(numero, bits=8):
    """
    Convierte un número decimal a binario con un número específico de bits
    """
    if numero < 0:
        return "No se permiten números negativos"
    
    if numero == 0:
        return "0" * bits
    
    binario = ""
    temp = numero
    while temp > 0:
        residuo = temp % 2
        binario = str(residuo) + binario
        temp = temp // 2
    
    # Rellenar con ceros a la izquierda
    while len(binario) < bits:
        binario = "0" + binario
    
    return binario

# Ejemplo de uso
numero = int(input("Ingresa un número decimal: "))
bits = int(input("Ingresa el número de bits (ej: 8, 16, 32): "))

resultado = decimal_a_binario_con_formato(numero, bits)
print(f"El número {numero} en binario de {bits} bits es: {resultado}")