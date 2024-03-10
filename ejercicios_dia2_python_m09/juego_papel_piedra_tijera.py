def movimiento(jugador):
    while True:
        movimiento = input(f"{jugador},piedra, papel o tijera: ")
        if movimiento in ['piedra', 'papel', 'tijera']:
            return movimiento
        else:
            print("piedra, papel o tijera.")

def ganador(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    
    elif (jugador1 == 'piedra' and jugador2 == 'tijera') or \
         (jugador1 == 'papel' and jugador2 == 'piedra') or \
        (jugador1 == 'tijera' and jugador2 == 'papel'):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"


nombre_jugador1 = input("Nombre del Jugador 1: ")
nombre_jugador2 = input("Nombre del Jugador 2: ")

movimiento_jugador1 = movimiento(nombre_jugador1)
movimiento_jugador2 = movimiento(nombre_jugador2)

resultado = ganador(movimiento_jugador1, movimiento_jugador2)
print(resultado)
