# --------------------------------LAPLACE-1D----------------------------------------
# un script de python que resuelve la ecuación de Laplace ∇^2 V = 0 en una dimensión
# V(x_i) para x_i ∈ [0,L] con una discretización x_{i+1} = x_i + h
# ---------------------------------------------------------------------------------#

# libreria con arreglos y funciones matemáticas
import numpy as np
# librería para gŕaficos
import matplotlib.pyplot as plt

# libreria para copiar objetos sin referenciar
from copy import deepcopy

# configuración del texto de las gráficas
from matplotlib import rc
rc('text', usetex=True)
rc('font', size=12)
rc('legend', fontsize=10)
rc('text.latex', preamble=r'\usepackage[OT1]{fontenc}')

print("LAPLACE 1D")

# Condiciones del problema
# Dominio
L = 1.
# Discretización
# número de nodos N y separación entre puntos h
N = 100
h = L / (N-1)
# arreglo con los valores de las coordenadas de cada nodo
x = L * np.linspace(0,1,N)
# Creación e inicialización de dos arreglos para 
# el cálculo de potencial V^VIEJO y V^NUEVO
V_V = np.zeros(N)
V_N = np.zeros(N)
# Condiciones de borde (dadas a ambos arreglos)
# x = 0 (i = 0 | primer nodo)
V_N[0] = 5.
V_V[0] = 5.
# x = L (i = N-1 | último nodo)
V_N[N-1] = 5.
V_V[N-1] = 5.
# Condiciones de convergencia
# número máximo de iteraciones
n_iter = 6000
# tolerancia para s = |V^NUEVO - V^VIEJO| < ϵ
e = 1E-6
n = 0
# lista para almacenar cada iteracion de V
V_lista = []
# Ciclo para calcular la solución
while True:
    V_lista.append(V_V)
    # Recorremos cada nodo interior del dominio
    for i in range(1,N-1):
        # y calculamos su nuevo valor
        V_N[i] = (1./2.) * (V_V[i-1] + V_V[i+1])
    # obtenemos la diferencia entre el valor nuevo y viejo del potencial
    s = np.linalg.norm(V_N - V_V)
    # si esta es menor a la tolerancia considerada
    if s < e:
        # detenemos las iteraciones
        break
    else:
        # actualizamos el potencial para la próxima iteración
        V_V = deepcopy(V_N)
    # contamos el número de iteración
    n = n + 1

# mensaje informativo
print(f"{n} iteraciones realizadas ")
print(f"La diferencia entre soluciones consecutivas es del orden de O(10^{int(np.log10(s))})")
# Gráfica de la solución
plt.plot(x, V_N)
plt.title(r"Potencial unidimensional")
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
n_ticks = 5
xticks = np.linspace(0,L,n_ticks)
xtickstags = ["%.2f"%(xi) for xi in xticks[:n_ticks-1]]
xtickstags.append("L")
plt.xticks(xticks, xtickstags)
plt.grid(ls="dashed")
plt.show()

# Animación para ver evolución de la solución
# import matplotlib.animation as animation
# fig, eje = plt.subplots()
# def actualizar_grafica(cuadro):
#     eje.clear()
#     eje.set_ylim(0,5.1)
#     eje.spines['top'].set_visible(False)
#     eje.plot(x, V_lista[cuadro], linewidth = 1.5)
#     eje.set_title(f"Potencial unidimensional \n ITERACIÓN {cuadro}")
#     eje.set_xlabel(r"$x$")
#     eje.set_ylabel(r"$V$")
#     n_ticks = 5
#     xticks = np.linspace(0,L,n_ticks)
#     xtickstags = ["%.2f"%(xi) for xi in xticks[:n_ticks-1]]
#     xtickstags.append("L")
#     plt.xticks(xticks, xtickstags)
#     plt.grid(ls="dashed")
#     return True
# animacion = animation.FuncAnimation(fig,
#                                     actualizar_grafica,
#                                     range(0,n,100),
#                                     interval=100,
#                                     repeat=False)
# animacion.save(filename="1Dsol_evol.gif", dpi=300, writer="pillow")
# plt.show()