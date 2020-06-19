import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

print(x)
print(y)

plt.plot(x, y, 'r')
plt.xlabel('Ось х')
plt.ylabel('Ось у')
plt.title('График')
#plt.show()

plt.subplot(1,2,1)
plt.plot(x,y,'r--')
plt.show()
plt.subplot(1,2,2)
plt.plot(y,x,'g*-')
#plt.show()

# ООП стиль

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes.plot(x,y,'b')
axes.set_xlabel('Ось х')
axes.set_ylabel('Ось у')
axes.set_title('Заголовок')

#plt.show()


fig = plt.figure()

axes1= fig.add_axes([0.1,0.1,0.8,0.8])
axes2= fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y, 'b')
axes1.set_xlabel('Подпись Х большого графика')
axes1.set_ylabel('Подпись У большого графика')
axes1.set_title('Заголовок большого графика')

axes2.plot(y,x, 'r')
axes2.set_xlabel('Подпись Х малого графика')
axes2.set_ylabel('Подпись У малого графика')
axes2.set_title('Заголовок малого графика')

#plt.show()


fig, axes = plt.subplots()

axes.plot(x,y,'r')

axes.plot(x,y,'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Заголовок')

#plt.show()


fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x,y, 'b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Заголовок')


fig, axes = plt.subplots(nrows=1, nclos=2)

for ax in axes:
    ax.plot(x,y,'g')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Заголовок')


plt.tight_layout()







plt.show()
