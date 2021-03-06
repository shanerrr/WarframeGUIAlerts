from PyQt5 import QtCore, QtGui, QtWidgets, uic
from urllib.request import urlopen, Request
import json

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
        self.bg.setPixmap(QtGui.QPixmap("bg.png"))
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
        self.AlertsText.setGeometry(QtCore.QRect(9, 9, 473, 573))
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
        self.MainPagebg.setPixmap(QtGui.QPixmap("bg.png"))
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
        self.alerttext1 = QtWidgets.QTextBrowser(Dialog)
        self.alerttext1.setGeometry(QtCore.QRect(10, 10, 157, 571))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.alerttext1.setFont(font)
        self.alerttext1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.alerttext1.setObjectName("alerttext1")
        self.alerttext1_3 = QtWidgets.QTextBrowser(Dialog)
        self.alerttext1_3.setGeometry(QtCore.QRect(324, 10, 157, 571))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.alerttext1_3.setFont(font)
        self.alerttext1_3.setAcceptDrops(True)
        self.alerttext1_3.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.alerttext1_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.alerttext1_3.setLineWidth(0)
        self.alerttext1_3.setObjectName("alerttext1_3")
        self.alerttext1_2 = QtWidgets.QTextBrowser(Dialog)
        self.alerttext1_2.setGeometry(QtCore.QRect(167, 10, 157, 571))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.alerttext1_2.setFont(font)
        self.alerttext1_2.setAcceptDrops(True)
        self.alerttext1_2.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.alerttext1_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.alerttext1_2.setLineWidth(1)
        self.alerttext1_2.setObjectName("alerttext1_2")
        self.textcycle = QtWidgets.QTextBrowser(Dialog)
        self.textcycle.setGeometry(QtCore.QRect(520, 10, 256, 192))
        self.textcycle.setObjectName("textcycle")
        self.MainPagebg.raise_()
        self.AlertsText.raise_()
        self.syndicatebut.raise_()
        self.fissurebut.raise_()
        self.sortiebut.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.alerttext1.raise_()
        self.alerttext1_3.raise_()
        self.alerttext1_2.raise_()
        self.textcycle.raise_()

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

        self.alerttext1_2.setFontWeight(QtGui.QFont.Bold)
        self.alerttext1_2.setFontUnderline(True)
        self.alerttext1_2.setTextColor(QtCore.Qt.red)
        self.alerttext1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.alerttext1_2.insertPlainText("ACTIVE ALERTS\n\n\n")

        self.alerttext1.setFontUnderline(True)
        self.alerttext1_3.setFontUnderline(True)
        self.alerttext1.setFontWeight(QtGui.QFont.Bold)
        self.alerttext1.setTextColor(QtCore.Qt.white)        
        self.alerttext1.setAlignment(QtCore.Qt.AlignCenter)
        self.alerttext1.insertPlainText("\n\n\nMISSION NAME:\n\n\n")
        self.alerttext1_2.setTextColor(QtCore.Qt.white)        
        self.alerttext1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.alerttext1_2.insertPlainText("MISSION NODE:\n\n\n")
        self.alerttext1_3.setFontWeight(QtGui.QFont.Bold)
        self.alerttext1_3.setTextColor(QtCore.Qt.white)        
        self.alerttext1_3.setAlignment(QtCore.Qt.AlignCenter)        
        self.alerttext1_3.insertPlainText("\n\n\nMISSION TYPE:\n\n\n")
        self.alerttext1_2.setFontUnderline(False)
        self.alerttext1_3.setFontUnderline(False)
        self.alerttext1.setFontUnderline(False)


        for alert in data['alerts']:

            #self.alerttext1.setTextColor(QtCore.Qt.green)
            self.alerttext1.setFontWeight(QtGui.QFont.Bold)
            self.alerttext1_2.setFontWeight(QtGui.QFont.Bold)
            self.alerttext1_3.setFontWeight(QtGui.QFont.Bold)
            
            self.alerttext1.insertPlainText(alert['mission']['description']+"\n")
            self.alerttext1_2.insertPlainText(alert['mission']['node']+"\n")
            self.alerttext1_3.insertPlainText(alert['mission']['type']+"\n")
            
            self.alerttext1.setTextColor(QtCore.Qt.white) 
            self.alerttext1.setFontWeight(QtGui.QFont.Normal)
            self.alerttext1_2.setFontWeight(QtGui.QFont.Normal)
            self.alerttext1_3.setFontWeight(QtGui.QFont.Normal)

            self.alerttext1_2.setFontUnderline(True)
            self.alerttext1_2.insertPlainText("Faction:\n")
            self.alerttext1_2.setFontUnderline(False)
            self.alerttext1_2.insertPlainText((alert['mission']['faction'])+"\n")

            self.alerttext1_3.setFontUnderline(True)
            self.alerttext1_3.insertPlainText("Enemy Level:\n")
            self.alerttext1_3.setFontUnderline(False)
            self.alerttext1_3.insertPlainText("("+ str(alert['mission']['minEnemyLevel'])+"-"+str(alert['mission']['maxEnemyLevel'])+")\n")

            self.alerttext1.setFontUnderline(True)
            self.alerttext1.insertPlainText("Rewards:\n")
            self.alerttext1.setFontUnderline(False)

            #print(len(alert['mission']['reward']['itemString']))
            if (len(alert['mission']['reward']['itemString']) >26):
                self.alerttext1_3.insertPlainText("\n")
                self.alerttext1_2.insertPlainText("\n")

            #gets date from combined date and time string
            num=0
            expiry=""
            while alert['expiry'][num] != "T":
                expiry=expiry + alert['expiry'][num]
                num = num +1

            #gets time from combined date and time string            
            num=((alert['expiry']).find("T")+1)
            expiryT=""
            while (alert['expiry'][num] != "."):
                expiryT=expiryT + alert['expiry'][num]
                num = num +1
     
            self.alerttext1.insertPlainText(alert['mission']['reward']['itemString']+"\n")
            self.alerttext1.insertPlainText("Credits:"+str(alert['mission']['reward']['credits'])+"\n\n\n\n"+"-----------------------------\n\n")
            self.alerttext1_2.setFontWeight(QtGui.QFont.Bold)
            self.alerttext1_2.insertPlainText("\n\n"+"Alert Expires:\n")
            self.alerttext1_2.setFontWeight(QtGui.QFont.Normal)
            self.alerttext1_2.insertPlainText(expiry+" at "+expiryT+"\n"+"-----------------------------\n\n")
            self.alerttext1_3.insertPlainText("\n\n\n\n"+"-----------------------------\n\n")

            #CetusandOrb Night/Day Cycle
        self.textcycle.setAlignment(QtCore.Qt.AlignCenter)
        self.textcycle.setFontWeight(QtGui.QFont.Bold)
        self.textcycle.setTextColor(QtCore.Qt.white)
        self.textcycle.insertPlainText("CETUS DAY/NIGHT CYCYLE\n\n")
        self.textcycle.insertPlainText("Current State:")
        if data['cetusCycle']["isDay"]:
            self.textcycle.setTextColor(QtCore.Qt.yellow)
            self.textcycle.insertPlainText(" Day\n")
            self.textcycle.setTextColor(QtCore.Qt.white)
            self.textcycle.insertPlainText("Time until ")
            self.textcycle.setTextColor(QtCore.Qt.red)
            self.textcycle.insertPlainText("Night:\n")
            self.textcycle.setTextColor(QtCore.Qt.white)
            self.textcycle.insertPlainText(data['cetusCycle']['timeLeft'])
               
        else:
            self.textcycle.setTextColor(QtCore.Qt.red)
            self.textcycle.insertPlainText(" Night\n")
            self.textcycle.setTextColor(QtCore.Qt.white)
            self.textcycle.insertPlainText("Time until ")
            self.textcycle.setTextColor(QtCore.Qt.yellow)            
            self.textcycle.insertPlainText("Day:\n")
            self.textcycle.setTextColor(QtCore.Qt.white)
            self.textcycle.insertPlainText(data['cetusCycle']['timeLeft'])

        #ORB VALLIS
        self.textcycle.insertPlainText("\n\n\nORB VALLIS WARM/COLD CYCYLE\n\n")
        self.textcycle.insertPlainText("Current State:")
        if data['vallisCycle']["isWarm"]:
            self.textcycle.setTextColor(QtGui.QColor(255,128,0))
            self.textcycle.insertPlainText(" Warm\n")
            self.textcycle.setTextColor(QtCore.Qt.white)
            self.textcycle.insertPlainText("Time until ")
            self.textcycle.setTextColor(QtCore.Qt.blue)
            self.textcycle.insertPlainText("Cold:\n")
            self.textcycle.setTextColor(QtCore.Qt.white)
            self.textcycle.insertPlainText(data['vallisCycle']['timeLeft'])
        else:
            self.textcycle.setTextColor(QtCore.Qt.blue)
            self.textcycle.insertPlainText(" Cold\n")
            self.textcycle.setTextColor(QtCore.Qt.white)
            self.textcycle.insertPlainText("Time until ")
            self.textcycle.setTextColor(QtGui.QColor(255,128,0))            
            self.textcycle.insertPlainText("Warm:\n")
            self.textcycle.setTextColor(QtCore.Qt.white)
            self.textcycle.insertPlainText(data['vallisCycle']['timeLeft'])

                    