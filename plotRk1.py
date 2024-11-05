import matplotlib.pyplot as plt

#Разница энергий
def dE(s1, s2, tm, m):
    #E = (m * V ^ 2)
    s1 /= 3.6
    e1 = m * s1 ** 2
    s2 /= 3.6
    e2 = m * s2 ** 2
    return (e2-e1) / tm
# print(dE(44, 50, 29.3, 33.5 * 1000))
# 25k, 35k,


speedKmH = [0, 1, 5, 7, 9, 12, 14, 19, 25, 30, 35, 46, 46]
amp = [160, 140, 120, 110, 100, 80, 75, 70, 55, 45, 42, 38.5, 0]
# speedKmH = [1, 5, 7, 9, 12, 14, 19, 25, 30, 35, 46]
# amp = [140, 120, 110, 100, 80, 75, 70, 55, 45, 42, 38.5]
rat = []
tur1 = []
tur2 = []
for i, n in enumerate(speedKmH):
    tur1.append(round(n / 3.6 / (0.78 * 3.14) * 5.33, 1))
    tur2.append(tur1[i] / (10 * 2.5))
    rat.append(round(amp[i]/160, 3))

    print(f"{speedKmH[i]:<2} {tur1[i]:<4} {amp[i]:<4}      {tur1[i]:<2} {rat[i]:<2} ")


plt.figure(figsize=(8, 8))
plt.plot(tur1, amp, marker='o', linestyle='-', color='b')
# Настройка графика
plt.xlabel('tur')
plt.ylabel('amp')
plt.grid()
# Отображение графика
plt.tight_layout()

plt.figure(figsize=(8, 8))
plt.plot(tur2, rat, marker='o', linestyle='-', color='g')
# Настройка графика
plt.xlabel('tur Scale')
plt.ylabel('rat Scale')
plt.grid()
# Отображение графика
plt.tight_layout()

plt.show()
