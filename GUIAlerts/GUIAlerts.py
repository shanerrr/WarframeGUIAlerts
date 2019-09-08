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
 
        self.pcbut.clicked.connect(self.nextwindow)#####

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Warframe Alerts Hub"))
        self.pcbut.setText(_translate("MainWindow", "PC"))
        self.ps4but.setText(_translate("MainWindow", "PS4"))
        self.xboxbut.setText(_translate("MainWindow", "XBOX"))
        self.Swibut.setText(_translate("MainWindow", "SWITCH"))
        self.quitbut.setText(_translate("MainWindow", "QUIT"))
    
    def nextwindow(self):
        self.switch_window.emit()


class Home(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.AlertsText = QtWidgets.QTextBrowser(Dialog)
        self.AlertsText.setGeometry(QtCore.QRect(10, 10, 471, 571))
        self.AlertsText.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.AlertsText.setObjectName("AlertsText")
        self.syndicatebut = QtWidgets.QPushButton(Dialog)
        self.syndicatebut.setGeometry(QtCore.QRect(550, 240, 201, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.syndicatebut.setFont(font)
        self.syndicatebut.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.syndicatebut.setObjectName("syndicatebut")
        self.fissurebut = QtWidgets.QPushButton(Dialog)
        self.fissurebut.setGeometry(QtCore.QRect(550, 270, 201, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.fissurebut.setFont(font)
        self.fissurebut.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.fissurebut.setObjectName("fissurebut")
        self.sortiebut = QtWidgets.QPushButton(Dialog)
        self.sortiebut.setGeometry(QtCore.QRect(550, 300, 201, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.sortiebut.setFont(font)
        self.sortiebut.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.sortiebut.setObjectName("sortiebut")
        self.MainPagebg = QtWidgets.QLabel(Dialog)
        self.MainPagebg.setGeometry(QtCore.QRect(310, 0, 791, 661))
        self.MainPagebg.setText("")
        self.MainPagebg.setPixmap(QtGui.QPixmap("Elements/bg.png"))
        self.MainPagebg.setObjectName("MainPagebg")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(570, 560, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 560, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.MainPagebg.raise_()
        self.AlertsText.raise_()
        self.syndicatebut.raise_()
        self.fissurebut.raise_()
        self.sortiebut.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.nextwindow)#####

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.syndicatebut.setText(_translate("Dialog", "Syndicate Alerts"))
        self.fissurebut.setText(_translate("Dialog", "Fissure Alerts"))
        self.sortiebut.setText(_translate("Dialog", "Sortie Alerts"))
        self.pushButton.setText(_translate("Dialog", "HOME"))
        self.pushButton_2.setText(_translate("Dialog", "QUIT"))

    def nextwindow(self):
        self.switch_window.emit()


    #def __init__(self):
        #QtWidgets.QWidget.__init__(self)
        #self.setWindowTitle('Login')

        #layout = QtWidgets.QGridLayout()

        #self.button = QtWidgets.QPushButton('Login')

        #layout.addWidget(self.button)

        #self.setLayout(layout)

    #def login(self):
        #self.switch_window.emit()



class Controller:

    def __init__(self,ui,ui2,window,dialog):

        self.windowone = ui
        self.windowmain = window

        self.windowtwo = ui2
        self.windowtwomain = dialog

    def show_main(self):

        self.windowtwo.close()
        self.windowone.show()

        self.windowmain.switch_window.connect(self.show_home)
        self.windowmain.quitbut.clicked.connect(self.windowone.close)
        print(self.windowmain.pcbut.text())

    def show_home(self):

        self.windowone.close()
        self.windowtwo.show()

        #QUIT and HOME button functions, respectively
        self.windowtwomain.pushButton_2.clicked.connect(self.windowtwo.close)
        self.windowtwomain.pushButton.clicked.connect(self.show_main)


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
    #main window
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #home window
    Dialog = QtWidgets.QDialog()
    ui2 = Home()
    ui2.setupUi(Dialog)

    controller = Controller(MainWindow,Dialog,ui,ui2)
    controller.show_main()
    sys.exit(app.exec_())

