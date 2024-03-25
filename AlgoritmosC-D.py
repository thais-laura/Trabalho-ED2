#!/usr/bin/env python
# coding: utf-8

# ## Algoritmo C

# In[24]:


import matplotlib.pyplot as plt
import numpy as np

x = [100, 500, 1000, 5000, 10000]
y1 = [45.61, 187.79, 392.4, 1999, 3886.4]
y2 = [39.89, 218.8, 397.8, 2032.3, 4234.9]
y3 = [40.17, 194.2, 404, 2071.7, 4153.1]
y4 = [43.18, 200.5, 375.5, 2080.7, 4132.3]

# Equação de regressão linear a partir das médias dos valores fornecidos
x1 = np.linspace(100, 10000, 100)
y5 =  0.411104*x1 - 9.85356

plt.plot(x, y2, '-ro', x, y2, '-ko', x, y3, '-go', x, y4, '-bo')
plt.plot(x1, y5, color='purple', linewidth=2.5)
plt.grid()
plt.xlabel('quantidade')
plt.ylabel('Duração [ms]')
plt.title('Duração do algoritmo C')
plt.legend(['ord cresc', 'ord decresc', 'aleat', 'aleat repet', 'regressao linear'])
plt.show()


# ## Algoritmo D

# In[23]:


import matplotlib.pyplot as plt
import numpy as np

x = [100, 500, 1000, 5000, 10000]
y1 = [0, 1.563, 3.124, 17.277, 40.779]
y2 = [0, 1.577, 3.13, 14.105, 41.129]
y3 = [0, 1.563, 3.16, 15.738, 37.591]
y4 = [0, 1.560, 3.126, 15.698, 31.393]

# Regressão quadrática a partir das médias dos valores fornecidos
x1 = np.linspace(100, 10000, 100)
y5 = 1.22751*(10**(-7))*(x1**2) + 0.00252862*x1 - 0.130907

plt.plot(x, y2, '-ro', x, y2, '-ko', x, y3, '-go', x, y4, '-bo')
plt.plot(x1, y5, color='purple', linewidth=2.5)
plt.grid()
plt.xlabel('quantidade')
plt.ylabel('Duração [ms]')
plt.title('Duração do algoritmo D')
plt.legend(['ord cresc', 'ord decresc', 'aleat', 'aleat repet', 'regressao quadratica'])
plt.show()

