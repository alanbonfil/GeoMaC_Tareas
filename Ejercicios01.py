#!/usr/bin/env python
# coding: utf-8

# # Ejercicios para el primer examen
# ## Geofísica Matemática y Computacional
# 
# - Alumno: Alan de la Fuente Bonfil
# - Prof. Luis Miguel de la Cruz Salas
# - Rev: sáb oct  3 19:11:26 CDT 2020

# ## Ejercicio 1.
# Las ecuaciones siguientes tienen una solución en los intervalos que se mencionan:
# 
# 1. $x \cos(x) - 2x^2 + 3x - 1 = 0$ en $[0.2, 0.3]$ y $[1.2, 1.3]$
# 2. $(x-2)^2 - \ln(x) = 0$ en $[1,2]$ y $[e, 4]$
# 3. $2^x \cos(2x)-(x-2)^2 = 0$ en $[2,3]$ y $[3,4]$
# 4. $x - (\ln(x))^x = 0 $ en $[4,5]$
# 
# **Realice lo siguiente**:
# - Use el teorema del valor intermedio para mostrar que la solución existe en cada intervalo mencionado.
# - Gráfique la función usando el código de la celda siguiente y:
#     - Modifique la función a ser evaluada ($y$).
#     - Modifique el dominio de graficación de la función ($x$).
#     - Modifique los extremos del intervalo a evaluar ($A$ y $B$).

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Función a ser evaluada
y = lambda x: x * np.cos(x)-2 * x**2 + 3 * x - 1

# Dominio de la función
xmin = 0
xmax = 2
x = np.linspace(xmin, xmax, 100)

A = 1.2  # Extremo izquierdo del intervalo
B = 1.3  # Extremo derecho del intervalo

# Gráfica de la función
plt.plot(x,y(x), 'r-', lw=2)

# Líneas verticales en los extremos del intervalo y línea en y = 0
ymin = np.min(y(x))
ymax = np.max(y(x))
plt.plot([A,A], [ymin,ymax], 'g--', lw=1)
plt.plot([B,B], [ymin,ymax], 'g--', lw=1)
plt.plot([xmin, xmax], [0,0], 'b-', lw=1)

plt.grid()
plt.show()


# In[11]:


# Función a ser evaluada
#y = lambda x: x * np.cos(x)-2 * x**2 + 3 * x - 1
y= lambda x: 2**x * np.cos(2x) - (x-2)**2

# Dominio de la función
xmin = 0
xmax = 2
x = np.linspace(xmin, xmax, 100)

A = 3  # Extremo izquierdo del intervalo
B = 4  # Extremo derecho del intervalo

# Gráfica de la función
plt.plot(x,y(x), 'r-', lw=2)

# Líneas verticales en los extremos del intervalo y línea en y = 0
ymin = np.min(y(x))
ymax = np.max(y(x))
plt.plot([A,A], [ymin,ymax], 'g--', lw=1)
plt.plot([B,B], [ymin,ymax], 'g--', lw=1)
plt.plot([xmin, xmax], [0,0], 'b-', lw=1)

plt.grid()
plt.show()


# ## Ejercicio 2.
# Calcular el segundo polinomio de Taylor $P_2(x)$ de la función $f(x) = e^x \cos(x)$ alrededor de $x_0 = 0$, así como el error $R_2(x)$ de acuerdo con el Teorema de Taylor.
# 
# $P_2(x) = 1 + x$
# 
# $R_2(X) = \frac{-2e^\xi (\sin \xi + \cos\xi)}{3!} x^3$
# 
# **Realice lo siguiente**:
# 
# - Aproximar $f(x)$ usando $P_2(x)$ en $x = 0.5$ y calcular el error absoluto y relativo de la aproximación. 
# - ¿Cómo se compara el error absoluto con la fórmula del error $R_2(x)$? **Hint**: encuentre una cota máxima de $R_2(x)$ en $[0,0.5]$.
# - Encuentre una cota para $R_2(x)$ en el intervalo $[0,1]$.
# - Aproximar la integral $\int_0^1 f(x) dx$ usando $\int_0^1 P_2(x) dx$.
# - Calcule la integral exacta de $\int_0^1 f(x) dx$ y compare con el error absoluto de la aproximación anterior. ¿Cómo se compara este resultado con el error calculado de la siguiente manera $\int_0^1 |R_2(x)| dx$?
# - Haga una gráfica de $f(x)$ y $P_2(x)$ en el intervalo $[0, 0.5]$. Decore la gráfica con una leyenda para cada una de las curvas, etiqueta en los ejes, y un título que diga: "$|f(0.5)-P_2(0.5)| = E_a$" donde $E_a$ es el error absoluto en $x=0.5$.

# In[20]:


f = lambda x: np.exp(1)**x * np.cos(x)
P2= lambda x: 1 + x

Ea= np.fabs(f(0.5)-P2(0.5))
print(Ea)

x = np.linspace (0, 0.5, 20)

plt.plot(x, f(x), lw=2, label='$f(x)=e^x cos(x)$')
plt.plot(x,P2(x), lw=2, label='$P_2(X)$')
plt.title('El titulo')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


# ## Ejercicio 3.
# Calcular el error absoluto y relativo de las siguientes aproximaciones:
# - $p = \pi, pa = 3.1416$
# - $p = e, pa = 2.718$
# - $p = 8!, pa = 39900$
# - $p = \sqrt{2}, pa = 1.4142$
# - $p = \sqrt{2}, pa = 1.414213$
# - $p = \frac{4}{5} + \frac{1}{3}, pa = round(p,3)$
# - $p = \frac{1}{3}-\frac{3}{11}+\frac{3}{20}, pa = round(p,3)$
# - $p = \frac{1}{3}-\frac{3}{11}+\frac{3}{20}, pa =$ truncamiento de $p$ a $3$ dígitos.

