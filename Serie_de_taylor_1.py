import numpy as np
from math import e
from math import factorial
import matplotlib.pyplot as plt
x = np.arange(-5, 5, 0.1)
y = np.zeros(len(x))

# Função Padrão
def f(x):
    return e**(x-1)
# Função aplicada na série de Taylor
def serie(x,i):
    y = 0
    for n in range(i+1):
      y = y + (x**n)/(factorial(n)*e)
    return y
print(f(3))
print(serie(3,20))

plt.style.use('seaborn-poster')

# e^(x-1)
fig, ax = plt.subplots()
fig.set_dpi(30)
plt.plot(x,f(x), label = "e^(x-1)")
plt.grid()
ax.set(title='f(x) = e^(x-1)', ylabel = 'y', xlabel = 'x')
plt.legend()
plt.show()

# x^2/n!*e
fig, ax = plt.subplots()
fig.set_dpi(30)

for n in range(21):
    if(n==1):
      plt.plot(x,serie(x,n), label = n)
plt.grid()
ax.set(title='f(x) = x^2/n!*e', ylabel = 'y', xlabel = 'x')
plt.legend()
plt.show()

fig, ax = plt.subplots()
fig.set_dpi(30)
plt.plot(x,f(x), label = "e^(x-1)")
for n in range(21):
    if(n==20):
      plt.plot(x,serie(x,n), label = n)
ax.set(title='Juntando', ylabel = 'y', xlabel = 'x')
plt.legend()
plt.show()
