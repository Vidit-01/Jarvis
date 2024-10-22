# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Python 3.8.0 (3413)

import requests
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
f = open("data/username.txt")
name = f.read()
f.close()

class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self):
        MainWindow = self
        self.setStyleSheet("border-radius:20px;")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 600)
        MainWindow.setMinimumSize(QtCore.QSize(450, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget.setUrl(QtCore.QUrl("http://jarvischat.pythonanywhere.com/chat"))
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEdit.setStyleSheet("border-radius:20px;\nborder: 1px solid black;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(81, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(81, 50))
        self.pushButton.setStyleSheet("border-radius:20px;\nborder: 1px solid black;\n\nbackground-color: rgb(85, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.sendMessage)
        self.lineEdit.returnPressed.connect(self.sendMessage)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Something .. . . ."))
        self.pushButton.setText(_translate("MainWindow", "Post"))

    def sendMessage(self):
        text = self.lineEdit.text()
        time = datetime.now().strftime("%H:%M:%S") + "\n"
        post = name + ":" + text + time
        requests.post("http://jarvischat.pythonanywhere.com/chat", post)
        self.lineEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
