import numpy 
partidos = ["socio-democrático", "ultra-derechista", "primero los ricos", "centro democrático", "cambio invertido", "alianza queremos mas pobres"]
votos_por_partido = np.random.randint(1, 25001, 6)
print(f"El ganador es el partido: '{partidos[np.argmax(votos_por_partido)]}' con {max(votos_por_partido)} votos")
