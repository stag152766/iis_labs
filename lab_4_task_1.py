#  Загрузим необходимые бибилиотеки и подготовим данные

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = x * 2
z = x ** 2

# Задача 1

# Выполните следующие шаги
# Создайте объект класса Figure используя метод plt.figure()
# Используйте add_axes чтобы добавить оси, занимающие все полотно фигруы
# Изобразите на полученном графике связь между x и y, чтобы плолучился похожий результат


fig = plt.figure()


axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes.plot(y,z,'b')
axes.set_xlabel('Ось х')
axes.set_ylabel('Ось у')
axes.set_title('Заголовок')


# Задача 2
# Создайте на одном полотке две пары осей, чтобы получилась похожая картинка

fig = plt.figure()

axes1= fig.add_axes([0.1,0.1,0.8,0.8])
axes2= fig.add_axes([0.6,0.5,0.2,0.2])

axes1.plot(x,y, 'b')


axes2.plot(y,x, 'r')


plt.show()