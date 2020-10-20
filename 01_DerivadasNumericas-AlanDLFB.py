#!/usr/bin/env python
# coding: utf-8

# # Cálculo de derivadas numéricas
# ## Proyecto PAPIME PE101019
# - Autor: Luis M. de la Cruz Salas
# - Alumno: Alan De La Fuente Bonfil 

# In[34]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.style.use('seaborn-talk')


# In[35]:


params = {'figure.figsize' : (10,5),
#          'text.usetex'    : True,
          'xtick.labelsize': 15,
          'ytick.labelsize': 15,
          'axes.labelsize' : 20,
          'axes.titlesize' : 20,
          'legend.fontsize': 15,
          'lines.linewidth'     : 3}

plt.rcParams.update(params)


# ### Aproximación de la primera derivada usando diferencias finitas hacia adelante (Forward):
# 
# $
# \displaystyle
# \dfrac{\partial u(x)}{\partial x} \approx \lim\limits_{h\to 0} \frac{u(x+h) - u(x)}{h}
# $
# 
# Definimos una función de Python para calcular está formula como sigue:

# In[36]:


def forwardFD(u,x,h):
    """ 
    Esquema de diferencias finitas hacia adelante.
    
    Parameters
    ----------
    u : función. 
    Función a evaluar.
    
    x : array
    Lugar(es) donde se evalúa la función
    
    h : array
    Tamaño(s) de la diferencia entre u(x+h) y u(x).
    
    Returns
    -------
    Cálculo de la derivada numérica hacia adelante.
    """
    return (u(x+h)-u(x))/h


# In[37]:


# Definimos un arreglo con diferentes tamaños de h:
N = 6
h = np.zeros(N)

h[0] = 1.0
for i in range(1,N):
    h[i] = h[i-1] * 0.5

# Definimos un arreglo con valores de 1.0 (donde evaluaremos el cos(x)):
x = np.ones(N)

print(h)
print(x)


# In[38]:


# Calculamos el error entre la derivada exacta y la derivada numérica:
ef = np.fabs( np.cos(x) - forwardFD(np.sin,x,h) )

# Colocamos la información de h y del error en un Dataframe y mostramos el resultado:
Error = pd.DataFrame(np.array([h, ef]).transpose(), 
                     columns=['$h$','$D_+$'])
Error


# In[39]:


# Hacemos el gráfico del error vs h
plt.plot(h, ef, '^-', label='$D_+$')
plt.xlabel('$h$')
plt.ylabel('Error')
plt.title('Aproximación de la derivada')
plt.legend()
plt.show()


# ### Aproximación de la primera derivada usando diferencias finitas hacia atrás (Backward):
# 
# $
# \displaystyle
# \frac{\partial u(x)}{\partial x} \approx \lim\limits_{h\to 0} \frac{u(x) - u(x-h)}{h}
# $
# 
# Definimos una función de Python para calcular está formula como sigue:

# In[40]:


def backwardFD(u,x,h):
    """ 
    Esquema de diferencias finitas hacia atrás.
    
    Parameters
    ----------
    u : función. 
    Función a evaluar.
    
    x : array
    Lugar(es) donde se evalúa la función
    
    h : array
    Tamaño(s) de la diferencia entre u(x+h) y u(x).
    
    Returns
    -------
    Cálculo de la derivada numérica hacia atrás.
    """
    return (u(x)-u(x-h))/h


# In[41]:


# Calculamos el error entre la derivada exacta y la derivada numérica:
eb = np.fabs( np.cos(x) - backwardFD(np.sin,x,h) )

# Metemos la información de h y del error en un Dataframe y mostramos el resultado:
Error = pd.DataFrame(np.array([h, ef, eb]).transpose(), 
                     columns=['$h$','$D_+$', '$D_-$'])
Error


# In[42]:


# Hacemos el gráfico del error vs h
plt.plot(h, ef, '^-', label='$D_+$')
plt.plot(h, eb, 'v-', label='$D_-$')
plt.xlabel('$h$')
plt.ylabel('Error')
plt.title('Aproximación de la derivada')
plt.legend()
plt.show()


# ### Aproximación de la primera derivada usando diferencias finitas hacía centradas (Centered):
# 
# $
# \displaystyle
# \frac{\partial u(x)}{\partial x} \approx \lim\limits_{h\to 0} \frac{u(x+h) - u(x-h)}{2h}
# $
# 
# Definimos una función de Python para calcular está formula como sigue:

# In[43]:


