import signal

def palindromo():
    aciertos = 0
    fallos = 0

    while True:
        try:
            palabra = input("Ingresa una palabra: ")
            palabra = palabra.lower()
            palabra = palabra.replace(" ", "")

            if palabra == palabra[::-1]:
                print("La palabra es un palíndromo.")
                aciertos += 1
            else:
                print("La palabra no es un palíndromo.")
                fallos += 1
            
            print(f"Número de aciertos: {aciertos}")
            print(f"Número de fallos: {fallos}")
            respuesta = input("¿Quieres jugar de nuevo? (s/n)")

            if (respuesta != "s"):
                print("¡ADIOS!")
                break
        
        except KeyboardInterrupt:
            print("\n¡ADIOS!")
            break

palindromo()