# In[42]:


Ea =np.fabs(np.pi - 3.1416)
print(Ea)
Er = Ea/np.fabs(np.pi)
print(Er)
print('Error absoluto = {:.20f}'.format(Ea))
print('Error relativo = {:.20f}'.format(Er))


# In[26]:


Ea = np.fabs(np.e - 2.718)
print(Ea)
Er=Ea/np.fabs(np.e)
print(Er)


# In[33]:


fac=np.math.factorial(8)
Ea= fac -39900
print(Ea)
Er=Ea/fac
print(Er)


# In[36]:


Ea = 2**1/2 - 1.4142
print(Ea)
Er=Ea/2**1/2
print(Er)


# In[39]:


Ea= 2**1/2 -1.414213
print(Ea)
Er=Ea/2**1/2
print(Er)


# In[48]:


ha =(4/5 + 1/3)
has=round(ha,3)
Ea= ha - has
Er= Ea/Er
print(Ea)
print(Er)


# In[3]:


po=(1/3 -3/11 +3/20)
pop=round(po,3)
Ea=po-pop
Er=Ea/po
print(po)
print(pop)
print(Ea)
print(Er)


# In[4]:


po=(1/3 -3/11 +3/20)
pop=round(po,3)
Ea=po-pop
Er=Ea/po
print('Error absoluto = {:.3f}'.format(Ea))
print('Error relativo = {:.3f}'.format(Er))


# ## Ejercicio 4.
# Suponga que tenemos dos puntos en el plano Cartesiano $(x_0, y_0)$ y $(x_1, y_1)$ con $y_0 \neq y_1$. Las siguientes dos fórmulas calculan en dónde es que esta línea cruza al eje $x$:
# $$
# x = \frac{x_0y_1 - x_1y_0}{y_1-y_0} 
# \quad \quad \text{y} \quad \quad
# x = x_0 - \frac{(x_1 - x_0)y_0}{y_1-y_0} 
# $$
# 
# **Realizar lo siguiente**:
# - Mostrar que ambas fórmulas son equivalentes. **Hint**: calcular la fórmula de la recta que pasa por ambos puntos y luego evaluarla cuando $y=0$ y despejar $x$.
# - Usar los siguientes datos $(x_0, y_0) = (1.31, 3.24)$ y $(x_1, y_1) = (1.93, 4.76)$ y una aritmética de redondeo a 6 dígitos para calcular $x$ usando las dos fórmulas anteriores. ¿Puede determinar cuál de las dos fórmulas es mejor y por qué? 
# 
# **Hint**: Evalue primero usando la precisión por omisión: 
# ```python
# # Primera fórmula
# def f1(x0,y0,x1,y1):
#     return (x0*y1 - x1*y0) /(y1 - y0)
# # Segunda fórmula
# def f2(x0,y0,x1,y1):
#     return x0 - (x1 - x0)*y0 /(y1 - y0)
# # Evaluación sin redondeo
# f1_e = f1(1.31,3.24,1.93,4.76)
# f2_e = f2(1.31,3.24,1.93,4.76)
# print('f1 = {:.55f}'.format(f1_e))
# print('f2 = {:.55f}'.format(f2_e))
# ```
# Posteriormente evalue usando redondeo:
# 
# ```python
# # Usamos las siguiente bibliotecas para redondear
# from decimal import getcontext, Decimal 
# getcontext().prec=6 # precisión a 6 dígitos
# print(getcontext())
# # Evaluamos con redondeo
# (x0, y0) = (Decimal(1.31),Decimal(3.24))
# (x1, y1) = (Decimal(1.93),Decimal(4.76))
# print('\n {:.6f} \t {:.6f} \t {:.6f} \t {:.6f} \n'.format(x0,y0,x1,y1))
# f1_a = f1(x0,y0,x1,y1)
# f2_a = f2(x0,y0,x1,y1)
# print('f1 = {:.10f}'.format(f1_a))
# print('f2 = {:.10f}'.format(f2_a))
# ```
# Ahora calcule el error absoluto y relativo comparando con los primeros resultados.
# 
# ```python
# E1_a = np.fabs(f1_e - float(f1_a))
# E2_a = np.fabs(f2_e - float(f2_a))
# E1_r = E1_a / np.fabs(f1_e)
# E2_r = E2_a / np.fabs(f2_e)
# print('Error absoluto f1: {:.55f}'.format(E1_a))
# print('Error absoluto f2: {:.55f}'.format(E2_a))
# print('Error relativo f1: {:.55f}'.format(E1_r))
# print('Error relativo f2: {:.55f}'.format(E2_r))
# ```

# In[ ]:





# ## Ejercicio 5. 
# La secuencia $\{F_n\}$ descrita por $F_0 = 1, F_1 = 1$, y $F_{n+2}$ = $F_n + F_{n+1}$, si $n \geq 0$, se conoce como la secuencia de Fibonacci. Sus términos ocurren naturalmente en especies botánicas, particularmente en aquellas con pétalos o escalas que se arreglan en forma de espiral logarítmica. 
# 
# Considere la secuencia $\{x_n\}$, donde $x_n = F_{n+1} / F_n$. El límite
# $\lim_{n \to \infty} x_n = x$ existe y es: 
# $$
# \displaystyle x = \frac{1 + \sqrt{5}}{2} \quad \text{(golden ratio)} 
# $$
# Escribir un algoritmo para aproximar $x$ y dada una $n$, calcular el error absoluto y el error relativo de la aproximación. Grafique la secuencia $x$.
# 
# **Hint**: calcule los números de Fibonacci y posteriormente la secuencia $x_n$. 
