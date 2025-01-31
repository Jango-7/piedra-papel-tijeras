nombre1 = input('Nombre jugador 1: ')
nombre2 = input('Nombre jugador 2: ')

jugador1 = input('Hola ' + nombre1 + ' qué eliges: piedra, papel o tijera? ')
jugador2 = input('Hola ' + nombre2 + ' qué eliges: piedra, papel o tijera? ')

condicion1 = jugador1 == 'piedra' and jugador2 == 'tijera'
condicion2 = jugador1 == 'papel' and jugador2 == 'piedra'
condicion3 = jugador1 == 'tijera' and jugador2 == 'papel'

if condicion1 or condicion2 or condicion3:
    print('Felicitaciones', nombre1, 'has ganado!')
elif jugador1 == jugador2:
    print('Ha habido un empate')
else:
    print('Felicidades', nombre2, 'has ganado!')