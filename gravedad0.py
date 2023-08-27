import math
import matplotlib.pyplot as plt

# Simulación del movimiento de un objeto bajo la gravedad
def movimiento_gravitatorio(tiempo_total, delta_tiempo):
    tiempo = [0]
    posicion = [0]

    # Variables iniciales
    velocidad_inicial = 0
    gravedad = 9.8

    # Cálculo de la posición en cada instante de tiempo
    for t in range(1, int(tiempo_total / delta_tiempo) + 1):
        tiempo.append(t * delta_tiempo)
        posicion_actual = posicion[t - 1] + velocidad_inicial * delta_tiempo
        posicion.append(posicion_actual)
        velocidad_inicial -= gravedad * delta_tiempo

    # Graficar la posición en función del tiempo
    plt.plot(tiempo, posicion)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Posición (m)')
    plt.title('Movimiento de un objeto bajo la gravedad')
    plt.show()

# Simulación del comportamiento de un péndulo
def simulacion_pendulo(tiempo_total, delta_tiempo, longitud, angulo_inicial):
    tiempo = [0]
    angulo = [angulo_inicial]
    velocidad_angular = [0]

    gravedad = 9.8

    for t in range(1, int(tiempo_total / delta_tiempo) + 1):
        tiempo.append(t * delta_tiempo)
        aceleracion_angular = -(gravedad / longitud) * math.sin(angulo[t - 1])
        velocidad_angular_actual = velocidad_angular[t - 1] + aceleracion_angular * delta_tiempo
        velocidad_angular.append(velocidad_angular_actual)
        angulo_actual = angulo[t - 1] + velocidad_angular[t] * delta_tiempo
        angulo.append(angulo_actual)

    # Graficar el ángulo en función del tiempo
    plt.plot(tiempo, angulo)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Ángulo (rad)')
    plt.title('Comportamiento de un péndulo')
    plt.show()
    
# Solicitar entrada de valores al usuario
print("Ejemplo :movimiento_gravitatorio(10, 0.1) ")
tiempo_total_movimiento = float(input("Ingrese el tiempo total de simulación para movimiento gravitatorio (segundos): "))
delta_tiempo_movimiento = float(input("Ingrese el intervalo de tiempo para movimiento gravitatorio (segundos): "))

print("Ejemplo :simulacion_pendulo(10, 0.01, 1, math.radians(45)) ")
tiempo_total_pendulo = float(input("Ingrese el tiempo total de simulación para el péndulo (segundos): "))
delta_tiempo_pendulo = float(input("Ingrese el intervalo de tiempo para el péndulo (segundos): "))
longitud_pendulo = float(input("Ingrese la longitud del péndulo (metros): "))
angulo_inicial_pendulo = float(input("Ingrese el ángulo inicial del péndulo (grados): "))

# Llamada a las funciones de simulación con los valores ingresados
movimiento_gravitatorio(tiempo_total_movimiento, delta_tiempo_movimiento)
simulacion_pendulo(tiempo_total_pendulo, delta_tiempo_pendulo, longitud_pendulo, math.radians(angulo_inicial_pendulo))
# Llamada a las funciones de simulación
#movimiento_gravitatorio(10, 0.1)
#simulacion_pendulo(10, 0.01, 1, math.radians(45))
