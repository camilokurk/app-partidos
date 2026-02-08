convocados = [1, 2, 3, 4, 5, 6, 7, 8]

titulares = [1, 2, 3, 4, 5]

print("Titulares:")
print(titulares)

cuartos_jugados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

en_pista = titulares.copy()

banquillo = []
for jugador in convocados:
    if jugador not in titulares:
        banquillo.append(jugador)

print("Banquillo:")
print(banquillo)

descansan = []
salen_a_pista = []

def calcular_cambios(convocados, en_pista, banquillo, descansan, salen_a_pista):

    for jugador in banquillo:
        salen_a_pista.append(jugador)

    for jugador in en_pista:
        descansan.append(jugador)

    diferencia = 5 - len(salen_a_pista)

    if diferencia > 0:
        for jugador in descansan[:diferencia]:
            salen_a_pista.append(jugador)
            descansan.remove(jugador)

    return (salen_a_pista, descansan)

calcular_cambios(convocados, en_pista, banquillo, descansan, salen_a_pista)

for jugador in salen_a_pista:
    cuartos_jugados[jugador] +=1

print("Salen a pista:")
print(salen_a_pista)
print("Descansan:")
print(descansan)

en_pista = salen_a_pista.copy()

banquillo = []
for jugador in convocados:
    if jugador not in en_pista:
        banquillo.append(jugador)

descansan = []
salen_a_pista = []

calcular_cambios(convocados, en_pista, banquillo, descansan, salen_a_pista)

for jugador in salen_a_pista:
    cuartos_jugados[jugador] +=1

print("Salen a pista:")
print(salen_a_pista)
print("Descansan:")
print(descansan)

en_pista = salen_a_pista.copy()

banquillo = []
for jugador in convocados:
    if jugador not in en_pista:
        banquillo.append(jugador)

descansan = []
salen_a_pista = []

print(cuartos_jugados)

