convocados = [1, 2, 3, 4, 5, 6, 7, 8]

titulares = [1, 2, 3, 4, 5]

cuartos_jugados = {jugador: 0 for jugador in convocados}

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