def centeredFD(u,x,h):
    """ 
    Esquema de diferencias finitas centradas.
    
    Parameters
    ----------
    u : función. 
    Función a evaluar.
    
    x : array
    Lugar(es) donde se evalúa la función
    
    h : array
    Tamaño(s) de la diferencia entre u(x+h) y u(x).
    
    Returns
    -------
    Cálculo de la derivada numérica centrada.
    """
    return (u(x+h)-u(x-h))/(2*h)


# In[44]:


# Calculamos el error entre la derivada exacta y la derivada numérica:
ec = np.fabs( np.cos(x) - centeredFD(np.sin,x,h) )

# Metemos la información de h y del error en un Dataframe y mostramos el resultado:
Error = pd.DataFrame(np.array([h,ef,eb,ec]).transpose(), 
                     columns=['$h$','$D_+$', '$D_-$','$D_0$'])
Error


# Observe que en este caso los errores son varios órdenes de magnitud más pequeños que para $D_+$ y $D_-$. Para hacer una gráfica más representativa usaremos escala log-log:

# In[45]:


# Hacemos el gráfico del error vs h
plt.plot(h, ef, '^-', label='$D_+$')
plt.plot(h, eb, 'v-', label='$D_-$')
plt.plot(h, ec, 's-', label='$D_0$')
plt.xlabel('$h$')
plt.ylabel('Error')
plt.title('Aproximación de la derivada')
plt.legend()
plt.loglog()  # Definimos la escala log-log
plt.show()


# Como se puede apreciar, la gráfica anterior muestra que la aproximación con diferencias finitas centradas es mejor, pues es de orden cuadrático.

# ## Ejercicio 0.
# Para mejorar aún más la aproximación de la derivada se pueden usar más puntos en la fórmula de aproximación. Por ejemplo: 
# 
# $
# D_3 u = \dfrac{1}{6 h} 
# \left[ 2u_{i+1} + 3u_{i} - 6u_{i-1} + u_{i-2} \right]
# $
# 
# - Agregar una función de Python para calcular la derivada con la fórmula anterior.
# - Calcular el error, completar la tabla de errores y hacer el gráfico con todas las aproximaciones. 
# 
# Al final de este ejercicio se debe obtener un gráfico similar al de la siguiente figura:
# 
# <img src="../Figuras/dernum.png">
# 
# **Hint**: Recuerde que $u_i = u(x)$, $u_{i+1} = u(x+h)$, $u_{i-1} = u(x-h)$ y $u_{i-2} = u(x-2h)$.

# In[46]:


# Implementación de D3
def d3FD(u,x,h):
    """ 
    Esquema de diferencias finitas centradas.
    
    Parameters
    ----------
    u : función. 
    Función a evaluar.
    
    x : array
    Lugar(es) donde se evalúa la función
    
    h : array
    Tamaño(s) de la diferencia entre u(x+h) y u(x).
    
    Returns
    -------
    Cálculo de la derivada numérica centrada.
    """
    return ((2*u(x+h))+3*u(x)-6*u(x-h)+u(x-2*h))/(6*h)


# In[47]:


# Calculamos el error entre la derivada exacta y la derivada numérica:
ed = np.fabs( np.cos(x) - d3FD(np.sin,x,h) )

# Metemos la información de h y del error en un Dataframe y mostramos el resultado:
Error = pd.DataFrame(np.array([h,ef,eb,ec,ed]).transpose(), 
                     columns=['$h$','$D_+$', '$D_-$','$D_0$','$D_3$'])
Error


# In[48]:


# Hacemos el gráfico del error vs h
plt.plot(h, ef, '^-', label='$D_+$')
plt.plot(h, eb, 'v-', label='$D_-$')
plt.plot(h, ec, 's-', label='$D_0$')
plt.plot(h, ed, 's-', label='$D_3$')
plt.xlabel('$h$')
plt.ylabel('Error')
plt.title('Aproximación de la derivada')
plt.legend()
plt.loglog()  # Definimos la escala log-log
plt.show()


# # Herramienta interativa
# La siguiente herramienta tiene como propósito mostras diferentes funciones y sus derivadas exactas así como el cálculo numérico de las derivadas usando varias aproximaciones. Puedes elegir la función y el tipo de aproximación. Después, puedes mover el punto donde se realiza la aproximación y el tamaño de la $h$.

# In[49]:


# LINUX y MACOS
#%run "./utils/interactiveDerivadasNumericas.ipynb"

