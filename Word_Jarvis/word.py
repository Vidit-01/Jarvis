# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Python 3.8.0 (3413)

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
import base64

class Ui_MainWindow(QtWidgets.QLabel):

    def setupUi(self):
        MainWindow = self
        self.file_name = " "
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1384, 768)
        self.setPixmap(QtGui.QPixmap("asset/im.jpg"))
        self.centralwidget = self
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Home_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.Home_tab.setMinimumSize(QtCore.QSize(1366, 100))
        self.Home_tab.setMaximumSize(QtCore.QSize(1366, 100))
        self.Home_tab.setObjectName("Home_tab")
        self.Home_tab.setStyleSheet("background-color:rgba(240,240,240,180)")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black")
        self.tab.setObjectName("tab")
        self.save = QtWidgets.QPushButton(self.tab)
        self.save.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.save.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black")
        self.save.setObjectName("save")
        self.saveap = QtWidgets.QPushButton(self.tab)
        self.saveap.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.saveap.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black")
        self.saveap.setObjectName("saveap")
        self.open = QtWidgets.QPushButton(self.tab)
        self.open.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.open.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black")
        self.open.setObjectName("open")
        self.saveah = QtWidgets.QPushButton(self.tab)
        self.saveah.setGeometry(QtCore.QRect(100, 40, 75, 23))
        self.saveah.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black")
        self.saveah.setObjectName("saveah")
        self.Home_tab.addTab(self.tab, "Home")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Paste = QtWidgets.QPushButton(self.tab_2)
        self.Paste.setGeometry(QtCore.QRect(10, 10, 50, 50))
        self.Paste.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/OIP.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Paste.setIcon(icon)
        self.Paste.setIconSize(QtCore.QSize(10, 10))
        self.Paste.setObjectName("Paste")
        self.Copy = QtWidgets.QPushButton(self.tab_2)
        self.Copy.setGeometry(QtCore.QRect(60, 10, 75, 25))
        self.Copy.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/OIP (1).jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Copy.setIcon(icon1)
        self.Copy.setObjectName("Copy")
        self.Cut = QtWidgets.QPushButton(self.tab_2)
        self.Cut.setGeometry(QtCore.QRect(60, 35, 75, 25))
        self.Cut.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/OIP (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Cut.setIcon(icon2)
        self.Cut.setObjectName("Cut")
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(140, 0, 16, 71))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.fontComboBox = QtWidgets.QFontComboBox(self.tab_2)
        self.fontComboBox.setGeometry(QtCore.QRect(170, 10, 151, 22))
        self.fontComboBox.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black")
        self.fontComboBox.setObjectName("fontComboBox")
        self.fontComboBox.currentFontChanged.connect(self.font_change)
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox.setGeometry(QtCore.QRect(320, 10, 42, 22))
        self.spinBox.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black")
        self.spinBox.setObjectName("spinBox")
        self.spinBox.valueChanged.connect(self.change_size)
        self.Bold = QtWidgets.QPushButton(self.tab_2)
        self.Bold.setGeometry(QtCore.QRect(170, 35, 25, 25))
        self.Bold.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        self.Bold.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/BS_Word-main/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Bold.setIcon(icon3)
        self.Bold.setObjectName("Bold")
        self.Italic = QtWidgets.QPushButton(self.tab_2)
        self.Italic.setGeometry(QtCore.QRect(195, 35, 25, 25))
        self.Italic.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        self.Italic.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/BS_Word-main/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Italic.setIcon(icon4)
        self.Italic.setObjectName("Italic")
        self.Underl = QtWidgets.QPushButton(self.tab_2)
        self.Underl.setGeometry(QtCore.QRect(220, 35, 25, 25))
        self.Underl.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        self.Underl.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/BS_Word-main/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Underl.setIcon(icon5)
        self.Underl.setObjectName("Underl")
        self.Superscript = QtWidgets.QPushButton(self.tab_2)
        self.Superscript.setGeometry(QtCore.QRect(270, 35, 25, 25))
        self.Superscript.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        self.Superscript.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/OIP (3).jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Superscript.setIcon(icon6)
        self.Superscript.setObjectName("Superscript")
        self.Subscript = QtWidgets.QPushButton(self.tab_2)
        self.Subscript.setGeometry(QtCore.QRect(245, 35, 25, 25))
        self.Subscript.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        self.Subscript.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/OIP (2).jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Subscript.setIcon(icon7)
        self.Subscript.setIconSize(QtCore.QSize(30, 30))
        self.Subscript.setObjectName("Subscript")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(380, 0, 20, 81))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Left = QtWidgets.QPushButton(self.tab_2)
        self.Left.setGeometry(QtCore.QRect(410, 10, 80, 25))
        self.Left.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/BS_Word-main/left-align.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Left.setIcon(icon8)
        self.Left.setObjectName("Left")
        self.Center = QtWidgets.QPushButton(self.tab_2)
        self.Center.setGeometry(QtCore.QRect(410, 35, 80, 25))
        self.Center.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/BS_Word-main/center-align.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Center.setIcon(icon9)
        self.Center.setObjectName("Center")
        self.Right = QtWidgets.QPushButton(self.tab_2)
        self.Right.setGeometry(QtCore.QRect(490, 10, 80, 25))
        self.Right.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/BS_Word-main/right-align.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Right.setIcon(icon10)
        self.Right.setObjectName("Right")
        self.Justi = QtWidgets.QPushButton(self.tab_2)
        self.Justi.setGeometry(QtCore.QRect(490, 35, 80, 25))
        self.Justi.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/BS_Word-main/justification.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Justi.setIcon(icon11)
        self.Justi.setIconSize(QtCore.QSize(10, 10))
        self.Justi.setObjectName("Justi")
        self.Textcolor = QtWidgets.QPushButton(self.tab_2)
        self.Textcolor.setGeometry(QtCore.QRect(615, 15, 75, 23))
        self.Textcolor.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black")
        self.Textcolor.setObjectName("Textcolor")
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        self.line_3.setGeometry(QtCore.QRect(580, 0, 20, 71))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Home_tab.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.Table = QtWidgets.QPushButton(self.tab_3)
        self.Table.setGeometry(QtCore.QRect(20, 10, 50, 50))
        self.Table.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        self.Table.setIcon(icon)
        self.Table.setIconSize(QtCore.QSize(10, 10))
        self.Table.setObjectName("Table")
        self.Picture = QtWidgets.QPushButton(self.tab_3)
        self.Picture.setGeometry(QtCore.QRect(70, 10, 50, 50))
        self.Picture.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        self.Picture.setIcon(icon)
        self.Picture.setIconSize(QtCore.QSize(10, 10))
        self.Picture.setObjectName("Picture")
        self.HTML = QtWidgets.QPushButton(self.tab_3)
        self.HTML.setGeometry(QtCore.QRect(120, 10, 50, 50))
        self.HTML.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        self.HTML.setIcon(icon)
        self.HTML.setIconSize(QtCore.QSize(10, 10))
        self.HTML.setObjectName("HTML")
        self.Link = QtWidgets.QPushButton(self.tab_3)
        self.Link.setGeometry(QtCore.QRect(170, 10, 50, 50))
        self.Link.setStyleSheet("background-color:rgba(255,255,255,180);border:2px solid black;")
        self.Link.setIcon(icon)
        self.Link.setIconSize(QtCore.QSize(10, 10))
        self.Link.setObjectName("Link")
        self.Home_tab.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.Home_tab)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setMaximumSize(QtCore.QSize(1000, 600))
        self.textEdit.setMinimumSize(500, 500)
        self.textEdit.setStyleSheet("background-color:rgba(255,255,255,240);")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addWidget(self.widget)
        self.spinBox.setValue(16)
        self.retranslateUi(MainWindow)
        self.Home_tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.show()

    def font_change(self):
        font = self.fontComboBox.currentFont()
        self.textEdit.setCurrentFont(font)

    def retranslateUi(self, MainWindow):
        self.Italic.clicked.connect(self.set_italic)
        self.Underl.clicked.connect(self.set_underline)
        self.Underl.setText("U")
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.save.clicked.connect(self.save_file)
        self.saveap.setText(_translate("MainWindow", "Save as PDF"))
        self.saveap.clicked.connect(self.save_pdf)
        self.open.setText(_translate("MainWindow", "Open"))
        self.open.clicked.connect(self.open_file)
        self.saveah.setText(_translate("MainWindow", "Save as HTML"))
        self.saveah.clicked.connect(self.save_as_html)
        self.Home_tab.setTabText(self.Home_tab.indexOf(self.tab), _translate("MainWindow", "File"))
        self.Paste.setText(_translate("MainWindow", "Paste"))
        self.Paste.clicked.connect(self.textEdit.paste)
        self.Copy.setText(_translate("MainWindow", "Copy"))
        self.Copy.clicked.connect(self.textEdit.copy)
        self.Cut.setText(_translate("MainWindow", "Cut"))
        self.Cut.clicked.connect(self.textEdit.cut)
        self.Left.setText(_translate("MainWindow", "Left"))
        self.Left.clicked.connect(self.align_left)
        self.Center.setText(_translate("MainWindow", "Center"))
        self.Center.clicked.connect(self.align_center)
        self.Right.setText(_translate("MainWindow", "Right"))
        self.Right.clicked.connect(self.align_left)
        self.Justi.setText(_translate("MainWindow", "Justification"))
        self.Justi.clicked.connect(self.align_center)
        self.Textcolor.setText(_translate("MainWindow", "Text Color"))
        self.Home_tab.setTabText(self.Home_tab.indexOf(self.tab_2), _translate("MainWindow", "Home"))
        self.Table.setText(_translate("MainWindow", "Table"))
        self.Table.clicked.connect(self.table_insert)
        self.Picture.setText(_translate("MainWindow", "Picture"))
        self.Picture.clicked.connect(self.insert_video)
        self.HTML.setText(_translate("MainWindow", "HTML"))
        self.HTML.clicked.connect(self.insert_html)
        self.Link.setText(_translate("MainWindow", "Link"))
        self.Link.clicked.connect(self.insert_link)
        self.Home_tab.setTabText(self.Home_tab.indexOf(self.tab_3), _translate("MainWindow", "Insert"))
        self.Bold.setText("B")
        self.Italic.setText("I")
        self.textEdit.insertHtml("\n        <style>\n            td{\n            padding: 10px;\n            border: 1px solid black;\n            border-collapse: collapse;}\n        </style>\n        ")

    def close_when(self):
        if self.file_name == " ":
            self.save_file()
        self.close

    def change_size(self):
        v = self.spinBox.value()
        self.textEdit.setFontPointSize(v)

    def set_italic(self):
        state = self.textEdit.fontItalic()
        self.textEdit.setFontItalic(not state)

    def set_underline(self):
        state = self.textEdit.fontUnderline()
        self.textEdit.setFontUnderline(not state)

    def save_file(self):
        htm = self.textEdit.toHtml()
        if self.file_name == " ":
            self.save_as_file()

    def save_as_file(self):
        self.file_name = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "C:\\", "Dxox files(*.dxox)")[0]
        htm = self.textEdit.toHtml()
        with open(self.file_name, "w+") as f:
            f.write(f"<!-- Copy right: Vidit Gupta this file is created by use of Vidit's program -->{htm}")
            f.close()

    def save_as_html(self):
        self.file_name = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "C:\\", "html files(*.html)")[0]
        htm = self.textEdit.toHtml()
        with open(self.file_name, "w+") as f:
            f.write(f"<!-- Copy right: Vidit Gupta this file is created by use of Vidit program -->{htm}")
            f.close()

    def open_file(self):
        self.file_name = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "C:\\", "Dxox files(*.dxox) \n html files (*.html)")[0]
        file_o = open(self.file_name)
        htmli = file_o.read()
        self.textEdit.setHtml(htmli)
        file_o.close()

    def insert_image(self):
        img_path = QtWidgets.QFileDialog.getOpenFileName(self, "open image", "C:\\", "image files (*.jpg *.png)\n All Files(*.*)")[0]
        try:
            img_d = open(img_path, "rb")
            data_ = base64.b64encode(img_d.read()).decode("utf-8")
            self.textEdit.insertHtml(f"<img src = data:image/png;base64,{data_}>")
        except Exception as e:
            try:
                pass
            finally:
                e = None
                del e

    def insert_video(self):
        img_path = QtWidgets.QFileDialog.getOpenFileName(self, "open image", "C:\\", "image files (*.mp4 *.png)\n All Files(*.*)")[0]
        try:
            img_d = open(img_path, "rb")
            data_ = base64.b64encode(img_d.read()).decode("utf-8")
            self.textEdit.insertHtml(f'<video width="320" height="240" controls>\n    <source src="data:video/mp4;base64,{data_}" >\n    </video>')
        except Exception as e:
            try:
                pass
            finally:
                e = None
                del e

    def save_pdf(self):
        f_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf);;All files()")
        print(f_name)
        if f_name != "":
            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setOutputFileName(f_name)
            self.textEdit.document().print_(printer)

    def insert_html(self):
        self.dialog = QtWidgets.QWidget()
        self.dialog.resize(QtCore.QSize(200, 50))
        self.plaint = QtWidgets.QPlainTextEdit(self.dialog)
        self.plaint.setPlaceholderText("Insert Html here")
        self.plaint.setGeometry(0, 0, 150, 50)
        self.button = QtWidgets.QPushButton(self.dialog)
        self.button.setGeometry(150, 0, 50, 50)
        self.button.setText("Submit")
        self.button.clicked.connect(self.button_clicked)
        self.dialog.show()

    def button_clicked(self):
        self.html = self.plaint.toPlainText()
        self.textEdit.insertHtml(self.html)
        self.dialog.close()

    def insert_link(self):
        self.dialog = QtWidgets.QWidget()
        self.dialog.resize(QtCore.QSize(200, 50))
        self.plaint1 = QtWidgets.QPlainTextEdit(self.dialog)
        self.plaint1.setPlaceholderText("Insert Text here")
        self.plaint1.setGeometry(0, 0, 150, 25)
        self.plaint2 = QtWidgets.QPlainTextEdit(self.dialog)
        self.plaint2.setPlaceholderText("Insert Link here")
        self.plaint2.setGeometry(0, 25, 150, 25)
        self.button = QtWidgets.QPushButton(self.dialog)
        self.button.setGeometry(150, 0, 50, 50)
        self.button.setText("Submit")
        self.button.clicked.connect(self.for_button)
        self.dialog.show()

    def for_button(self):
        txt = self.plaint1.toPlainText()
        link = self.plaint2.toPlainText()
        self.textEdit.insertHtml(f"<a href= https://{link}>{txt}</a>")

    def align_left(self):
        self.textEdit.setAlignment(QtCore.Qt.AlignLeft)

    def align_right(self):
        self.textEdit.setAlignment(QtCore.Qt.AlignRight)

    def align_center(self):
        f = self.textEdit.fontPointSize()
        print(f)
        self.textEdit.setAlignment(QtCore.Qt.AlignCenter)

    def table_insert(self):
        fs = self.textEdit.fontPointSize()
        x = int(input("here"))
        y = int(input("here"))
        lis = [""]
        lis.append('<table border="0" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" cellspacing="0" cellpadding="0">')
        for i in range(y):
            lis.append("<tr>\n")
            for i in range(x):
                lis.append('<td style=" padding-left:10; padding-right:10; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;">Yo</td>\n')
            else:
                lis.append("</tr>\n")

        else:
            lis.append("</table>")
            st = " ".join(lis)
            self.textEdit.insertHtml(st)
            ht = self.textEdit.toHtml()
            ht1 = ht.replace('<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">', "")
            ht2 = ht1.replace("</p>", "")
            self.textEdit.setHtml(ht2)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow().setupUi()
    app.exec_()
