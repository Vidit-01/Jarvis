# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.8

import os
import sys
zz = os.path.dirname(os.path.abspath(__file__))
os.chdir(zz)
import time
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon
start = time.time()
from PyQt5.QtCore import QAbstractAnimation, Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QGraphicsColorizeEffect, QLabel, QMainWindow, QWidget
from Word_Jarvis import word
from FileBrowser_Jarvis import filebrowser
from Calculator_Jarvis import calculate
from Browser_Jarvis import browser
from Editor_Jarvis import editor
from Settings_Jarvis import settings
import pyttsx3
import speech_recognition as sr
import desktop
import chatapp
import taskbar
import googlesearch
import multiprocessing
import webbrowser
import pyautogui
import math
import os
name1 = open('data/username.txt')
name = name1.read()
name1.close()

class User:
    
    def setup(self):
        name1 = open('data/username.txt')
        name = name1.read()
        name1.close()
        if name == '':
            self.dialog = QtWidgets.QDialog()
            self.dialog.resize(200, 100)
            self.menu = QtWidgets.QLineEdit(self.dialog)
            self.menu.setPlaceholderText('Enter Username')
            self.menu.setWindowTitle('Enter Username')
            self.menu.setGeometry(0, 0, 100, 30)
            self.ok = QtWidgets.QPushButton('Ok', self.dialog)
            self.ok.clicked.connect(self.create_user)
            self.ok.setGeometry(0, 40, 100, 30)
            self.menu.returnPressed.connect(self.create_user)
            self.dialog.show()
            app.exec_()
        if name != '':
            p1.start()

    
    def create_user(self):
        pass
    # WARNING: Decompyle incomplete


engine = pyttsx3.init()
app = QApplication([])
DESKTOP = desktop.Desktop()
TASKBAR = taskbar.TaskBar()
deskt = DESKTOP
task = QWidget()
color = QGraphicsColorizeEffect()
color.setColor(Qt.green)
task.setWindowFlag(Qt.WindowStaysOnTopHint)
task.setWindowTitle('TaskBar')
bro = QMainWindow(deskt)
calen = QMainWindow(deskt)
BROWSER = browser.Ui_MainWindow(bro)
bro.setCentralWidget(BROWSER)
BROWSER.setupUi()
CHATAPP = chatapp.Ui_MainWindow(deskt)
CHATAPP.setupUi()
DESKTOP.setupUi(deskt)
TASKBAR.setupUi(task)
TASKBAR.setup_start(TASKBAR.menu)
desk = deskt

def open_word():
    word_label = QMainWindow(desk)
    WORD = word.Ui_MainWindow(word_label)
    WORD.setWindowFlag(Qt.FramelessWindowHint)
    word_label.setWindowTitle('Jarvis Word')
    WORD.setupUi()
    word_label.showMaximized()


def open_calculator(eq):
    CALCI = calculate.Window(desk)
    CALCI.ini1t()
    CALCI.label.setText(eq)
    ans = CALCI.action_equal()
    CALCI.show()
    return ans


def open_calendar():
    calen.show()


def open_files():
    exp_label = QMainWindow(desk)
    EXPLORER = filebrowser.FileBrowser(exp_label)
    EXPLORER.setTabsClosable(True)
    EXPLORER.tabCloseRequested.connect(EXPLORER.removetabs)
    exp_label.setCentralWidget(EXPLORER)
    exp_label.setWindowTitle('Jarvis Explorer')
    EXPLORER.showDrives('')
    EXPLORER.showDrives('')
    exp_label.showMaximized()


def open_settings():
    SETTINGS = settings.Ui_MainWindow(desk)
    SETTINGS.setupUi()
    SETTINGS.show()


def open_web(term):
    pass
# WARNING: Decompyle incomplete


def open_b():
    open_web('https://google.com')


def open_editor():
    EDITOR = editor.Editor(desk)
    EDITOR.setupUi('C:\\Users\\Vidit')


def open_chat():
    CHATAPP.show()


def open_apps():
    self = TASKBAR
    self.menu.setStyleSheet('border:1px solid white;background-color:black')
    self.menu.setGeometry(0, self.h - 440, 400, 400)
    TASKBAR.setup_start(TASKBAR.menu)
    TASKBAR.chrome.clicked.connect(open_b)
    TASKBAR.pushButton_2.clicked.connect(open_word)
    TASKBAR.pushButton_3.clicked.connect(open_files)
    TASKBAR.pushButton_4.clicked.connect(open_editor)
    TASKBAR.pushButton_5.clicked.connect(open_settings)
    TASKBAR.pushButton_10.clicked.connect(sys.exit)
    TASKBAR.menu.show()


