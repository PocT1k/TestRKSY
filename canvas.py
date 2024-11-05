from tkinter import *
from metro import Metro, fprint


shiftY = 25
shiftX = 50

metro = Metro()
grk = metro.van.grk

tk = Tk()
canvas = Canvas(tk, width = 500, height = 300)
canvas.pack()

def updateButtomsGRK(event):
    if event.keysym == 'w':
        grk.addPos()
    elif event.keysym == 's':
        grk.dimPos()
    else:
        nPos = int(event.keysym)
        if nPos > grk.quanRunPos:
            nPos = -nPos + (grk.quanRunPos + 1)
        grk.setPos(nPos)

    canvas.coords(idControllerImg, shiftX, (grk.quanPos - grk.getPos() + grk.quanBreakPos - 1) * shiftY)
    # canvas.move(idControllerImg, 0, -shiftY * rk.add())
    # tk.update()

canvas.bind_all('w', updateButtomsGRK)
canvas.bind_all('s', updateButtomsGRK)

canvas.bind_all('1', updateButtomsGRK)
canvas.bind_all('2', updateButtomsGRK)
canvas.bind_all('3', updateButtomsGRK)
canvas.bind_all('4', updateButtomsGRK)

canvas.bind_all('5', updateButtomsGRK)

canvas.bind_all('6', updateButtomsGRK)
canvas.bind_all('7', updateButtomsGRK)
canvas.bind_all('8', updateButtomsGRK)
canvas.bind_all('9', updateButtomsGRK)


controllerObj = PhotoImage(file = 'controller.png')
idControllerImg = canvas.create_image(shiftX, grk.quanRunPos * shiftY, anchor = NW, image = controllerObj)

for i in range(grk.quanPos):
    canvas.create_text(shiftX * 0.5, (i + 0.5) * shiftY, text = grk.namePos[i], font = ('Calibri', 20))
tk.update()
