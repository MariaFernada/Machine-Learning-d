import random
municipality = [random.sample(range(1, 45001), 6) for x in range(0, 124)]
results = [sum(col) for col in zip(*municipality)]
print("The winer was: " + str(results.index(max(results))))
