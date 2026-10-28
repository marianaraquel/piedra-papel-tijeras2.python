nombre1=input("¿cómo se llama el jugador1 ?: ")
nombre2=input("¿cómo se llama el jugador2 ?: ")
i=0
while i < 3:

    jugador1=input("Hola " + nombre1 + "¿ que elijes? ¿piedra, papel o tijeras? : ")
    minuscula1=jugador1.lower()
    jugador2=input("Hola "+ nombre2 + " ¿que elijes? ¿piedra, papel o tijeras? : ")
    minuscula2=jugador2.lower()

    condicion1=minuscula1=="piedra" and minuscula2=="tijeras"
    condicion2=minuscula1=="papel" and minuscula2=="piedra"
    condicion3=minuscula1=="tijeras" and minuscula2=="papel"


    if jugador1==jugador2:
        print("¡Ha sido un empate!")
    elif condicion1 or condicion2 or condicion3 :
        print("Ha ganado:",nombre1)
    else:
        print("Ha ganado:",nombre2)
    i+=1
