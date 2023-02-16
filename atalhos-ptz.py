import tkinter
import time
from tkinter import *
from pyautogui import *
import pyautogui
import keyboard


def Leitor():
    pyautogui.hotkey("alt", "1")
    time.sleep(0.2)
    pyautogui.keyDown('num1')
    time.sleep(0.5)
    pyautogui.keyUp('num1')
    time.sleep(1.5)
    pyautogui.hotkey("alt", "2")


def Orador():
    pyautogui.hotkey("alt", "1")
    time.sleep(0.2)
    pyautogui.keyDown('num2')
    time.sleep(0.5)
    pyautogui.keyUp('num2')
    time.sleep(1.5)
    pyautogui.hotkey("alt", "2")    


def OradorBaixo():
    pyautogui.hotkey("alt", "1")
    time.sleep(0.2)
    pyautogui.keyDown('num5')
    time.sleep(0.5)
    pyautogui.keyUp('num5')
    time.sleep(1.5)
    pyautogui.hotkey("alt", "2")    


def Mesa():
    pyautogui.hotkey("alt", "1")
    time.sleep(0.2)
    pyautogui.keyDown('num3')
    time.sleep(0.5)
    pyautogui.keyUp('num3')
    time.sleep(1.5)
    pyautogui.hotkey("alt", "2")        

keyboard.add_hotkey(';', OradorBaixo)

keyboard.add_hotkey("7", Leitor)

keyboard.add_hotkey("8", Orador)

keyboard.add_hotkey("9", Mesa)



root = Tk()
root.title("Atalhos PTZ")
root.geometry("280x120")
# root.bind("<Key>", Leitor)
texto_orientacao = Label(root, text="Atalhos")
texto_orientacao.grid(column=1, row=0)

botaoLeitor = Button(root, text="7 - Leitor", command=Leitor)
botaoLeitor.grid(column=0, row=1, padx=2, pady=5)

botaoOrador = Button(root, text="8 - Orador", command=Orador)
botaoOrador.grid(column=1, row=1, padx=2, pady=5)

botaoMesa = Button(root, text="9 - Mesa", command=Mesa)
botaoMesa.grid(column=2, row=1, padx=2, pady=5)

botaoOradorB = Button(root, text="/ - Orador Baixo", command=OradorBaixo)
botaoOradorB.grid(column=1, row=2, padx=0, pady=5)

root.mainloop()


# keyboard.wait()