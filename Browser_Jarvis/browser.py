# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.8

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def setupUi(self):
        MainWindow = self
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(800, 600)
        self.window = MainWindow
        self.centralwidget = QtWidgets.QTabWidget()
        self.centralwidget.setObjectName('centralwidget')
        self.centralwidget.setStyleSheet('QTabBar::tab { border-radius:20px;height: 25px; width: 100px; }')
        self.centralwidget.setTabsClosable(True)
        self.centralwidget.tabCloseRequested.connect(self.close_t)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName('menubar')
        self.menuTabs = QtWidgets.QMenu(self.menubar)
        self.menuTabs.setObjectName('menuTabs')
        self.menuTabs_2 = QtWidgets.QMenu(self.menubar)
        self.menuTabs_2.setObjectName('menuTabs_2')
        MainWindow.setMenuBar(self.menubar)
        self.actionAdd_New_Tab = QtWidgets.QAction(MainWindow)
        self.urlbar = QtWidgets.QLineEdit(self.menubar)
        self.urlbar.setGeometry(150, 0, 800, 20)
        self.actionAdd_New_Tab.setObjectName('actionAdd_New_Tab')
        self.actionBack = QtWidgets.QAction(MainWindow)
        self.actionBack.setObjectName('actionBack')
        self.actionForward = QtWidgets.QAction(MainWindow)
        self.actionForward.setObjectName('actionForward')
        self.actionAdd_New_Tab_2 = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Tab_2.setObjectName('actionAdd_New_Tab_2')
        self.actionAdd_New_Tab_2.triggered.connect(self.new)
        self.menuTabs.addAction(self.actionBack)
        self.menuTabs.addSeparator()
        self.menuTabs.addAction(self.actionForward)
        self.menuTabs_2.addAction(self.actionAdd_New_Tab_2)
        self.menubar.addAction(self.menuTabs.menuAction())
        self.menubar.addAction(self.menuTabs_2.menuAction())
        self.urlbar.returnPressed.connect(self.set_url)
        self.add_tab()
        self.centralwidget.currentWidget().page().profile().downloadRequested.connect(self.on_downloadRequested)
        self.centralwidget.currentChanged.connect(self.tab_change)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def set_url(self):
        q = QtCore.QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('https')
        self.centralwidget.currentWidget().setUrl(q)

    
    def add_tab(self, url = ('https://google.com')):
        page = QtWebEngineWidgets.QWebEngineView()
        page.setUrl(QtCore.QUrl(url))
        self.centralwidget.insertTab(0, page, page.title())
        self.centralwidget.setCurrentIndex(0)

    
    def tab_change(self):
        ur = self.centralwidget.currentWidget().url().toString()
        self.urlbar.setText(ur)

    
    def close_t(self, i):
        self.centralwidget.removeTab(i)

    
    def new(self):
        pg = QtWebEngineWidgets.QWebEngineView()
        pg.setUrl(QtCore.QUrl('http://google.com'))
        self.centralwidget.insertTab(0, pg, 'Google')

    
    def on_downloadRequested(self, download):
        old_path = download.url().path()
        suffix = QtCore.QFileInfo(old_path).suffix()
        (path, _) = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', old_path, '*.' + suffix)
        if path:
            download.setPath(path)
            download.accept()

    on_downloadRequested = QtCore.pyqtSlot('QWebEngineDownloadItem*')(on_downloadRequested)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', 'MainWindow'))
        self.menuTabs.setTitle(_translate('MainWindow', 'Back/Forward'))
        self.menuTabs_2.setTitle(_translate('MainWindow', 'Tabs'))
        self.actionAdd_New_Tab.setText(_translate('MainWindow', 'Add New Tab'))
        self.actionAdd_New_Tab.triggered.connect(self.new)
        self.actionBack.setText(_translate('MainWindow', 'Back'))
        self.actionBack.triggered.connect(self.centralwidget.currentWidget().back)
        self.actionForward.setText(_translate('MainWindow', 'Forward'))
        self.actionAdd_New_Tab_2.setText(_translate('MainWindow', 'Add New Tab'))


#Ui_MainWindow = <NODE:27>(Ui_MainWindow, 'Ui_MainWindow', QtWidgets.QMainWindow)
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
