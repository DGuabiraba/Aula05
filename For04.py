cont = 0
for i in range(1, 10+1, 1):

    n = int(input("Digite um numero:"))
    if n < 0:
        cont += 1
print(f"{cont}")
