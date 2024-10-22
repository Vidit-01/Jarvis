# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.8

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    '''Ui_MainWindow'''
    
    def setupUi(self):
        MainWindow = self
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(800, 538)
        MainWindow.setStyleSheet('')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 40, 581, 141))
        self.widget.setStyleSheet('font: 25 16pt "Segoe UI Light";')
        self.widget.setObjectName('widget')
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setGeometry(QtCore.QRect(180, 70, 171, 41))
        self.radioButton_3.setObjectName('radioButton_3')
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 70, 161, 41))
        self.radioButton_4.setObjectName('radioButton_4')
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 10, 531, 51))
        self.label.setObjectName('label')
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(40, 180, 581, 141))
        self.widget_2.setStyleSheet('font: 25 16pt "Segoe UI Light";')
        self.widget_2.setObjectName('widget_2')
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 531, 51))
        self.label_2.setObjectName('label_2')
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(22, 80, 161, 31))
        self.lineEdit.setObjectName('lineEdit')
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 80, 171, 31))
        self.lineEdit_2.setObjectName('lineEdit_2')
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(40, 320, 581, 141))
        self.widget_3.setStyleSheet('font: 25 16pt "Segoe UI Light";')
        self.widget_3.setObjectName('widget_3')
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 531, 51))
        self.label_3.setObjectName('label_3')
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(22, 80, 161, 31))
        self.lineEdit_3.setObjectName('lineEdit_3')
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 80, 171, 31))
        self.lineEdit_4.setObjectName('lineEdit_4')
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionhell = QtWidgets.QAction(MainWindow)
        self.actionhell.setObjectName('actionhell')
        self.actionyo = QtWidgets.QAction(MainWindow)
        self.actionyo.setObjectName('actionyo')
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', 'MainWindow'))
        self.radioButton_3.clicked.connect(self.built_in)
        self.radioButton_4.clicked.connect(self.default_in)
        self.radioButton_3.setText(_translate('MainWindow', 'Built-in '))
        self.radioButton_4.setText(_translate('MainWindow', 'System Default'))
        self.label.setText(_translate('MainWindow', '1. The webresults must open in :-'))
        self.label_2.setText(_translate('MainWindow', 'Change Password'))
        self.lineEdit.setPlaceholderText(_translate('MainWindow', 'Enter New Password'))
        self.lineEdit_2.setPlaceholderText(_translate('MainWindow', 'repeat new password'))
        self.lineEdit_2.returnPressed.connect(self.password_new)
        self.label_3.setText(_translate('MainWindow', 'Add New function'))
        self.lineEdit_3.setPlaceholderText(_translate('MainWindow', 'Trigger word '))
        self.lineEdit_4.setPlaceholderText(_translate('MainWindow', 'out put'))
        self.lineEdit_4.returnPressed.connect(self.trigger_new)
        self.actionhell.setText(_translate('MainWindow', 'hell'))
        self.actionyo.setText(_translate('MainWindow', 'yo'))

    
    def built_in(self):
        self.browsers = 'built-in'
        self.open_write()

    
    def default_in(self):
        self.browsers = 'default'
        self.open_write()

    
    def open_write(self):
        pass
    # WARNING: Decompyle incomplete

    
    def password_new(self):
        newp = self.lineEdit.text()
        newp1 = self.lineEdit_2.text()
    # WARNING: Decompyle incomplete

    
    def trigger_new(self):
        pass
    # WARNING: Decompyle incomplete


#Ui_MainWindow = <NODE:27>(Ui_MainWindow, 'Ui_MainWindow', QtWidgets.QMainWindow)
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
