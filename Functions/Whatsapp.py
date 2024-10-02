from AppOpener import open as appopener
from pyautogui import click
from pyautogui import position
from keyboard import press
from keyboard import write
from time import sleep

def WhatsappMsg(name, message):
    appopener("whatsapp", match_closest=True)
    sleep(10)

    click(x=277, y=144)
    sleep(1)
    
    write(name)
    sleep(3)

    click(x=379, y=279)
    sleep(1)

    click(x=930, y=1045)
    sleep(1)

    write(message)
    sleep(0.5)

    click(x=1886, y=1043)
    press('enter')

def FindClickPosition():
    sleep(1)
    kkk = position()
    print(kkk)

# FindClickPosition()
# WhatsappMsg('you', 'hello')