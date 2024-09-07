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
n_iter = 5000
# tolerancia para s = |V^NUEVO - V^VIEJO| < ϵ
e = 1E-3

n = 1
s = -1
# Ciclo para calcular la solución
while (s < e or n <= n_iter):
    # Recorremos cada nodo interior del dominio
    for i in range(1,N-1):
        # y calculamos su nuevo valor
        V_N[i] = (1./2.) * (V_V[i-1] + V_V[i+1])
    # obtenemos la diferencia entre el valor nuevo y viejo del potencial
    s = np.linalg.norm(V_N - V_V)
    # actualizamos el potencial para la próxima iteración
    V_V = deepcopy(V_N)
    # contamos el número de iteración
    n = n + 1

# mensaje informativo
print(f"{n} iteraciones realizadas ")
print(f"La diferencia entre soluciones consecutivas es de O(10^{int(np.log10(s))})")
# Gráfica de la solución
plt.plot(x,V_N)
plt.title(r"Potencial unidimensional")
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.show()