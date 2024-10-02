from AppOpener import open as appopener
from pyautogui import click
from pyautogui import position
from keyboard import press
from keyboard import write
from time import sleep

def Call(name):
    appopener("phone link", match_closest=True)
    sleep(15)

    click(x=282, y=164)
    sleep(10)

    click(x=520, y=79)
    sleep(2)

    click(x=1677, y=193)
    sleep(2)

    write(name)
    sleep(2)

    press('enter')
    sleep(2)
    
    click(x=1677, y=193)

def FindClickPosition():
    sleep(1)
    kkk = position()
    print(kkk)


Call('Mummy')
# FindClickPosition()