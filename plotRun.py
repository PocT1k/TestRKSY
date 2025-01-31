import matplotlib.pyplot as plt
import math

# Чтение данных из файла
file = 'Файлы\\logs2-turn30'
file = 'logs'
with open(file + '.txt', 'r') as file:
    lines = file.readlines()
# Извлечение заголовков из первой строки
headers = lines[0].strip().split(';')  # Получаем заголовки и разбиваем по разделителю ';'
colors = 'rgb'
plt.figure(figsize=(19, 10))

toSoloBuild = [7, 5, 6, 13]
toRelation = [4, 6]
numPlots = len(toSoloBuild)
# Определяем количество строк и столбцов для подграфиков
nRows = math.ceil(math.sqrt(numPlots)) # Количество строк
nCols = math.ceil(numPlots / nRows) # Количество столбцов


#Удаляем ласт строку, если она не дописана
counterDataRow = len(lines[2].split(';'))
if len(lines[-1].split(';')) != counterDataRow:
    lines.pop()

dataColT = [float(line.strip().split(';')[0]) for line in lines[2:]]
for i, build in enumerate(toSoloBuild):
    # Извлечение значений, пропуская первую строку (заголовок)
    dataCol = [float(line.strip().split(';')[build]) for line in lines[2:]]

    plt.subplot(nCols, nRows, i + 1)  # 1 строка, 2 столбца, 1-й график
    plt.plot(dataColT, dataCol, marker='o', linestyle='-', color=colors[i % len(colors)])
    plt.title(f"{build} {headers[build]}")
    plt.xlabel('time')
    plt.ylabel('var')
    plt.grid()

# Отображение графиков
plt.tight_layout()  # Автоматически подгоняет подграфики


# dataCol0 = [float(line.strip().split(';')[toRelation[0]]) for line in lines[2:]]
# dataCol1 = [float(line.strip().split(';')[toRelation[1]]) for line in lines[2:]]
#
# plt.figure(figsize=(8, 8))
# plt.plot(dataCol0, dataCol1, marker='o', linestyle='-', color='b')
#
# # Настройка графика
# plt.xlabel(f"{toRelation[0]} {headers[toRelation[0]]}")
# plt.ylabel(f"{toRelation[1]} {headers[toRelation[1]]}")
# plt.grid()
# plt.legend()

# Отображение графика
plt.tight_layout()
plt.show()
