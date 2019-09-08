import json
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from urllib.request import urlopen, Request


class Ui_MainWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

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
        self.pc = QtWidgets.QPushButton(self.centralwidget)
        self.pc.setGeometry(QtCore.QRect(190, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        self.pc.setFont(font)
        self.pc.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255);")
        self.pc.setObjectName("pc")
        self.ps4 = QtWidgets.QPushButton(self.centralwidget)
        self.ps4.setGeometry(QtCore.QRect(300, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        self.ps4.setFont(font)
        self.ps4.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255);")
        self.ps4.setObjectName("ps4")
        self.xb1 = QtWidgets.QPushButton(self.centralwidget)
        self.xb1.setGeometry(QtCore.QRect(420, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(8)
        self.xb1.setFont(font)
        self.xb1.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255);")
        self.xb1.setObjectName("xb1")
        self.swi = QtWidgets.QPushButton(self.centralwidget)
        self.swi.setGeometry(QtCore.QRect(530, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.swi.setFont(font)
        self.swi.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255);")
        self.swi.setObjectName("swi")
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
 
        #RETURNS STRING OF PLATFORM DEPNDING ON BUTTON CLICK
        self.pc.clicked.connect(lambda:self.nextwindow(self.pc.objectName()))
        self.ps4.clicked.connect(lambda:self.nextwindow(self.ps4.objectName()))
        self.xb1.clicked.connect(lambda:self.nextwindow(self.xb1.objectName()))
        self.swi.clicked.connect(lambda:self.nextwindow(self.swi.objectName()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Warframe Alerts Hub"))
        self.pc.setText(_translate("MainWindow", "PC"))
        self.ps4.setText(_translate("MainWindow", "PS4"))
        self.xb1.setText(_translate("MainWindow", "XBOX"))
        self.swi.setText(_translate("MainWindow", "SWITCH"))
        self.quitbut.setText(_translate("MainWindow", "QUIT"))
    
    def nextwindow(self,butstr):
        self.switch_window.emit(butstr)


class Home(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def setupUi(self, Dialog, text):
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

        self.pushButton.clicked.connect(self.nextwindow)

        if text != str:
            self.alertdata(text)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Warframe Alerts Hub"))
        self.syndicatebut.setText(_translate("Dialog", "Syndicate Alerts"))
        self.fissurebut.setText(_translate("Dialog", "Fissure Alerts"))
        self.sortiebut.setText(_translate("Dialog", "Sortie Alerts"))
        self.pushButton.setText(_translate("Dialog", "HOME"))
        self.pushButton_2.setText(_translate("Dialog", "QUIT"))

    def nextwindow(self):
        self.switch_window.emit()

    def alertdata(self,platform):

        #fake browser visit to api URL
        headers = {'User-Agent': 'Mozilla/5.0'}
        WFAPI = ('https://api.warframestat.us/%s' % platform)
        req = Request(url=WFAPI, headers=headers)
        jsonobj = urlopen(req)

        #JSON
        data = json.load(jsonobj)

        self.AlertsText.setFontWeight(QtGui.QFont.Bold)
        self.AlertsText.setFontUnderline(True)
        self.AlertsText.setAlignment(QtCore.Qt.AlignCenter)
        self.AlertsText.setTextColor(QtCore.Qt.red)
        self.AlertsText.append("ACTIVE ALERTS\n\n\n")
        self.AlertsText.setFontWeight(QtGui.QFont.Normal)
        self.AlertsText.setFontUnderline(False)

        self.AlertsText.setTextColor(QtCore.Qt.white)
        self.AlertsText.setFontWeight(QtGui.QFont.Bold)
        self.AlertsText.insertPlainText("                 Mission Name: ")
        self.AlertsText.setAlignment(QtCore.Qt.AlignRight)
        self.AlertsText.insertPlainText("                 Mission Node:")
        self.AlertsText.setAlignment(QtCore.Qt.AlignLeft)
        self.AlertsText.insertPlainText("                 Mission Type:\n\n\n\n")


        for alert in data['alerts']:
            #self.AlertsText.setFontPointSize(11)
            self.AlertsText.insertPlainText("  " + alert['mission']['description']+"")
            self.AlertsText.setAlignment(QtCore.Qt.AlignLeft)
            self.AlertsText.insertPlainText("                     "+alert['mission']['node'])
            self.AlertsText.setAlignment(QtCore.Qt.AlignCenter)
            self.AlertsText.insertPlainText(alert['mission']['type']+"\n\n\n\n")
            #self.AlertsText.setAlignment(QtCore.Qt.AlignRight)
            #for alertname in alert['mission']:
                #self.AlertsText.append(alert['description'])#str(alertname['description']))

                #print(str(alertname['description'])



class Controller:
#controlls data from classes
    def __init__(self):

        #mainwindow init
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        #secondwindow init
        self.Dialog = QtWidgets.QDialog()
        self.ui2 = Home()
        self.ui2.setupUi(self.Dialog,str)

    def show_main(self):

        self.Dialog.close()
        self.MainWindow.show()
        #QUIT BUTTON
        self.ui.switch_window.connect(self.show_home)
        self.ui.quitbut.clicked.connect(self.MainWindow.close)

    def show_home(self,text):

        self.ui2.setupUi(self.Dialog,text)
        self.MainWindow.close()
        self.Dialog.show()

        #QUIT and HOME button functions, respectively
        self.ui2.pushButton_2.clicked.connect(self.Dialog.close)
        self.ui2.pushButton.clicked.connect(self.show_main)


    #def show_window_two(self, text):
        #self.window_two = WindowTwo(text)
        #self.window.close()
        #self.window_two.show()



if __name__ == "__main__":

    #ensures path is in working directory
    from os import chdir, getcwd
    wd=getcwd()
    print(wd)
    chdir(wd)

    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())

