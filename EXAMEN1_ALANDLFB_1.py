#!/usr/bin/env python
# coding: utf-8

# # Primer examen
# ## Geofísica Matemática y Computacional
# 
# - Alumno: Alan de la Fuente Bonfil
# - Prof. Luis Miguel de la Cruz Salas
# - Fecha: 08/10/2020

# In[23]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Ejercicio 1.
# ¿En qué intervalo de la derivada de las siguientes funciones se hace cero?
# - $f(x) = 1 - e^x + (e-1)\sin(\frac{\pi x}{2}),$ <br>
# - $f(x) = (x - 1)\tan x + x \pi x,sin \pi x,$ <br>
# - $f(x) = x \sin \pi x - (x-2) \ln x, $ <br>
# - $f(x) = (x - 2) \sin x \ln(x + 2), $ <br>
# 
# **Realizar lo siguiente**
# - Grafique las siguientes funciones para mostrar que su derivada se hace cero en los intervalos proporcionados.
# - Muestre que $f^\prime(x)$ se hace cero en los intervalos correspondientes.

# In[35]:


# Función a ser evaluada
y = lambda x: 1- np.exp(x)+(np.exp(1)-1)*np.sin(np.pi*x/2)
#y = lambda x : 1 - (np.e**x) + (np.e-1)*np.sin((np.pi*x/2)

# Dominio de la función
xmin = 0
xmax = 2
x = np.linspace(xmin, xmax, 100)

A = 0  # Extremo izquierdo del intervalo
B = 1  # Extremo derecho del intervalo

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


# In[36]:


# Función a ser evaluada
y= lambda x: (x-1)*np.tan(x)+x*np.sin(np.pi*x)

# Dominio de la función
xmin = 0
xmax = 1
x = np.linspace(xmin, xmax, 100)

A = 0  # Extremo izquierdo del intervalo
B = 0.4  # Extremo derecho del intervalo

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


# In[37]:


# Función a ser evaluada
y = lambda x: x*np.sin(np.pi*x) - (x-2)*np.log(x)

# Dominio de la función
xmin = 0
xmax = 2
x = np.linspace(xmin, xmax, 100)

A = 1  # Extremo izquierdo del intervalo
B = 2  # Extremo derecho del intervalo

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


# In[38]:


# Función a ser evaluada
y = lambda x: (x-2)*np.sin(x)*np.log(x+2)
# Dominio de la función
xmin = -1
xmax = 0
x = np.linspace(xmin, xmax, 100)

A = 1  # Extremo izquierdo del intervalo
B = 2  # Extremo derecho del intervalo

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
# Calcular el error absoluto y relativo de las siguientes aproximaciones:
# - $p = \pi, pa = 22/7$
# - $p = e^{10} , pa = 22000$
# - $p = 10^\pi, pa = 1400$
# - $p = 9!, pa = \sqrt{18\pi}(9/e)^9$
# 

# In[41]:


Ea =np.fabs(np.pi - 22/7)
Er = Ea/np.fabs(np.pi)
print('Error absoluto = {:.20f}'.format(Ea))
print('Error relativo = {:.20f}'.format(Er))


# In[40]:


Ea = np.fabs(np.e**10 - 22000)
Er=Ea/np.fabs(np.e**10)
print('Error absoluto = {:.20f}'.format(Ea))
print('Error relativo = {:.20f}'.format(Er))


# In[42]:


fac=np.math.factorial(9)
Ea= fac -((18*np.pi)**(1/2))*(9/np.e)**9
Er=Ea/fac
print('Error absoluto = {:.20f}'.format(Ea))
print('Error relativo = {:.20f}'.format(Er))


# In[46]:


Ea = (10**(np.pi)) - 1400
print(np.fabs(Ea))
Er=Ea/10**(np.pi)
print(np.fabs(Er))


# ## Ejercicio 3.
# El polinomio de Taylor de grado $n$ de la función 
# $f(x) = e^x$ es
# $\displaystyle P_n(x) = \sum_{i=0}^n \frac{x^i}
# {i!}$. Usando el Polinomio de Taylor de grado $9$ podemos aproximar $e^{-5}$ usando los siguientes dos métodos:
# 
# a. $\displaystyle e^{-5} \approx \sum_{i=0}^n \frac{(-5)^i}{i!}= \sum_{i=0}^n \frac{(-1)^i 5^i} {i!}$ <br>
# 
# b. $\displaystyle e^{-5} = \frac{1}{e^5} \approx \frac{1} {\sum_{i=0}^n \frac{5^i}{i!}}$
# 
# ¿Cuál de los 2 fórmulas anteriores da una mejor aproximación? ¿por qué?
# 

# In[52]:


def aprox_a(x,n):
    suma = 0
    for i in range(0,n+1):
        suma += (-1)**i * 5**i/ np.math.factorial(i)
    return suma    

def aprox_b(x,n):
    suma = 0
    for i in range(0,n+1):
        suma += (5)**i / np.math.factorial(i)
    return 1 / suma 


# In[53]:


x = -5
n = 20
e1 = aprox_a(x,n)
e2 = aprox_b(x,n)

print('e = {:.55f}'.format(np.exp(-5)))
print('e = {:.55f}'.format(e1))
print('e = {:.55f}'.format(e2))


# ## Respuesta 3.
# El método "b" aporta una mejor aproximación, debido a que el método "a" conlleva elevar
# el -1 a la i y eso lleva a una oscilación, se requerirían mas elementos de la serie de Taylor para quitar la inestabilidad
# por lo que la aproximación "b" es la mejor ya que converge en la solución mas estable.
# 

# In[ ]:





# In[ ]:




