
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
    wd=wd+"\Elements"
    print(wd)
    chdir(wd)

    from mainP import *  #imports mainfile
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())
