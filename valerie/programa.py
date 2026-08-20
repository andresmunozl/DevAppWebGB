def decimal_a_binario(numero):
	return bin(numero)[2:]


def binario_a_decimal(numero):
	return int(numero, 2)


def main():
	print("Conversor de numeros")
	print("1. Decimal a binario")
	print("2. Binario a decimal")

	opcion = input("Elige una opcion (1 o 2): ").strip()

	try:
		if opcion == "1":
			numero = int(input("Introduce un numero decimal: "))
			if numero < 0:
				raise ValueError
			print(f"Resultado: {decimal_a_binario(numero)}")
		elif opcion == "2":
			numero = input("Introduce un numero binario: ").strip()
			if not numero or any(digito not in "01" for digito in numero):
				raise ValueError
			print(f"Resultado: {binario_a_decimal(numero)}")
		else:
			print("Opcion no valida.")
	except ValueError:
		print("Entrada no valida.")


if __name__ == "__main__":
	main()
