cont = 0
cont2 = 0

for i in range(1, 11):
    num = int(input("Digite um numero: "))
    if 10 <= num <= 20:
        cont += 1

    else:
        cont2 += 1

print(f"entre 10 e 20: {cont} fora de deste intervalo {cont2}")
