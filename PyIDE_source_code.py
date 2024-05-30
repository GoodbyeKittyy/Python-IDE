# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import subprocess
import sys
import os
import tempfile
from shutil import rmtree
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Analyzer(object):
    def setupUi(self, Analyzer):
        Analyzer.setObjectName("Analyzer")
        Analyzer.resize(1400, 850)
        Analyzer.setMinimumSize(QtCore.QSize(1400, 850))
        Analyzer.setMaximumSize(QtCore.QSize(1400, 850))
        Analyzer.setStyleSheet("background-color: rgb(252, 255, 217);\n"
"color: rgb(0, 0, 0);\n"
"")
        Analyzer.setIconSize(QtCore.QSize(20, 30))
        self.centralwidget = QtWidgets.QWidget(Analyzer)
        self.centralwidget.setObjectName("centralwidget")
        self.Browse = QtWidgets.QLabel(self.centralwidget)
        self.Browse.setGeometry(QtCore.QRect(300, 0, 321, 41))
        self.Browse.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Browse.setFont(font)
        self.Browse.setWordWrap(True)
        self.Browse.setObjectName("Browse")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 1380, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.container_TE = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.container_TE.setMinimumSize(QtCore.QSize(0, 0))
        self.container_TE.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.container_TE.setStyleSheet("font: 12pt \"Segoe MDL2 Assets\";\n"
"background-color: rgb(255, 243, 178);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.container_TE.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe MDL2 Assets\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">#Welcome, write your code here !</span></p></body></html>")
        self.container_TE.setTabStopWidth(20)
        self.container_TE.setAcceptRichText(True)
        self.container_TE.setPlaceholderText("")
        self.container_TE.setObjectName("container_TE")
        self.horizontalLayout.addWidget(self.container_TE)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.output_LB = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.output_LB.setMinimumSize(QtCore.QSize(500, 0))
        self.output_LB.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_LB.setFont(font)
        self.output_LB.setObjectName("output_LB")
        self.horizontalLayout.addWidget(self.output_LB)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_download = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_download.setStyleSheet("font: 9pt \"Segoe MDL2 Assets\";\n"
"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_download.setObjectName("btn_download")
        self.horizontalLayout_2.addWidget(self.btn_download)
        self.btn_reset = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_reset.setStyleSheet("font: 9pt \"Segoe MDL2 Assets\";\n"
"background-color: rgb(254, 117, 26);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout_2.addWidget(self.btn_reset)
        self.btn_exe = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_exe.setStyleSheet("font: 9pt \"Segoe MDL2 Assets\";\n"
"background-color: rgba(18, 244, 90, 9);\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_exe.setObjectName("btn_exe")
        self.horizontalLayout_2.addWidget(self.btn_exe)
        spacerItem2 = QtWidgets.QSpacerItem(510, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(-4, 693, 271, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setStyleSheet("font: 87 10pt \"Segoe UI Black\";\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.TC_TE = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.TC_TE.setAlignment(QtCore.Qt.AlignCenter)
        self.TC_TE.setObjectName("TC_TE")
        self.horizontalLayout_3.addWidget(self.TC_TE)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(380, 763, 271, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setStyleSheet("font: 87 10pt \"Segoe UI Black\";\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.OFG_TE = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.OFG_TE.setAlignment(QtCore.Qt.AlignCenter)
        self.OFG_TE.setObjectName("OFG_TE")
        self.horizontalLayout_4.addWidget(self.OFG_TE)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(380, 693, 271, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setStyleSheet("font: 87 10pt \"Segoe UI Black\";\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.Total_Time_TE = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.Total_Time_TE.setAlignment(QtCore.Qt.AlignCenter)
        self.Total_Time_TE.setObjectName("Total_Time_TE")
        self.horizontalLayout_5.addWidget(self.Total_Time_TE)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(-4, 763, 271, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_7.setStyleSheet("font: 87 10pt \"Segoe UI Black\";\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.SC_TE = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.SC_TE.setAlignment(QtCore.Qt.AlignCenter)
        self.SC_TE.setObjectName("SC_TE")
        self.horizontalLayout_6.addWidget(self.SC_TE)
        self.op_LB = QtWidgets.QLabel(self.centralwidget)
        self.op_LB.setGeometry(QtCore.QRect(940, 10, 400, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.op_LB.setFont(font)
        self.op_LB.setStyleSheet("color: rgb(255, 0, 0);")
        self.op_LB.setAlignment(QtCore.Qt.AlignCenter)
        self.op_LB.setObjectName("op_LB")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 630, 261, 21))
        self.label.setStyleSheet("color: rgb(74, 141, 170);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.input_TE = QtWidgets.QTextEdit(self.centralwidget)
        self.input_TE.setGeometry(QtCore.QRect(890, 660, 501, 151))
        self.input_TE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_TE.setFrameShape(QtWidgets.QFrame.Box)
        self.input_TE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_TE.setObjectName("input_TE")
        self.op_LB_2 = QtWidgets.QLabel(self.centralwidget)
        self.op_LB_2.setGeometry(QtCore.QRect(1070, 630, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.op_LB_2.setFont(font)
        self.op_LB_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.op_LB_2.setAlignment(QtCore.Qt.AlignCenter)
        self.op_LB_2.setObjectName("op_LB_2")
        Analyzer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Analyzer)
        self.statusbar.setObjectName("statusbar")
        Analyzer.setStatusBar(self.statusbar)

        self.retranslateUi(Analyzer)
        self.btn_reset.clicked.connect(self.container_TE.clear)
        QtCore.QMetaObject.connectSlotsByName(Analyzer)


        #Response
        self.btn_exe.clicked.connect(self.onclicker)
        self.btn_exe.clicked.connect(self.output)#execution)
        self.btn_download.clicked.connect(self.download)

        self.retranslateUi(Analyzer)
        #Clickings
        
        self.btn_reset.clicked.connect(self.container_TE.clear)
        try:
            self.btn_reset.clicked.connect(self.stop)
        except(Exception):
            pass
        self.btn_reset.clicked.connect(self.container_TE.clear)
        QtCore.QMetaObject.connectSlotsByName(Analyzer)
        
        
    def Create(self):
        try :
            self.user=os.path.expanduser('~')
            self.user=self.user.replace('\\','/')
            os.mkdir(self.user+'/AppData/Local/Temp/parsing')
        #This is the directory where we store the temporary data
        except(FileExistsError):
            pass
            #folder already exists

        os.chdir(self.user+'/AppData/Local/Temp/parsing')
        # Select the directory
        # perforn all the work here .
   
    def makepy(self,mytext):
        self.Create()
        fo=open("parse.py","w+")
        fo.write(mytext)
        fo.close()
        f=open("output.txt","w+")
        f.close()


        
        
    def download(self):
        self.destination=os.path.expanduser('~')
        self.destination=self.destination+'\Downloads\program_analyzer.py'
        try:
            result=os.system('copy parse.py'+' '+self.destination)
            if result==0:
                self.statusbar.setStyleSheet("background-color:rgb(255,228,128); color:rgb(0,0,0);")
                self.statusbar.showMessage('Successfully Downloaded  on '+self.destination)
            else:
                self.statusbar.setStyleSheet("background-color:rgb(255,228,228); color:rgb(0,0,0);")
                self.statusbar.showMessage('Downloading Failed....')

        except(FileNotFound):
            self.statusbar.setStyleSheet("background-color:rgb(255,228,228); color:rgb(255,255,255);")
            self.statusbar.showMessage('Downloading Failed...."')
            
    def execution(self):
        os.chdir(self.user+'/AppData/Local/Temp/parsing')
        #result=os.system('python parse.py')
        result=self.output('python parse.py')
        if result==0:
            self.statusbar.setStyleSheet("background-color:rgb(69,207,0);")
            self.statusbar.showMessage('Successfully Executed')
        else:
            self.statusbar.setStyleSheet("background-color:rgb(255,30,0);")
            self.statusbar.showMessage('Error in Execution')
                        
    def stop(self):
        self.user=os.path.expanduser('~')
        self.user=self.user.replace('\\','/')
        os.chdir(self.user+'/AppData/Local/Temp/')
        try:
            rmtree('parsing')
        except(Exception):
            pass
        self.statusbar.setStyleSheet("background-color:rgb(252, 255, 217);")
        self.statusbar.showMessage('')
        self.output_LB.setText('')
    def show_op(self):
        #self.ops.setGeometry(QtCore.QRect(1100, 0, 1700, 850))
        f=open("output.txt", 'r')
        op=f.read()
        self.output_LB.setText(op)
        f.close()
    def get_input(self):
        #f=open('input.log','wb')
        op=''
        for i in sys.stdin:
            if 'EXT'== i.rstrip():
                break
            else:
                op=op+str(i)+'\n'
        return str.encode(op)
    def onclicker(self):
        mytext=self.container_TE.toPlainText()
        self.makepy(mytext)
    def output(self):
        self.user=os.path.expanduser('~')
        self.user=self.user.replace('\\','/')
        os.chdir(self.user+'/AppData/Local/Temp/parsing')
        self.command='python parse.py'
        f=open("output.txt", 'wb')  # replace 'w' with 'wb' for Python 3
        ret_val = subprocess.Popen( self.command,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
        
        #ret_val.stdin.write(self.getInput())

        output, errors = ret_val.communicate()
        f.write(output)
        f.write(errors)
        self.success=True
        if( ret_val.returncode ):
            self.success = False
        f.close()
        if self.success==True:
            self.statusbar.setStyleSheet("background-color:rgb(69,207,0);")
            self.statusbar.showMessage('Successfully Executed')
        if self.success==False:
            self.statusbar.setStyleSheet("background-color:rgb(255,30,0);")
            self.statusbar.showMessage('Error in Execution')
        self.show_op()



    def retranslateUi(self, Analyzer):
        _translate = QtCore.QCoreApplication.translate
        Analyzer.setWindowTitle(_translate("Analyzer", "PyIDE"))
        self.Browse.setText(_translate("Analyzer", "Program Analyzer"))
        self.output_LB.setHtml(_translate("Analyzer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_download.setText(_translate("Analyzer", "Download"))
        self.btn_reset.setText(_translate("Analyzer", "Reset"))
        self.btn_exe.setText(_translate("Analyzer", "Execute"))
        self.label_2.setText(_translate("Analyzer", "T(n)  :"))
        self.TC_TE.setText(_translate("Analyzer", "N/A"))
        self.label_3.setText(_translate("Analyzer", "Order of growth  :"))
        self.OFG_TE.setText(_translate("Analyzer", "N/A"))
        self.label_5.setText(_translate("Analyzer", "Size Of File :"))
        self.Total_Time_TE.setText(_translate("Analyzer", "N/A"))
        self.label_7.setText(_translate("Analyzer", "S(n)  :"))
        self.SC_TE.setText(_translate("Analyzer", "N/A"))
        self.op_LB.setText(_translate("Analyzer", "===========Output==========="))
        self.op_LB_2.setText(_translate("Analyzer", "Input"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Analyzer = QtWidgets.QMainWindow()
    ui = Ui_Analyzer()
    ui.setupUi(Analyzer)
    Analyzer.show()
    sys.exit(app.exec_())
