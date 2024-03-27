import matplotlib.pyplot as plt
import numpy as np

x = [100, 500, 1000, 5000, 10000]
y1 = [0.199, 2.294, 3.787, 15.36, 36.48] 
y2 = [0.194, 1.599, 3.586, 22.54, 32.71] 
y3 = [0.199, 1.395, 2.991, 16.45, 34.61] 
y4 = [0.299, 1.594, 3.972, 16.06, 32.99] 

#media1= 0.22275
#media2= 1.7205
#media3= 3.584
#media4= 17.6025
#media5= 34.1975

# Equação de regressão linear a partir das médias dos valores fornecidos
x1 = np.linspace(100, 10000, 100)
y5 =  0.00343126*x1 + 0.0736543

plt.plot(x, y1, '-ro', x, y2, '-ko', x, y3, '-go', x, y4, '-bo')
plt.plot(x1, y5, color='purple', linewidth=2.5)
plt.grid()
plt.xlabel('quantidade')
plt.ylabel('Duração [ms]')
plt.title('Duração do algoritmo C')
plt.legend(['ord cresc', 'ord decresc', 'aleat', 'aleat repet', 'regressao linear'])
plt.show()
