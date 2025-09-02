n = int(input("Digite um némero e eu direi se ele é par ou ímpar: "))
if n % 2 == 0:
    print(f"O número {n} é par.")
else:
    print(f"O número {n} é ímpar.")
if n > 0:
    print("Ele é positivo.")
elif n == 0:
    print("Ele é nulo.")
elif n < 0:
    print("Ele é negativo")