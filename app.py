#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

def jugar_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]
    puntuacion_jugador = 0

    while True:
        # Oponente elige una opción aleatoria
        opcion_oponente = random.choice(opciones)

        # Interacción con el jugador
        opcion_jugador = input("Elige piedra, papel o tijeras: ").lower()

        # Validación de entrada del usuario
        if opcion_jugador not in opciones:
            print("¡Opción no válida! Por favor, elige entre piedra, papel o tijeras.")
            continue

        # Determinar ganador de la ronda
        if opcion_jugador == opcion_oponente:
            print(f"Empate. Ambos eligieron {opcion_jugador}.")
        elif (
            (opcion_jugador == "piedra" and opcion_oponente == "tijeras") or
            (opcion_jugador == "tijeras" and opcion_oponente == "papel") or
            (opcion_jugador == "papel" and opcion_oponente == "piedra")
        ):
            print(f"Ganaste. {opcion_jugador} gana a {opcion_oponente}.")
            puntuacion_jugador += 1
        else:
            print(f"Perdiste. {opcion_oponente} gana a {opcion_jugador}.")

        # Mostrar puntuación actual
        print(f"Puntuación actual: {puntuacion_jugador}")

        # Preguntar al jugador si desea jugar de nuevo
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != "s":
            print(f"¡Gracias por jugar! Puntuación final: {puntuacion_jugador}")
            break

# Iniciar el juego
jugar_piedra_papel_tijeras()


