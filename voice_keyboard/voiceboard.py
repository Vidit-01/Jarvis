# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.8

import pyautogui
import pyttsx3

def speak(word):
    x = pyttsx3.init()
    x.say(word)
    x.runAndWait()

print(pyautogui.KEY_NAMES)

def virtualKey(term = None):
    if term.startswith('hold on'):
        key = term.replace('hold on', '')
        pyautogui.keyDown(key)
        speak(f'''holding {key}''')
    if term.startswith('press'):
        key = term.replace('press', '').lower()
        pyautogui.press('enter')
        print(key)
        speak(f'''pressing {key}''')
    if term.startswith('type'):
        sentence = term.replace('term', '')
        keys = list(sentence)
        for i in keys:
            pyautogui.press(i)

if __name__ == '__main__':
    x = input('here:')
    virtualKey(x)
