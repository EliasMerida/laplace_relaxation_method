# --------------------------------LAPLACE-2D----------------------------------------
# un script de python que resuelve la ecuación de Laplace ∇^2 V = 0 en dos dimensiones
# V(x_i,y_j) para (x_i,y_j) ∈ [0,Lx]x[0,Ly] con una discretización x_{i+1} = x_i + h, y_{j+1} = y_j + h
# ---------------------------------------------------------------------------------#

# libreria con arreglos y funciones matemáticas
import numpy as np
# librería para gŕaficos
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d 

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
Lx = 1.
Ly = 1.
# Discretización
# número de nodos N y separación entre puntos h
h = 1E-2
N = int(Lx / h) + 1
# arreglo con los valores de las coordenadas de cada nodo
# x = np.arange(0,Lx+h,h)
# y = np.arange(0,Ly+h,h)
x = Lx * np.linspace(0,1,N)
y = Ly * np.linspace(0,1,N)
# Creación e inicialización de dos arreglos para 
# el cálculo de potencial V^VIEJO y V^NUEVO
# considerando x -> i (fila), y->j (columna)
V_V = np.zeros((N,N))
V_N = np.zeros((N,N))
# Condiciones de borde
# x = 0, ∀y 
V_N[0,:] = 5.
V_V[0,:] = 5.
# x = Lx, ∀y 
V_N[N-1,:] = 5.
V_V[N-1,:] = 5.
# y = 0, ∀x 
V_N[:,0] = 5.
V_V[:,0] = 5.
# x = 0, ∀y 
V_N[:,N-1] = 5.
V_V[:,N-1] = 5.
# Condiciones de convergencia
# número máximo de iteraciones
n_iter = 5000
# tolerancia para s = |V^NUEVO - V^VIEJO| < ϵ
e = 1E-3
# valores iniciales
n = 1
s = -1
# Ciclo para calcular la solución
while (s < e or n <= n_iter):
    # Recorremos cada nodo interior del dominio
    for i in range(1,N-1):
        for j in range(1,N-1):
            # y calculamos su nuevo valor
            V_N[i,j] = (1./4.) * (V_V[i-1,j] + V_V[i+1,j] + V_V[i,j-1] + V_V[i,j+1])
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
X, Y = np.meshgrid(x,y)
# creo figura
fig = plt.figure()
# creo ejes para graficar en 3D
eje = plt.axes(projection='3d')
# en los ejes grafico la superficie
sup = eje.plot_surface(X, Y, V_N, cmap='gist_heat')
# a la figura le sumo una barra, indicando en que ejes (ax) en que reduzca el tamaño de la barra (shrink)
fig.colorbar(sup, ax = eje, shrink = 0.5)
eje.set_title(r"Potencial bidimensional")
eje.set_xlabel(r"$x$")
eje.set_ylabel(r"$y$")
plt.show()

plt.set_cmap('inferno')   
plt.contourf(X,Y,V_N)
plt.colorbar()
plt.title(r"Potencial bidimensional")
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.show()