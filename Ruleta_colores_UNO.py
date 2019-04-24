# Ruleta de colores para el juego "UNO".
import random
import time
import sys

print("Presioná 'Enter' para girar la ruleta")
print("Ingresá 'Salir' para cerrar")
while True:
    key = input()
    randnumber = random.randint(1, 4)
    color = ""
    if key.upper() == "SALIR":
        quit()
    if randnumber == 1:
        color = "Rojo"
    elif randnumber == 2:
        color = "Azul"
    elif randnumber == 3:
        color = "Amarillo"
    else:
        color = "Verde"
    time.sleep(0.25)
    for s in range(5):
        sys.stdout.flush()
        sys.stdout.write(".")
        time.sleep(0.15)
    print("\n" + color + "!")
