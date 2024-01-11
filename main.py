import os

def main():
    print("¡Bienvenido al Juego de Laberinto!")
    nombre_jugador = input("Ingresa tu nombre: ")
    print(f"Bienvenido, {nombre_jugador}.")

   
if __name__ == "__main__":
    main()


# Definir el laberinto
laberinto = [
    "#####################",
    "#P.................#",
    "#.#######.########.#",
    "#.#...............#.#",
    "#.#.#############.#.#",
    "#.#.#...........#.#.#",
    "#.#.#.#########.#.#.#",
    "#.#.#.#.......#.#.#.#",
    "#.#.#.#.#####.#.#.#.#",
    "#.#.#.#.#...#.#.#.#.#",
    "#.#.#.#.#.#.#.#.#.#.#",
    "#.#.#.#.#.#.#.#.#.#.#",
    "#.#.#.#.#.#.#.#.#.#.#",
    "#.#.#.#.#.#.#.#.#.#.#",
    "#.#.#.#.#.#.#.#.#.#.#",
    "#.#.#.#.#.#.#.#.#.#.#",
    "#...........#........#",
    "#####################"
]

# Encontrar la posición inicial del jugador
def encontrar_posicion(laberinto):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == "P":
                return i, j

# Imprimir el laberinto
def imprimir_laberinto(laberinto):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar 
    for fila in laberinto:
        print(fila)

# Mover al jugador en el laberinto
def mover_jugador(tecla, posicion):
    i, j = posicion
    if tecla == "↑" and laberinto[i - 1][j] != "#":
        laberinto[i][j], laberinto[i - 1][j] = laberinto[i - 1][j], laberinto[i][j]
        return i - 1, j
    elif tecla == "↓" and laberinto[i + 1][j] != "#":
        laberinto[i][j], laberinto[i + 1][j] = laberinto[i + 1][j], laberinto[i][j]
        return i + 1, j
    elif tecla == "←" and laberinto[i][j - 1] != "#":
        laberinto[i][j], laberinto[i][j - 1] = laberinto[i][j - 1], laberinto[i][j]
        return i, j - 1
    elif tecla == "→" and laberinto[i][j + 1] != "#":
        laberinto[i][j], laberinto[i][j + 1] = laberinto[i][j + 1], laberinto[i][j]
        return i, j + 1
    else:
        return i, j

# Función principal del juego
def juego():
    posicion = encontrar_posicion(laberinto)

    while True:
        imprimir_laberinto(laberinto)
        tecla = input("Mueve al jugador con las teclas ↑ ↓ ← → (q para salir): ")
        
        if tecla.lower() == 'q':
            print("¡Juego terminado!")
            break

        posicion = mover_jugador(tecla, posicion)
        
        if laberinto[posicion[0]][posicion[1]] == "#":
            print("¡Oops! ¡Has chocado contra una pared!")
            break
        elif laberinto[posicion[0]][posicion[1]] == ".":
            print("¡Bien! Sigamos explorando...")
        elif laberinto[posicion[0]][posicion[1]] == "#":
            print("¡Felicidades! ¡Has llegado a la meta!")
            break

# Iniciar el juego
if __name__ == "__main__":
    juego()
