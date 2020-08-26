numero_1 = int(input("Escriba un número entero: "))
numero_2 = int(input(f"Escriba un número entero mayor o igual que {numero_1}: "))
for i in range(numero_1, numero_2 + 1):
    if i % 2 == 0: print(f"El número {i} es par.")
