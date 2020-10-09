#!/usr/bin/env python
# coding: utf-8

# # Primer examen
# ## Geofísica Matemática y Computacional
# 
# - Alumno: Alan de la Fuente Bonfil
# - Prof. Luis Miguel de la Cruz Salas
# - Fecha: 08/10/2020

# In[14]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[63]:


# Función a ser evaluada
y = lambda x: (np.pi*(np.e-1))/2 * np.cos((np.pi*x)/2)
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


# In[66]:


# Función a ser evaluada
y= lambda x: (np.sin(x)/np.cos(x)) + (1/(np.cos**2(x)))*(x-1) + np.sin(np.pi*x) + np.pi*x*np.cos(np.pi*x)

# Dominio de la función
xmin = 0
xmax = 2
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


# In[ ]:





# In[67]:


# Función a ser evaluada
y = lambda x: np.sin(np.pi*x) + np.pi*np.cos(np.pi*x)-np.log(x)-((x-2)/x)

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


# ## Ejercicio 2.
# Calcular el error absoluto y relativo de las siguientes aproximaciones:
# - $p = \pi, pa = 22/7$
# - $p = e^(10), pa = 22000$
# - $p = 10^\pi, pa = 1400$
# - $p = 9!, pa = \sqrt{18*\pi}(9/e)^9$
# 

# In[6]:


Ea =np.fabs(np.pi - 22/7)
print(Ea)
Er = Ea/np.fabs(np.pi)
print(Er)
print('Error absoluto = {:.20f}'.format(Ea))
print('Error relativo = {:.20f}'.format(Er))


# In[12]:


Ea = np.fabs(np.e**10 - 22000)
print(Ea)
Er=Ea/np.fabs(np.e**10)
print(Er)


# In[8]:


fac=np.math.factorial(9)
Ea= fac -((18*np.pi)**(1/2))*(9/np.e)**9
print(Ea)
Er=Ea/fac
print(Er)


# In[62]:


Ea = (10**(np.pi)) - 1400
print(np.fabs(Ea))
Er=Ea/10**(np.pi)
print(np.fabs(Er))

