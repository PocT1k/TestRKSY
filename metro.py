import math


def fprint(str = '\n'):
    print(str, end='')
    with open('logs.txt', 'a') as f:
        f.write(str)


class AutomaticSwitch:
    condition = True
    def __init__(self, maxCurrent, normalCondition = True):
        self.maxCurrent = maxCurrent
        self.normalCondition = normalCondition
pass # class AutomaticSwitch:

class GRK:
    __position = 0
    runRes = [4.176, 1.818, 0.451, 0]
    breakRes = [2.083, 1.37, 0.478, 0.273]
    quanRunPos = len(runRes)
    quanBreakPos = -len(breakRes)
    quanPos = quanRunPos - quanBreakPos + 1
    namePos = ['Х4', 'Х3', 'Х2', 'Х1', 'Н', 'Т1', 'Т2', 'Т3', 'Т4']

    def addPos(self, disPos = 1):
        self.__position += disPos
        if self.__position > self.quanRunPos:
            self.__position = self.quanRunPos
    def dimPos(self, disPos = 1):
        self.__position -= disPos
        if self.__position < self.quanBreakPos:
            self.__position = self.quanBreakPos
    def setPos(self, newPos = 0):
        self.__position = newPos
        if self.__position > self.quanRunPos:
            self.__position = self.quanRunPos
        if self.__position < self.quanBreakPos:
            self.__position = self.quanBreakPos
    def getPos(self):
        return self.__position
    def getRes(self):
        if self.__position == 0:
            return 0
        if self.__position > 0:
            return self.runRes[self.__position - 1]
        else:
            return self.breakRes[-self.__position - 1]
pass # class GRK

class Van:
    statParallConnectEngine = 0
    energy = 0.0 # Джоули
    mass = int(33.5 * 1000)  # Килограммы
    gearRatio = 5.33
    quanEngine = 4
    resRotEng = 0.0285
    resStatEng = 0.0312 + 0.0103
    resFullEng = round((resRotEng + resStatEng) * quanEngine, 3) # Омы 0.28
    engineKPD = 0.89

    # switch_BV = AutomaticSwitch(1500)
    # RP = [switch_BV]
    grk = GRK()

    def getRes(self):
        if self.grk.getPos() == 0:
            return 'inf'
        else:
            return round(self.resFullEng + self.grk.getRes(), 3)

    def proc(self, ts, voltage):
        # pos Позиция
        fprint(f"{self.grk.getPos()}; ")

        # vol Вольтаж, на вагон
        voltage = voltage * (self.statParallConnectEngine + 1)
        fprint(f"{voltage}; ")

        # res Сопротивление, общее
        fulRes = self.getRes()
        fprint(f"{fulRes}; ")

        # sPs Скорость прошлая(м/с)
        speedPastMs = math.sqrt(2 * self.energy / self.mass)
        speedPastMs = round(speedPastMs, 3)
        fprint(f"{speedPastMs}; ")

        # tur Обороты двигателя(об/с)
        turnovers = speedPastMs / (0.78 * math.pi) * self.gearRatio
        turnovers = round(turnovers, 3)
        fprint(f"{turnovers}; ")

        # rat Коэфф мощности [0, 1]
        # ratio = 0.9 / (turnovers / 10 + 0.9) # 1 случайная
        # След 2: ошибка, не то вообще делаю с графиком, не те коэффециэнты
        # ratio = (1280 / (turnovers + 5) - 5) / 251 # Что-то похожее на значения, полученные с РК2
        # ratio = (4000 / (turnovers + 20) - 50) / 150 # Что-то похожее на значения, полученные с РК2, попытка
        # ratio = 0.2 / (turnovers / 10 + 0.2)  # 2 случайная, улучшенная
        # ratio = 10 / (turnovers + 10)  # 3 типо подобрано
        # ratio = 0.1 / (turnovers/15 + 0.1)  # 4
        # ratio = 1 / (turnovers + 1)  # 5 От графика ампеража
        ratio = 20 / (turnovers ** 2 + 20)  # 6 ...
        if ratio < 0:
            ratio = 0.0
        else:
            ratio = round(ratio, 3)
        fprint(f"{ratio}; ")

        # amp Ток
        if fulRes == 'inf':
            amperage = 0.0
        else:
            amperage = voltage / fulRes * ratio
            if self.grk.getPos() < 0:
                amperage = -amperage
            amperage = round(amperage, 3)
        fprint(f"{round(amperage, 2)}; ")

        # pow Мощность
        power = voltage * amperage
        power = round(power, 3)
        fprint(f"{power}; ")

        # eAd Энергия прибавление
        energyAdd = power * self.engineKPD
        energyAdd = round(energyAdd, 3)
        fprint(f"{energyAdd}; ")

        # eDm Энергия потери
        energyDim = (0.5 * (speedPastMs ** 2) + 3) * 1000 * 0
        energyDim = round(energyDim, 3)
        fprint(f"{energyDim}; ")

        # eFl Прибавление
        self.energy += (energyAdd - energyDim) * ts
        if self.energy < 0:
            self.energy = 0.0
        else:
            self.energy = round(self.energy, 3)
        fprint(f"{self.energy}; ")

        # sNw Скорость(м/с)
        speedNowMs = math.sqrt(2 * self.energy / self.mass)
        speedNowMs = round(speedNowMs, 3)
        fprint(f"{speedNowMs}; ")

        # sKh Скорость(км/ч)
        speedKh = round(speedNowMs * 3.6, 3)
        fprint(f"{speedKh}; ")

        return speedKh
    pass # def proc()
pass  # class Van

class Metro:
    voltage = 740 # Вольты, 740 - метрострой, 825 - номинал
    amperage = 3000 # Амперы
    van = Van()

    def proc(self, ts):
        res = self.van.proc(ts, self.voltage)
        return res
pass # class Metro
