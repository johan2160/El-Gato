import random

class TresEnRaya:

    def __init__(self):
        self.tablero = []

    def crear_tablero(self):
        for i in range(3):
            fila = []
            for j in range(3):
                fila.append('-')
            self.tablero.append(fila)

    def obtener_primer_jugador_aleatorio(self):
        return random.randint(0, 1)

    def marcar_casilla(self, fila, col, jugador):
        if self.tablero[fila][col] == '-':
            self.tablero[fila][col] = jugador
            return True
        else:
            print("¡Esa casilla ya está ocupada! Elige otra.")
            return False

    def verificar_ganador(self, jugador):
        n = len(self.tablero)

        # comprobando filas
        for i in range(n):
            if all([casilla == jugador for casilla in self.tablero[i]]):
                return True

        # comprobando columnas
        for i in range(n):
            if all([self.tablero[j][i] == jugador for j in range(n)]):
                return True

        # comprobando diagonales
        if all([self.tablero[i][i] == jugador for i in range(n)]) or all(
                [self.tablero[i][n - 1 - i] == jugador for i in range(n)]):
            return True

        return False

    def esta_tablero_lleno(self):
        for fila in self.tablero:
            if '-' in fila:
                return False
        return True

    def cambiar_turno_jugador(self, jugador):
        return 'X' if jugador == 'O' else 'O'

    def mostrar_tablero(self):
        for fila in self.tablero:
            for elemento in fila:
                print(elemento, end=" ")
            print()

    def empezar(self):
        self.crear_tablero()

        jugador = 'X' if self.obtener_primer_jugador_aleatorio() == 1 else 'O'
        while True:
            print(f"Turno del jugador {jugador}")

            self.mostrar_tablero()

            # obteniendo entrada del usuario y marcando la casilla
            while True:
                try:
                    fila, col = list(
                        map(int, input("Ingresa números de fila y columna para marcar la casilla: ").split()))

                    if self.marcar_casilla(fila - 1, col - 1, jugador):
                        break
                except (ValueError, IndexError):
                    print("Ingresa valores válidos para fila y columna.")

            # verificando si el jugador actual ha ganado o no
            if self.verificar_ganador(jugador):
                print(f"¡El jugador {jugador} gana el juego!")
                break

            # comprobando si el juego ha terminado en empate
            if self.esta_tablero_lleno():
                print("¡Empate!")
                break

            # cambiando el turno
            jugador = self.cambiar_turno_jugador(jugador)

        # mostrando la vista final del tablero
        print()
        self.mostrar_tablero()


# comenzando el juego
tres_en_raya = TresEnRaya()
tres_en_raya.empezar()
