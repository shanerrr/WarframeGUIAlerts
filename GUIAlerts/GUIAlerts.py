from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Ui_MainWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setEnabled(True)
        self.bg.setGeometry(QtCore.QRect(9, 9, 782, 541))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("Elements/bg.png"))
        self.bg.setAlignment(QtCore.Qt.AlignCenter)
        self.bg.setObjectName("bg")
        self.pcbut = QtWidgets.QPushButton(self.centralwidget)
        self.pcbut.setGeometry(QtCore.QRect(190, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        self.pcbut.setFont(font)
        self.pcbut.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255);")
        self.pcbut.setObjectName("pcbut")
        self.ps4but = QtWidgets.QPushButton(self.centralwidget)
        self.ps4but.setGeometry(QtCore.QRect(300, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        self.ps4but.setFont(font)
        self.ps4but.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255);")
        self.ps4but.setObjectName("ps4but")
        self.xboxbut = QtWidgets.QPushButton(self.centralwidget)
        self.xboxbut.setGeometry(QtCore.QRect(420, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(8)
        self.xboxbut.setFont(font)
        self.xboxbut.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255);")
        self.xboxbut.setObjectName("xboxbut")
        self.Swibut = QtWidgets.QPushButton(self.centralwidget)
        self.Swibut.setGeometry(QtCore.QRect(530, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.Swibut.setFont(font)
        self.Swibut.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255);")
        self.Swibut.setObjectName("Swibut")
        self.quitbut = QtWidgets.QPushButton(self.centralwidget)
        self.quitbut.setGeometry(QtCore.QRect(360, 520, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.quitbut.setFont(font)
        self.quitbut.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 0, 0);")
        self.quitbut.setObjectName("quitbut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setEnabled(False)
        self.menuFile.setTitle("")
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
        self.pcbut.clicked.connect(self.login)#####

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Warframe Alerts Hub"))
        self.pcbut.setText(_translate("MainWindow", "PC"))
        self.ps4but.setText(_translate("MainWindow", "PS4"))
        self.xboxbut.setText(_translate("MainWindow", "XBOX"))
        self.Swibut.setText(_translate("MainWindow", "SWITCH"))
        self.quitbut.setText(_translate("MainWindow", "QUIT"))
    
    def login(self):
        self.switch_window.emit()


class Home(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Login')

        layout = QtWidgets.QGridLayout()

        self.button = QtWidgets.QPushButton('Login')

        layout.addWidget(self.button)

        self.setLayout(layout)

    def login(self):
        self.switch_window.emit()



class Controller:

    def __init__(self,ui,window):

        self.windowone = ui
        self.windowmain = window

    def show_main(self):

        self.windowone.show()
        self.windowmain.switch_window.connect(self.show_home)
        self.windowmain.quitbut.clicked.connect(self.windowone.close)
        print(self.windowmain.pcbut.text())

    def show_home(self):

        self.home = Home()
        self.home.switch_window.connect(self.show)

        self.windowone.close()
        self.home.show()

    def show_window_two(self, text):

        self.window_two = WindowTwo(text)
        self.window.close()
        self.window_two.show()



if __name__ == "__main__":

    #ensures path is in working directory
    from os import chdir, getcwd
    wd=getcwd()
    print(wd)
    chdir(wd)

    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    controller = Controller(MainWindow,ui)
    controller.show_main()
    sys.exit(app.exec_())

