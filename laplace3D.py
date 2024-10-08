# --------------------------------LAPLACE-3D----------------------------------------
# un script de python que resuelve la ecuación de Laplace ∇^2 V = 0 en tres dimensiones
# V(x_i,y_j,z_k) para (x_i,y_j,z_k) ∈ [0,Lx]x[0,Ly]x[0,Lz] con una discretización x_{i+1} = x_i + h,
# y_{j+1} = y_j + h, z_{k+1} = z_k + h
# ---------------------------------------------------------------------------------#

# libreria con arreglos y funciones matemáticas
import numpy as np
# librería para gŕaficos
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d 

# libreria para copiar objetos sin referenciar
from copy import deepcopy

# configuración del texto de las gráficas
# comente si no tiene una distribución de latex instalada
from matplotlib import rc
rc('text', usetex=True)
rc('font', size=12)
rc('legend', fontsize=10)
rc('text.latex', preamble=r'\usepackage[OT1]{fontenc}')

# Condiciones del problema
# Dominio
Lx = 1.
Ly = 1.
Lz = 1.
# Discretización
# número de nodos N y separación entre puntos h
h = 1E-1
N = int(Lx / h)
# arreglo con los valores de las coordenadas de cada nodo
# x = np.arange(0,Lx+h,h)
# y = np.arange(0,Ly+h,h)
x = Lx * np.linspace(0,1,N)
y = Ly * np.linspace(0,1,N)
z = Lz * np.linspace(0,1,N)
# Creación e inicialización de dos arreglos para 
# el cálculo de potencial V^VIEJO y V^NUEVO
# considerando x -> i (primer indice), 
# y->j (segundo indice), z->k (tercer indice)
V_V = np.zeros((N,N,N))
V_N = np.zeros((N,N,N))
# Condiciones de borde
# x = 0, ∀y ∀z (plano yz) 
V_N[0,:,:] = 5.
V_V[0,:,:] = 5.
# x = Lx, ∀y ∀z
V_N[N-1,:,:] = 5.
V_V[N-1,:,:] = 5.
# y = 0, ∀x ∀z
V_N[:,0,:] = 5.
V_V[:,0,:] = 5.
# y = Ly, ∀x ∀z
V_N[:,N-1,:] = 5.
V_V[:,N-1,:] = 5.
# z = 0, ∀x ∀y
V_N[:,:,0] = 5.
V_V[:,:,0] = 5.
# z = Lz, ∀x ∀y
V_N[:,:,N-1] = 5.
V_V[:,:,N-1] = 5.

# Condiciones de convergencia
# número máximo de iteraciones
n_iter = 1E5
# tolerancia para s = |V^NUEVO - V^VIEJO| < ϵ
e = 1E-4
# valores iniciales
n = 0
# Ciclo para calcular la solución
while True:
    # Recorremos cada nodo interior del dominio
    for i in range(1,N-1):
        for j in range(1,N-1):
            for k in range(1,N-1):
                # y calculamos su nuevo valor
                V_N[i,j,k] = (1./6.) * (V_V[i-1,j,k] + V_V[i+1,j,k] + V_V[i,j-1,k] + V_V[i,j+1,k] + V_V[i,j,k-1] + V_V[i,j,k+1])
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
    # control alternativo, número de iteraciones
    if n > n_iter:
        break

# mensaje informativo
print(f"{n} iteraciones realizadas ")
print(f"La diferencia entre soluciones consecutivas es del orden de O(10^{int(np.log10(s))})")



# Graficas de niveles para 3 cortes distintos
# V(x,y,L/2)
L_2 = int(N/2)
X, Y = np.meshgrid(x,y)
fig, eje = plt.subplots(figsize=(9,7))
cf = eje.contourf(X, Y, V_N[:,:,L_2], levels=20, cmap='viridis')
cs = eje.contour(X, Y, V_N[:,:,L_2], levels=20, colors='white', linewidths=0.5)
eje.clabel(cs, inline=True, fontsize=8)
plt.colorbar(cf)
plt.title(r"Potencial $V(x,y,z)$ para $z = \frac{L}{2}$")
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.show()

# V(x,L/2,z)
L_2 = int(N/2)
X, Z = np.meshgrid(x,z)
fig, eje = plt.subplots(figsize=(9,7))
cf = eje.contourf(X, Z, V_N[:,L_2,:], levels=20, cmap='viridis')
cs = eje.contour(X, Z, V_N[:,:,L_2], levels=20, colors='white', linewidths=0.5)
eje.clabel(cs, inline=True, fontsize=8)
plt.colorbar(cf)
plt.title(r"Potencial $V(x,y,z)$ para $y = \frac{L}{2}$")
plt.xlabel(r"$x$")
plt.ylabel(r"$z$")
plt.show()

# V(L/2,y,z)
L_2 = int(N/2)
Y, Z = np.meshgrid(y,z)
fig, eje = plt.subplots(figsize=(9,7))
cf = eje.contourf(Y, Z, V_N[L_2,:,:], levels=20, cmap='viridis')
cs = eje.contour(Y, Z, V_N[L_2,:,:], levels=20, colors='white', linewidths=0.5)
eje.clabel(cs, inline=True, fontsize=8)
plt.colorbar(cf)
plt.title(r"Potencial $V(x,y,z)$ para $x = \frac{L}{2}$")
plt.xlabel(r"$y$")
plt.ylabel(r"$z$")
plt.show()
