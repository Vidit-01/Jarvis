# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.8

from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import datetime
y = sys.argv[0].split('/')
y.pop()
a = '/'.join(y)

class Desktop(QtWidgets.QLabel):
    
    def setupUi(self, MainWindow):
        MainWindow = self
        w = QtWidgets.QDesktopWidget().width()
        h = QtWidgets.QDesktopWidget().height()
        MainWindow.resize(w, h)
        self.label = MainWindow
        self.label.setGeometry(0, 0, w, h)
        self.label.setPixmap(QtGui.QPixmap('asset/im.jpg'))
        self.label.setScaledContents(True)
        self.lockscreen = QtWidgets.QLabel(MainWindow)
        self.lockscreen.resize(w, h)
        self.lockscreen.setPixmap(QtGui.QPixmap('asset/images.jpg'))
        self.lockscreen.setScaledContents(True)
        self.lockscreen.setScaledContents(True)
        self.user = QtWidgets.QLabel(self.lockscreen)
        self.user.setGeometry(300, 200, 500, 100)
        self.login = QtWidgets.QPushButton(self.lockscreen)
        self.login.setStyleSheet('background-color:white;border-radius:20px; border:3px solid black;')
        self.login.setGeometry(600, 510, 150, 70)
        self.login.setText('Login')
        self.password = QtWidgets.QLineEdit(self.lockscreen)
        self.password.setGeometry(450, 450, 300, 50)
        self.password.setStyleSheet('border-radius:20px; border:3px solid black;')
        self.passw1 = open('data/password.txt')
        self.passw = self.passw1.read()
        self.passw1.close()
        self.time = QtWidgets.QLabel(MainWindow)
        self.time.setGeometry(0, 50, 250, 200)
        self.time.setStyleSheet("font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-weight: 100;font-style: italic; color: white;font-size:40px;")
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setText('September')
        d = datetime.date.today().strftime('%d')
        m = datetime.date.today().strftime('%B')
        self.time.setText(f'''{d}\n{m}''')
        self.minutes = QtWidgets.QLabel(MainWindow)
        self.minutes.setGeometry(0, 250, 250, 200)
        self.minutes.setAlignment(QtCore.Qt.AlignCenter)
        t = datetime.datetime.now().strftime('%H:%H:%S')
        self.minutes.setStyleSheet("font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-weight: 100;font-style: italic; color: white;font-size:40px;")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timeismoney)
        self.timer.start(1)
        self.lbl = QtWidgets.QLabel(MainWindow)
        self.lbl.setGeometry(w - 300, 250, 250, 200)
        self.lbl.setStyleSheet("font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-weight: 100;font-style: italic; color: white;font-size:40px;")
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setText('helloo')
        self.lockscreen.raise_()
        self.lockscreen.raise_()
        self.lockscreen.raise_()
        self.lockscreen.raise_()

    
    def create_user(self):
        pass
    # WARNING: Decompyle incomplete

    
    def showall(self):
        self.lockscreen.hide()

    
    def timeismoney(self):
        time = datetime.datetime.now().strftime('%H:%M:%S')
        self.minutes.setText(time)

    
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
        try:
            x = open(f, 'rb')
            y = open('asset/im.jpg', 'wb')
            y.write(x.read())
            self.setPixmap(QtGui.QPixmap('asset/im.jpg'))
            x.close()
            y.close()
        except:
            pass

#Desktop = <NODE:27>(Desktop, 'Desktop', QtWidgets.QLabel)
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = Desktop()
    main.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    main.setupUi(main)
    main.show()
    sys.exit(app.exec_())
