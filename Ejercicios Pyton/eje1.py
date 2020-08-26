from random import randint
edad_habitantes = [randint(1, 100) for i in range(randint(1000, 75000))]
menores, mayores = len(list((filter(lambda edad: edad<18 , edad_habitantes)))), len(list(filter(lambda edad: edad>=18, edad_habitantes)))
print(f"Población total: {len(edad_habitantes)}")
print(f"Porcentaje de menores de edad: {menores/len(edad_habitantes)*100}. Porcentaje de mayores de edad: {mayores/len(edad_habitantes)*100}")
