import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir constantes
ANCHO = 800
ALTO = 800
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)

# Crear la ventana
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tablero de Parchís")

# Clases para el juego
class Ficha:
    def __init__(self, color):
        self.color = color
        self.posicion = 0  # Posición en el tablero
        self.en_carcela = True  # Si la ficha está en la cárcel

class Jugador:
    def __init__(self, color):
        self.color = color
        self.fichas = [Ficha(color) for _ in range(4)]  # 4 fichas por jugador
        self.fichas_en_juego = 0  # Fichas que han salido de la cárcel

class Tablero:
    def __init__(self):
        self.jugadores = [Jugador("Rojo"), Jugador("Verde"), Jugador("Azul"), Jugador("Amarillo")]
        self.turno_actual = 0  # Índice del jugador actual
        self.dado1 = 0
        self.dado2 = 0

    def lanzar_dados(self):
        self.dado1 = random.randint(1, 6)
        self.dado2 = random.randint(1, 6)

    def mover_ficha(self, jugador, ficha, movimiento):
        if ficha.en_carcela:
            if movimiento == 5:
                ficha.en_carcela = False
                ficha.posicion = 0  # Salida
                jugador.fichas_en_juego += 1
                print(f"{jugador.color} ha sacado una ficha de la cárcel.")
            else:
                print(f"{jugador.color} no puede mover la ficha de la cárcel.")
        else:
            nueva_posicion = ficha.posicion + movimiento
            if nueva_posicion < 68:
                ficha.posicion = nueva_posicion
                print(f"{jugador.color} ha movido su ficha a la posición {ficha.posicion}.")
            else:
                print(f"{jugador.color} no puede mover la ficha más allá de la posición 68.")

    def jugar_turno(self):
        jugador = self.jugadores[self.turno_actual]
        print(f"\nTurno de {jugador.color}.")
        self.lanzar_dados()
        print(f"Dados: {self.dado1}, {self.dado2}")

        # Lógica para mover fichas
        for dado in (self.dado1, self.dado2):
            if jugador.fichas_en_juego > 0:
                print("Fichas en juego:", [ficha.posicion for ficha in jugador.fichas if not ficha.en_carcela])
                ficha_a_mover = int(input(f"Selecciona la ficha a mover (0-3): "))
                self.mover_ficha(jugador, jugador.fichas[ficha_a_mover], dado)

        # Cambiar turno
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)

# Función para dibujar el tablero
def dibujar_tablero(tablero):
    # Fondo blanco
    screen.fill(BLANCO)

    # Dibujar el tablero
    pygame.draw.rect(screen, VERDE, (100, 100, 600, 600))  # Área del tablero
    pygame.draw.rect(screen, NEGRO, (100, 100, 600, 600), 5)  # Borde del tablero

    # Dibujar las casillas (ejemplo simple)
    for i in range(1, 6):
        pygame.draw.rect(screen, ROJO, (100 + i * 100, 100, 100, 100), 0)  # Parte superior
        pygame.draw.rect(screen, AZUL, (100 + i * 100, 600, 100, 100), 0)  # Parte inferior
        pygame.draw.rect(screen, AMARILLO, (100, 100 + i * 100, 100, 100), 0)  # Parte izquierda
        pygame.draw.rect(screen, VERDE, (600, 100 + i * 100, 100, 100), 0)  # Parte derecha

    # Dibujar el centro
    pygame.draw.rect(screen, NEGRO, (350, 350, 100, 100), 0)  # Centro del tablero

    # Dibujar las fichas
    for jugador in tablero.jugadores:
        for ficha in jugador.fichas:
            if not ficha.en_carcela:
                # Aquí puedes personalizar la posición de las fichas según su posición en el tablero
                x = 100 + ficha.posicion % 10 * 60  # Ejemplo de cálculo de posición
                y = 100 + ficha.posicion // 10 * 60
                pygame.draw.circle(screen, jugador.color, (x, y), 20)  # Dibujar ficha

# Bucle principal
tablero = Tablero()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dibujar_tablero(tablero)
    pygame.display.flip()

    # Jugar un turno
    tablero.jugar_turno()  # Llama a la función para jugar un turno


    ### Explicación del Código:

#- **Clases**:
#  - `Ficha`: Representa una ficha del jugador, con atributos para el color, la posición y si está en la cárcel.
#  - `Jugador`: Representa a un jugador, con un color y una lista de fichas.
#  - `Tablero`: Representa el tablero del juego, maneja los jugadores, el lanzamiento de dados y el movimiento de fichas.

#- **Lógica del Juego**:
#  - El juego se ejecuta en un bucle donde cada jugador lanza los dados y elige qué ficha mover.
#  - Se permite que el jugador mueva una ficha de la cárcel si saca un 5.
#  - Se imprime el estado del juego en cada turno.

#- **Interacción**:
#  - El jugador puede seleccionar qué ficha mover mediante la entrada de consola.

### Consideraciones:

#- Este código es una implementación básica y no incluye todas las reglas.
#- La entrada del usuario se maneja de manera simple. Puedes agregar validaciones para asegurarte de que el usuario ingrese valores válidos.