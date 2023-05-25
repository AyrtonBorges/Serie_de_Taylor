import numpy as np
from math import e
from math import factorial
import matplotlib.pyplot as plt
x = np.arange(-1.1,1.1,0.01)
y = np.zeros(len(x))

# Função Padrão
def f(x):
    return np.log((x**2+1))
# Função aplicada na série de Taylor
def serie(x,i):
    y = 0
    for n in range(1,i+1):
      y += (((-1)**(n+1))/n)*(x**(2*n))
    return y

print(f(0.2))
print(serie(0.2,20))

plt.style.use('seaborn-poster')
# ln(x**2+1)
fig, ax = plt.subplots()
fig.set_dpi(30)
plt.plot(x,f(x), label = "ln(x^2+1)")
plt.grid()
ax.set(title='f(x) = ln(x^2+1)', ylabel = 'y', xlabel = 'x')
plt.legend()
plt.show()

# (((-1)**(n+1))/n)*(x**(2*n))
fig, ax = plt.subplots()
fig.set_dpi(30)

for n in range(21):
    if(n):
      plt.plot(x,serie(x,n), label = n)
plt.grid()
ax.set(title='f(x) = (((-1)**(n+1))/n)*(x**(2*n))', ylabel = 'y', xlabel = 'x')
plt.legend()
plt.show()

fig, ax = plt.subplots()
fig.set_dpi(30)
plt.plot(x,f(x), label = "ln(x^2+1)")
for n in range(21):
    if(n==20):
      plt.plot(x,serie(x,n), label = n)
ax.set(title='Juntando', ylabel = 'y', xlabel = 'x')
plt.legend()
plt.show()