# Si usas WINDOWS debes comentar la línea de arriba y 
# descomentar la línea que sigue. Deberás también sustituir
# TU_DIRECTORIO por el directorio donde esté el repositorio GeoMaC

#%run "C:\\Users\\aland\\GeoMac_Tareas\\GeoMaC\\DerivadasNumericas\\utils\\interactiveDerivadasNumericas.ipynb"


# ## Ejercicio 1.
# Implementar la siguiente aproximación y graficarla junto con todos los resultados anteriores:
# 
# $$
# f^\prime = \frac{3 f_i - 4 f_{i-1} + f_{i-2}}{2h}
# $$

# In[50]:


# Implementación de D2
def D2B(u,x,h):
    """ 
    Esquema de diferencias finitas centradas.
    
    Parameters
    ----------
    u : función. 
    Función a evaluar.
    
    x : array
    Lugar(es) donde se evalúa la función
    
    h : array
    Tamaño(s) de la diferencia entre u(x+h) y u(x).
    
    Returns
    -------
    Cálculo de la derivada numérica .
    """
    return (1/(2*h))*(3*(u(x))-4*u(x-h)+u(x-(2*h)))


# In[52]:


# Calculamos el error entre la derivada exacta y la derivada numérica:
e2b = np.fabs( np.cos(x) - D2B(np.sin,x,h))

# Metemos la información de h y del error en un Dataframe y mostramos el resultado:
Error = pd.DataFrame(np.array([h,ef,eb,ec,ed,e2b]).transpose(), 
                     columns=['$h$','$D_+$', '$D_-$','$D_0$','$D_3$','$D_2$'])
Error


# In[53]:


# Hacemos el gráfico del error vs h
plt.plot(h, ef, '^-', label='$D_+$')
plt.plot(h, eb, 'v-', label='$D_-$')
plt.plot(h, ec, 's-', label='$D_0$')
plt.plot(h, ed, 's-', label='$D_3$')
plt.plot(h, e2b, 's-', label='$D_2$')
plt.xlabel('$h$')
plt.ylabel('Error')
plt.title('Aproximación de la derivada')
plt.legend()
plt.loglog()  # Definimos la escala log-log
plt.show()


# ## Ejercicio 2.
# Obtener los coeficientes $A$, $B$ y $C$ para una aproximación del siguiente tipo: 
# 
# $$
# f^\prime = A f_i + B f_{i+1} + C f_{i+2}
# $$
# 
# y luego implementar la fórmula y graficarla junto con los resultados anteriores.
# 
# ¿Cuál de todas las aproximaciones usaría? ¿Por qué?

# In[54]:


# Implementación hacia adelante
def Df2(u,x,h):
    """ 
    Esquema de diferencias finitas centradas.
    
    Parameters
    ----------
    u : función. 
    Función a evaluar.
    
    x : array
    Lugar(es) donde se evalúa la función
    
    h : array
    Tamaño(s) de la diferencia entre u(x+h) y u(x).
    
    Returns
    -------
    Cálculo de la derivada numérica .
    """
    return (1/(2*h))*(-3*(u(x))+4*u(x+h)-u(x+(2*h)))


# In[63]:


# Calculamos el error entre la derivada exacta y la derivada numérica:
ef2 = np.fabs( np.cos(x) - Df2(np.sin,x,h))

# Metemos la información de h y del error en un Dataframe y mostramos el resultado:
Error = pd.DataFrame(np.array([h,ef,eb,ec,ed,e2b,ef2]).transpose(), 
                     columns=['$h$','$D_+$', '$D_-$','$D_0$','$D_3$','$D_-2$','$D_+2$'])
Error


# In[56]:


# Hacemos el gráfico del error vs h
plt.plot(h, ef, '^-', label='$D_+$')
plt.plot(h, eb, 'v-', label='$D_-$')
plt.plot(h, ec, 's-', label='$D_0$')
plt.plot(h, ed, 's-', label='$D_3$')
plt.plot(h, e2b, 's-', label='$D_2$')
plt.plot(h, ef2, 's-', label='$D_+2$')
plt.xlabel('$h$')
plt.ylabel('Error')
plt.title('Aproximación de la derivada')
plt.legend()
plt.loglog()  # Definimos la escala log-log
plt.show()


# In[66]:


## Respuesta Ejercicio 2.
La mejor aproximación es la D3 porque involucra elementos anteriores a i y posteriores a i, 
contiene un menor error y mayor aproximación


# In[ ]:




