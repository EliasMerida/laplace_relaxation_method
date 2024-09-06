# Resolución de la Ecuación de Laplace mediante el método de relajación

En este resumen se desarrollan las ideas básicas para la implementación del método de relajación para la resolución de la ecuación de Laplace en 2 y 3 dimensiones con condiciones de borde de Dirichlet.
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

donde el índice $i$ se refiere al nodo $i$ de la grilla definida por nuestra discretización. En lo que resta de nuestro estudio, consideraremos una discretización uniforme del tipo
$\Delta x = \frac{L}{N-1}$, donde $L$ es el tamaño del dominio, $N$ la cantidad de nodos sobre dicho dominio para el cual calcularemos la solución. $\Delta x$ será entonces
la separación entre cada nodo consecutivo, tal que $x_{i+1} = x_{i} + \Delta x$.
Si reemplazamos esta ecuación por diferencias finitas en la ecuación de Laplace para una dimensión obtendremos la ecuación:

$$ \frac{V_{i+1} - 2 V_i + V_{i-1}}{\Delta x^2} = 0 $$ 

o despejando $V_i$

$$ V_i = \frac{1}{2}(V_{i+1} + V_{i-1}) $$

Esta última ecuación nos indica que el valor de la solución en un nodo dependerá de la solución en los nodos vecinos. 