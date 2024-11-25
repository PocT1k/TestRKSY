import time
from canvas import metro, tk, fprint
van = metro.van
grk = van.grk
grk.addPos(4)


fps = 30
ts = 1 / fps


print(('ENG!!!' * 30 + '\n') * 3)
with open('logs.txt', 'w') as file: pass
heads = ['tim', 'pos', 'vol', 'res', 'sPs', 'tur', 'rat', 'amp', 'pow', 'eAd', 'eDm', 'eFl', 'sNw', 'sKh']
fprint(f"{' '*5}" + '; '.join(heads) + '; ' + '\n')
fprint(f"{' '*5}" + '; '.join(' ' * (3 - len(str(i))) + str(i) for i in range(len(heads))) + '; ' + '\n')

cTime = 0.0
while True:
    # Счётчик
    fprint(f"{'{:8.2f}'.format(round(cTime, 2))}; ")

    res = metro.proc(ts)
    fprint()

    cTime += ts
    tk.update()
    # time.sleep(ts/2)
    if res >= 20:
        break
