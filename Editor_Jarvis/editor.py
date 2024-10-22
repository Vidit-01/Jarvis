# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.8

from PyQt5 import QtWidgets, QtCore, QtGui
import os

class Editor(QtWidgets.QMainWindow):
    '''Editor'''
    
    def setupUi(self, path):
        self.path = path
        os.chdir(path)
        self.setStyleSheet('background-color:rgb(37,37,38);color:white;')
        MainWindow = QtWidgets.QWidget(self)
        self.main = MainWindow
        self.table = QtWidgets.QTableWidget(MainWindow)
        self.tab = QtWidgets.QTabWidget(MainWindow)
        self.vbox = QtWidgets.QHBoxLayout(MainWindow)
        self.vbox.addWidget(self.table)
        self.vbox.addWidget(self.tab)
        self.tab.addTab(QtWidgets.QWidget(), 'yo')
        self.table.setMinimumWidth(100)
        self.table.setMaximumWidth(200)
        self.setCentralWidget(self.main)
        files = os.listdir(path)
        self.table.setRowCount(len(files))
        self.table.setColumnCount(1)
        x = 0
        for i in files:
            header = QtWidgets.QTableWidgetItem()
            self.table.setVerticalHeaderItem(x, header)
            header.setBackground(QtCore.Qt.transparent)
            yoy = QtWidgets.QTableWidgetItem(i)
            self.table.setItem(x, 0, yoy)
            x = x + 1
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.table.itemDoubleClicked.connect(self.opened)
        self.show()

    
    def opened(self, item):
        file_name = item.text()
        ext = os.path.splitext(file_name)[-1]
        if ext != '':
            self.textedit = QtWidgets.QTextEdit()
            self.tab.addTab(self.textedit, file_name)
            self.textedit.setFontFamily("Consolas, 'Courier New', monospace")
            self.textedit.setFontPointSize(15)
            f = open(os.path.join(self.path, file_name), 'rb')
            html = f.read()
            
            try:
                self.textedit.setPlainText(html.decode())
                self.textedit.textChanged.connect(self.yoyoy)
            
            except Exception:
                if b'.xml' in html:
                    self.textedit.setHtml(str(html))
            finally:
                pass

            f.close()
        else:
            self.open_folder(os.path.join(self.path, file_name))

    
    def open_folder(self, path):
        self.path = path
        file = os.listdir(path)
        self.table.setRowCount(len(file))
        x = 0
        for i in file:
            yoy = QtWidgets.QTableWidgetItem(i)
            self.table.setItem(x, 0, yoy)
            x = x + 1
        self.tab.clear()

    
    def yoyoy(self):
        x = self.tab.tabText(self.tab.currentIndex())
        papath = os.path.join(self.path, x)
        yoy = self.textedit.toPlainText()
    # WARNING: Decompyle incomplete


#Editor = <NODE:27>(Editor, 'Editor', QtWidgets.QMainWindow)
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    edit = Editor()
    edit.setupUi(os.path.join("C:\\Users\\Vidit"))
    app.exec_()
