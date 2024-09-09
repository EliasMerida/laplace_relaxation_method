# Resolución de la Ecuación de Laplace mediante el método de relajación

En este resumen se desarrollan las ideas básicas para la implementación del método de relajación para la resolución de la ecuación de Laplace con condiciones de borde de Dirichlet.
## La ecuación de Poisson y la ecuación de Laplace

Para una distribución estática de carga, es posible encontrar el potencial, y por lo tanto el campo eléctrico mediante la resolución de la **ecuación de Poisson**

$$ \nabla^2 V = -\frac{\rho}{\epsilon_0} $$

Si se considera un dominio donde no haya cargas, esta ecuación se convierte en la **ecuación de Laplace**

$$ \nabla^2 V = 0 $$

El teorema de unicidad nos asegura que si encontramos una solución de la ecuacion de Laplace (o de Poisson) que cumpla con las condiciones de borde, 
hemos encontrado *la solución* de nuestro problema.

## Diferencias finitas
Estamos interesados en calcular la solución de forma numérica para una serie de puntos (nodos) sobre el dominio definido para nuestro problema (grilla).
Para resolver la ecuación de Laplace, discretizamos las derivadas aproximandolas mediante una ecuación de diferencias del tipo:

$$ \frac{\partial^2 V}{\partial x^2} \sim \frac{V_{i+1} - 2 V_i + V_{i-1}}{\Delta x^2} $$

donde el índice $i$ $(i = 0,1,2,...)$ se refiere al nodo $i$ de la grilla definida por nuestra discretización. En lo que resta de nuestro estudio, consideraremos una discretización uniforme del tipo
$\Delta x = \frac{L}{N-1}$, donde $L$ es el tamaño del dominio, $N$ la cantidad de nodos sobre dicho dominio para el cual calcularemos la solución. $\Delta x$ será entonces
la separación entre cada nodo consecutivo, tal que $x_{i+1} = x_{i} + \Delta x$.
Si reemplazamos esta ecuación por diferencias finitas en la ecuación de Laplace para una dimensión obtendremos la ecuación:

$$ \frac{V_{i+1} - 2 V_i + V_{i-1}}{\Delta x^2} = 0 $$ 

o despejando $V_i$ (**Ec. 1**)

$$ V_i = \frac{1}{2}(V_{i+1} + V_{i-1}) $$

Esta última ecuación nos indica que el valor de la solución en un nodo dependerá de la solución en los nodos vecinos.

## Dos y tres dimensiones

Se puede demostrar que en el caso de un problema bidimensional tendremos (**Ec. 2**)

$$ V_{i,j} = \frac{1}{4}(V_{i,j+1} + V_{i-1,j} + V_{i,j-1} + V_{i+1,j}) $$

y para el caso tridimensional (**Ec. 3**)

$$ V_{i,j,k} = \frac{1}{6}(V_{i,j+1,k} + V_{i-1,j,k} + V_{i,j-1,k} + V_{i+1,j,k} + V_{i,j,k+1} + V_{i,j,k-1}) $$

en donde se ha considerado una discretización uniforme e igual en cada dirección (i.e. $\Delta x = \Delta y = \Delta z = h$). 

## Método de relajación

Seguiremos el siguiente método para encontrar una solución númerica:

1. Definimos una discretización del dominio.
2. Indicamos las condiciones de borde de nuestro problema, dando los valores correspondientes a los nodos de los extremos: $V_0 = V^{\text{BORDE}}, V_{N-1} = V^{\text{BORDE}}$. En este estudio se consideraron condiciones de borde de Dirichlet. 
3. Inicializamos cada nodo interior con un valor de prueba, usualmente un valor constante.
4. Calculamos un nuevo valor para cada nodo  $V^{\text{NUEVO}}$, utilizando la ecuación correspondiente (1, 2 o 3).
5. Una vez que hayamos calculado el nuevo valor de $V$ para cada nodo interno, reemplazamos nuestra suposición inicial $V^{\text{VIEJO}}$ por dicho valor $V^{\text{NUEVO}}$ y repetimos el proceso desde *4*.
6. Se repiten los pasos *4* y *5* hasta que se haya alcanzado la precisión deseada (por ej. $\vert V^{\text{NUEVO}} - V^{\text{VIEJO}} \vert < \epsilon$) o se hayan realizado un número de iteraciones predeterminado.

Este esquema se conoce como método de Jacobi. Evidentemente se necesitará de dos *arreglos* para el cálculo del potencial. Una solución más eficiente es el método de Gauss-Seidel,
en el cual se reemplazan los valores $V^{\text{VIEJO}}$ con los $V^{\text{NUEVO}}$, apenas estos son calculados.

## Algunos resultados
Se resuelven las ecuaciones para el caso más sencillo, con valores de potencial constante en cada frontera.

### Caso unidimensional

Como hemos visto, en el caso unidimensional, la solución es de la forma $ V(x) = a x + b$, donde el valor de las constantes $a$ y $b$ depende de las condiciones de borde. En nuestro caso se considero un dominio de longitud $L = 1$, con condiciones de borde: $V(0) = V(L) = 5$, con lo cual la solución será $V(x) = 5$. Está solución nos permite analizar el método de relajación: podemos ver que ha medida que realizamos las iteraciones, los valores de los bordes *se propagan* al interior del dominio. 

[img1]: https://github.com/EliasMerida/laplace_relaxation_method/blob/main/1Dsol_evol.gif

![sol_evol][img1]

Para 19905 iteraciones realizadas la diferencia entre soluciones consecutivas es de $O(10^{-6})$.

[img2]: https://github.com/EliasMerida/laplace_relaxation_method/blob/main/1dlaplace.png

![laplace1d][img2]

Como hemos discutido previamente, se puede interpretar que la ecuación de Laplace nos indica que la solución en un punto es un *promedio* de la solución a derecha e izquierda. Además que no pueden tener máximos ni mínimos locales, los únicos valores extremos están en los bordes.

### Caso bidimensional
En el caso bidimensional se estudia un dominio cuadrado, con $L=1$, con condiciones de borde constantes:

i. $V(0,y) = 5$

ii. $V(L,y) = 5$

iii. $V(x,0) = 5$

iv. $V(x,L) = 5$

[img3]: https://github.com/EliasMerida/laplace_relaxation_method/blob/main/laplace2D.png

![laplace2d][img3]

La diferencia entre soluciones consecutivas, para 5000 iteraciones, es de $O(10^{-1})$.

[img4]: https://github.com/EliasMerida/laplace_relaxation_method/blob/main/laplace2D_contour.png
![laplace2d_countour][img4]

Tanto en el caso unidimensional como en el bidimensional se consideraron 100 nodos.

### Caso tridimensional
De manera análoga se considero una configuración en donde los bordes se encuentran un valor constante. A diferencia de los casos anterior, se trabajo como solo 10 nodos en cada dimensión, para aliviar el costo computacional de trabajar con arreglos con muchos elementos.

[img5]: https://github.com/EliasMerida/laplace_relaxation_method/blob/main/laplace3D_x_cte.png
[img6]: https://github.com/EliasMerida/laplace_relaxation_method/blob/main/laplace3D_y_cte.png
[img7]: https://github.com/EliasMerida/laplace_relaxation_method/blob/main/laplace3D_z_cte.png

Ya que es difícil visualizar el campo escalar tridimensional $V(x,y,z)$, se gráfico el potencial para 3 planos, justo en el centro de dicha dirección, es decir, se graficó $V(x,y,z)$ para $x = \frac{L}{2}", $y = \frac{L}{2}" y $z = \frac{L}{2}" 

![3Dx][img5]
![3Dy][img6]
![3Dz][img7]


## Bibliografía
1. John David Jackson, *Classical Electrodynamics*, 3rd edition. Wiley New York 1999.
2. David Jeffrey Griffiths, *Introduction to Electrodynamics*, 3rd edition. Prentice Hall 1999.