class Jarvis(object):
    
    def speak(self, audio):
        engine.say(audio)
        engine.runAndWait()

    
    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            self.Jarvis(query)
        except:
            pass

    
    def Jarvis(self, word):
        DESKTOP.lbl.setText(str(word))
        query = str(word).lower()
        if 'open' in query:
            x = query.replace('open', '')
            if 'word' in x:
                TASKBAR.word.click()
            if 'app' in query:
                TASKBAR.apps.click()
            if 'editor' in query:
                TASKBAR.editor.click()
            if 'files' in query:
                TASKBAR.files.click()
            elif 'word' not in query:
                self.speak(f'''opening {x}''')
                url = googlesearch.search(x)[0]
                open_web(url)
        if 'say' in query:
            x = query.replace('say', '')
            self.speak(x)
        if 'yourself' in query:
            self.speak('I am Jarvis a Personal Assistant made by Vidit')
        if 'search google for' in query:
            quer1 = query.replace('search google for', '')
            link = f'''https://www.google.com/search?q={quer1}&rlz=1C1CHWL_enIN961IN961&sxsrf=ALeKk02Sg6LnJq0Tb5SGHtzPr0uFAJmSRQ%3A1628571206013&ei=RgYSYbMcz9jPuw-B0Zr4Dw&oq=quer1&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEA0yBAgAEA0yBAgAEA0yBAguEA0yBAgAEA0yCAgAEA0QBRAeOgkIABCwAxANEB46CwgAELADEA0QChAeSgQIQRgBUM4uWKQ_YJ1CaAFwAHgAgAHWAYgB0gOSAQUwLjIuMZgBAKABAcgBAsABAQ&sclient=gws-wiz&ved=0ahUKEwiz1-bB1KXyAhVP7HMBHYGoBv8Q4dUDCA4&uact=5'''
            open_web(link)
        if '+' in query and '-' in query and '*' in query or '/' in query:
            ans = open_calculator(query)
            self.speak(f'''{query} = {ans}''')
        if 'play' in query:
            playonyt = playonyt
            import pywhatkit
            r = query.replace('play', '')
            x = playonyt(r, False, **('open_video',))
            open_web(x)
        if 'fullscreen' in query or 'full screen' in query:
            pyautogui.press('f11')
        if 'change window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
        if 'close window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')
        if 'sin' in query:
            q1 = query.replace('sin', '')
            self.speak(math.sin(eval(q1)))
        if 'cos' in query:
            q1 = query.replace('cos', '')
            self.speak(math.cos(eval(q1)))
        if 'type' in query and 'press' in query or 'hold on' in query:
            voiceBoard = voiceBoard
            import voice_keyboard
            voiceBoard.virtualKey(query)
        if 'maps' in query or 'map' in query:
            place = query.replace('maps', '')
            lnk = f'''https://www.google.com/maps/place/{place}'''
            open_web(lnk)
        f = open('data/trigger.txt')
        if f.read() != '':
            lis = eval(f.read())
            if lis[0] in query:
                self.speak(lis[1])
        f.close()

    
    def main(self):
        query = self.takeCommand()
        self.Jarvis(query)

    
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.right_create(event)

    
    def right_create(self, event):
        self.menu = QtWidgets.QMenu(self)
        self.act1 = QtWidgets.QAction('Change BackGround')
        self.act1.triggered.connect(self.set_bg)
        self.menu.addAction(self.act1)
        self.menu.exec_(event.globalPos())

    
    def set_bg(self):
        f = QtWidgets.QFileDialog.getOpenFileName()[0]
        x = open(f, 'rb')
        y = open('asset/im.jpg', 'wb')
        y.write(x.read())
        self.setPixmap(QtGui.QPixmap('asset/im.jpg'))
        x.close()
        y.close()



def command_box():
    x = TASKBAR.command.text()
    Jarvis().Jarvis(x)
    TASKBAR.command.clear()

TASKBAR.word.clicked.connect(open_word)
TASKBAR.files.clicked.connect(open_files)
TASKBAR.command.returnPressed.connect(command_box)
TASKBAR.browser.clicked.connect(open_b)
TASKBAR.editor.clicked.connect(open_editor)
TASKBAR.setting.clicked.connect(open_settings)
TASKBAR.apps.clicked.connect(open_apps)
TASKBAR.chat.clicked.connect(open_chat)

def Show():
    import sys
    deskt.showFullScreen()
    passowrd_clicked()
    sys.exit(app.exec_())

p1 = multiprocessing.Process(target=Show)
p2 = multiprocessing.Process(target=Jarvis().main)

def passowrd_clicked():
    self = DESKTOP
    x = self.password.text()
    if self.passw == x or self.passw == '':
        DESKTOP.showall()
        import pyttsx3
        engine = pyttsx3.init()
        engine.say('Welcome Back Sir')
        engine.runAndWait()
        p2.start()
        task.show()
    else:
        self.password.clear()
        self.password.setPlaceholderText('You Entered wrong password')
        import pyttsx3
        engine = pyttsx3.init()
        engine.say('Sir please enter the right password')
        engine.runAndWait()


def end_all():
    p1.close()
    p2.close()

DESKTOP.login.clicked.connect(passowrd_clicked)
DESKTOP.password.returnPressed.connect(passowrd_clicked)
TASKBAR.pushButton_10.clicked.connect(end_all)
if __name__ == '__main__':
    multiprocessing.freeze_support()
    user = User()
    user.setup()
