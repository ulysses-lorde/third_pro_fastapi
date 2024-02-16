from time import sleep

import pyautogui

# pyautogui.press()
# pyautogui.hotkey()

searches = [
    'animes do dia', 'resultado da megasena',
    'citacao do dia', 'cotação do dolar', 'acer nitro 5',
    'dia comemorativo hoje', 'verdade ou desafio',
    'lancamentos do cinema', 'league of legends','pubg'
]


for text in searches:
    sleep(10)
    pyautogui.hotkey('ctrl', 'e')
    pyautogui.write(text, interval=0.20)
    pyautogui.press('enter')
