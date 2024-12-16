


nombre1 = input("Ingrese su nombre jugador 1 : ")
nombre2 = input("Ingrese su nombre jugador 2 : ")

jugador1 = input(nombre1+" elija piedra, papel o tijera: ")
jugador2 = input(nombre2+" elija piedra, papel o tijera: ")


condicion = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2  == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if jugador1 == jugador2:
    print("Empate!! ")
elif condicion or condicion2 or condicion3:
    print("Ha ganado "+nombre1)
else:
    print("Ha ganado "+nombre2)

