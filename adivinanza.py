import random



numeroSecreto = random.randint(1, 101)
adivinado = False
cantIntentos = 5

print("Adivina el número secreto")


while adivinado == False:
    
    if cantIntentos <= 0:
        print("Game Over!")
        break
    
    numeroElegido = int(input("Ingresa un número del 1 al 100: "))
    cantIntentos -= 1
    
    if numeroElegido == numeroSecreto:
        print("Has Adivinado!!!")
        adivinado = True
    elif numeroElegido > numeroSecreto:
        print("El número secreto es más chico que el número elegido. Te quedan "+str(cantIntentos)+" intentos")
    else:
        print("el número secreto es mayor que el número elegido. Te quedan "+str(cantIntentos)+" intentos")
        
    
    




