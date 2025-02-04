# Desafío
# Se puede colocar el nombre en la segunda solicitud
# Lo ingresado por el usuario sea lowerCase de tal forma de comparar minúscula con minúscula
# Más de 1 turno con el bucle while

nombre1 = input('Nombre jugador 1: ')
nombre2 = input('Nombre jugador 2: ')

victorias1 = 0
victorias2 = 0

while victorias1 < 3 and victorias2 < 3:


    jugador1 = input(f'Hola {nombre1}, qué eliges: piedra, papel o tijera? ').lower()
    jugador2 = input(f'Hola {nombre2}, qué eliges: piedra, papel o tijera? ').lower()

    condicion1 = jugador1 == 'piedra' and jugador2 == 'tijera'
    condicion2 = jugador1 == 'papel' and jugador2 == 'piedra'
    condicion3 = jugador1 == 'tijera' and jugador2 == 'papel'
    
    if jugador1 == jugador2:
        print('Hay un empate')
    elif condicion1 or condicion2 or condicion3:
        print(f'{nombre1} has ganado!')
        victorias1 += 1
    else:
        print(f'{nombre2}, has ganado!')
        victorias2 += 1
    
    print(f'Marcador: {nombre1} {victorias1} - {victorias2} {nombre2}')
    print('-' * 30) 

if victorias1 == 3:
    print(f'{nombre1} has ganado con 3 victorias')
else:
    print(f'{nombre2} has ganado con 3 victorias')


print("Esta es la prueba para el pull at home")