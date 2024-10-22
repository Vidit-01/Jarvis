# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.8

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QModelIndex, Qt
import os

class FileBrowser(QtWidgets.QTabWidget):
    '''FileBrowser'''
    
    def setupUi(self, MainWindow, foldername):
        MainWindow = self
        self.c.hide()
        self.d.hide()
        self.e.hide()
        self.main = MainWindow
        self.x = 0
        MainWindow.resize(800, 600)
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(3)
        self.list = []
        for i in os.listdir(foldername):
            if i.startswith('$'):
                continue
            self.list.append(i)
        self.table.setRowCount(len(self.list))
        self.x = 0
        for i in self.list:
            self.tableitem = QtWidgets.QTableWidgetItem(i)
            self.tableiiii = QtWidgets.QTableWidgetItem('Delete')
            self.tableiiii.setBackground(Qt.red)
            self.table.setItem(self.x, 2, self.tableiiii)
            self.table.setHorizontalHeaderLabels([
                'Name',
                'Type',
                'Delete'])
            ext = os.path.splitext(i)[-1]
            print(ext)
            if ext != '':
                self.tablefiletype = QtWidgets.QTableWidgetItem(ext)
                self.table.setItem(self.x, 1, self.tablefiletype)
                if ext == '.py' or ext == '.pyw':
                    py = QtGui.QIcon('asset/python.jpg')
                    self.tableitem.setIcon(py)
                    print('#############################################')
            else:
                    self.tablefiletype = QtWidgets.QTableWidgetItem('Folder')
                    self.table.setItem(self.x, 1, self.tablefiletype)
            self.table.setItem(self.x, 0, self.tableitem)
            self.x = self.x + 1
        self.table.itemClicked.connect(self.removeFiles)
        self.table.doubleClicked.connect(self.youknowthid)
        self.table.setEditTriggers(self.table.NoEditTriggers)
        MainWindow.insertTab(0, self.table, foldername)
        self.table.raise_()
        self.table.raise_()
        self.table.raise_()
        self.table.raise_()
        MainWindow.setCurrentIndex(0)

    
    def youknowthid(self, window):
        print(window.row(), window.column())
        filename = self.table.item(window.row(), 0)
        print(filename.text())
        name = self.main.tabText(self.main.currentIndex())
        file = os.path.join(name, filename.text())
        type = os.path.splitext(filename.text())[1]
        if type == '':
            self.main.removeTab(0)
            self.setupUi(self, file)
        else:
            os.startfile(file)
            print(filename)

    
    def removetabs(self, i):
        if self.main.count() == 1:
            app.exit()
        self.main.removeTab(i)

    
    def removeFiles(self, abcd):
        print(abcd.row(), abcd.column())
        if abcd.column() == 2:
            self.abcd = abcd
            x = self.table.item(abcd.row(), 0).text()
            y = self.main.tabText(self.main.currentIndex())
            self.dialog = QtWidgets.QDialog(self.main)
            dialog = self.dialog
            self.full_file = os.path.join(y, x)
            lbal = QtWidgets.QLabel(f'''Are you sure to delete file{self.full_file}''', dialog)
            yes = QtWidgets.QPushButton('Yes', dialog)
            no = QtWidgets.QPushButton('No', dialog)
            yes.clicked.connect(self.removeyes)
            no.clicked.connect(self.removeno)
            yes.setGeometry(0, 50, 50, 20)
            no.setGeometry(50, 50, 50, 20)
            self.dialog.show()

    
    def removeyes(self):
        os.remove(self.full_file)
        self.dialog.close()
        self.table.removeRow(self.abcd.row())

    
    def removeno(self):
        self.dialog.close()

    
    def showDrives(self, MainWindow):
        MainWindow = self
        self.home = QtWidgets.QWidget()
        self.c = QtWidgets.QPushButton('C:/', self.home)
        self.c.setGeometry(100, 100, 100, 100)
        self.c.clicked.connect(self.openC)
        self.d = QtWidgets.QPushButton('D:/', self.home)
        self.d.setGeometry(200, 100, 100, 100)
        self.d.clicked.connect(self.openD)
        self.e = QtWidgets.QPushButton('E:/', self.home)
        self.e.setGeometry(300, 100, 100, 100)
        self.addTab(self.home, 'Home')
        self.e.clicked.connect(self.openE)
        self.c.hide()
        self.d.hide()
        self.e.hide()
        if os.path.exists('C:/'):
            self.c.show()
        if os.path.exists('D:/'):
            self.d.show()
        if os.path.exists('E:/'):
            self.e.show()

    
    def openC(self):
        self.setupUi(self, 'C:/')
        self.removeTab(2)

    
    def openD(self):
        self.setupUi(self, 'D:/')
        self.removeTab(2)

    
    def openE(self):
        self.setupUi(self, 'E:/')
        self.removeTab(2)


#FileBrowser = <NODE:27>(FileBrowser, 'FileBrowser', QtWidgets.QTabWidget)
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    f = FileBrowser()
    lbl = QtWidgets.QTabWidget()
    lbl.setTabsClosable(True)
    f.setTabsClosable(True)
    f.tabCloseRequested.connect(f.removetabs)
    f.showDrives(lbl)
    f.show()
    app.exec_()
