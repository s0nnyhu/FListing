# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listing.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os
import subprocess
import fnmatch

class Ui_mainWin(object):
    def setupUi(self, mainWin):
        mainWin.setObjectName("mainWin")
        mainWin.resize(445, 313)
        mainWin.setStyleSheet("")
        self.frame = QtWidgets.QFrame(mainWin)
        self.frame.setGeometry(QtCore.QRect(-30, 10, 471, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gpBox = QtWidgets.QGroupBox(self.frame)
        self.gpBox.setGeometry(QtCore.QRect(30, 0, 431, 61))
        self.gpBox.setObjectName("gpBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.gpBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 411, 31))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tbDir = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.tbDir.setObjectName("tbDir")
        self.gridLayout_2.addWidget(self.tbDir, 1, 1, 1, 1)
        self.lbDir = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbDir.setObjectName("lbDir")
        self.gridLayout_2.addWidget(self.lbDir, 1, 0, 1, 1)
        self.btnDir = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btnDir.setObjectName("btnDir")
        self.btnDir.clicked.connect(self.setDir)
        self.gridLayout_2.addWidget(self.btnDir, 1, 2, 1, 1)
        self.ckSubDir = QtWidgets.QCheckBox(self.frame)
        self.ckSubDir.setGeometry(QtCore.QRect(40, 60, 121, 17))
        self.ckSubDir.setObjectName("ckSubDir")
        self.gbRules = QtWidgets.QGroupBox(self.frame)
        self.gbRules.setGeometry(QtCore.QRect(30, 90, 431, 71))
        self.gbRules.setObjectName("gbRules")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.gbRules)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 411, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tbPattern = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.tbPattern.setObjectName("tbPattern")
        self.gridLayout_3.addWidget(self.tbPattern, 0, 1, 1, 1)
        self.lbPattern = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.lbPattern.setObjectName("lbPattern")
        self.gridLayout_3.addWidget(self.lbPattern, 0, 0, 1, 1)
        self.ckFile = QtWidgets.QCheckBox(self.frame)
        self.ckFile.setGeometry(QtCore.QRect(180, 60, 71, 17))
        self.ckFile.setObjectName("ckFile")
        self.ckFolder = QtWidgets.QCheckBox(self.frame)
        self.ckFolder.setGeometry(QtCore.QRect(270, 60, 71, 17))
        self.ckFolder.setObjectName("ckFolder")
        self.gbOutput = QtWidgets.QGroupBox(self.frame)
        self.gbOutput.setGeometry(QtCore.QRect(30, 160, 431, 101))
        self.gbOutput.setObjectName("gbOutput")
        self.gridLayoutWidget = QtWidgets.QWidget(self.gbOutput)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 411, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tbAfter = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.tbAfter.setObjectName("tbAfter")
        self.gridLayout.addWidget(self.tbAfter, 5, 1, 1, 1)
        self.lbAfter = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbAfter.setObjectName("lbAfter")
        self.gridLayout.addWidget(self.lbAfter, 5, 0, 1, 1)
        self.tbBefore = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.tbBefore.setObjectName("tbBefore")
        self.gridLayout.addWidget(self.tbBefore, 0, 1, 1, 1)
        self.lbBefore = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbBefore.setObjectName("lbBefore")
        self.gridLayout.addWidget(self.lbBefore, 0, 0, 1, 1)
        self.btnTree = QtWidgets.QPushButton(mainWin)
        self.btnTree.setGeometry(QtCore.QRect(20, 280, 81, 23))
        self.btnTree.setObjectName("btnTree")
        self.btnTree.clicked.connect(self.generateTree)
        self.btnList = QtWidgets.QPushButton(mainWin)
        self.btnList.setGeometry(QtCore.QRect(350, 280, 75, 23))
        self.btnList.setObjectName("btnList")
        self.btnList.clicked.connect(self.listComponent)

        self.retranslateUi(mainWin)
        QtCore.QMetaObject.connectSlotsByName(mainWin)


    def msgBox(self, firstText, secText):
        msgBox = QMessageBox()
        msgBox.setText(firstText)
        msgBox.setInformativeText(secText)
        msgBox.setDefaultButton(QMessageBox.Save)
        msgBox.setWindowIcon(QtGui.QIcon('folder.png'))
        ret = msgBox.exec_()


    def subDir_file(self, src, strBefore, strAfter):
        generated_file = open("listing.txt","w")
        for src, dirs, files in os.walk(src):
            #for d in dirs:
            #    generated_file.write(os.path.join(src, d) + "\n")  
            for f in files:
                generated_file.write(strBefore + os.path.join(src, f) + strAfter + "\n" )
        generated_file.close()

    def subDir_dir(self, src, strBefore, strAfter):
        generated_file = open("listing.txt","w")
        for src, dirs, files in os.walk(src):
            for d in dirs:
                generated_file.write(strBefore + os.path.join(src, d) + strAfter + "\n")  
            #for f in files:
            #    generated_file.write(os.path.join(src, f) + "\n")
        generated_file.close()

    def subDir_dir_file(self, src, strBefore, strAfter):
        generated_file = open("listing.txt","w")
        for src, dirs, files in os.walk(src):
            for d in dirs:
                generated_file.write(strBefore + os.path.join(src, d) + strAfter + "\n")  
            for f in files:
                generated_file.write(strBefore + os.path.join(src, f) + strAfter + "\n")
        generated_file.close()

    def get_dir_file_with_pattern(self, src, pattern, strBefore, strAfter):
        generated_file = open("listing.txt","w")
        for src, dirs, files in os.walk(src):
            for d in fnmatch.filter(dirs, pattern):
                generated_file.write(strBefore + os.path.join(src, d) + strAfter + "\n")  
            for f in fnmatch.filter(files, pattern):
                generated_file.write(strBefore + os.path.join(src, f) + strAfter + "\n")
        generated_file.close()


    def get_dir_with_pattern(self, src, pattern, strBefore, strAfter):
        generated_file = open("listing.txt","w")
        for src, dirs, files in os.walk(src):
            for d in fnmatch.filter(dirs, pattern):
                generated_file.write(strBefore + os.path.join(src, d) + strAfter + "\n")  
        generated_file.close()

    def get_file_with_pattern(self, src, pattern, strBefore, strAfter):
        generated_file = open("listing.txt","w")
        for src, dirs, files in os.walk(src): 
            for f in fnmatch.filter(files, pattern):
                generated_file.write(strBefore + os.path.join(src, f) + strAfter + "\n")
        generated_file.close()


    def get_file_pattern(self, src, pattern, strBefore, strAfter):
        generated_file = open("listing.txt","w")
        for src, dirs, files in os.walk(src, topdown=True):
            del dirs[:]
            for f in fnmatch.filter(files, pattern):
                generated_file.write(strBefore + (f) + strAfter + "\n")
        generated_file.close()

    def get_dir_pattern(self, src, pattern, strBefore, strAfter):
        generated_file = open("listing.txt","w")
        for _, dirs, _ in os.walk(src):
            for d in fnmatch.filter(dirs, pattern):
                generated_file.write(strBefore + (d) + strAfter + "\n")
            del dirs[:]  
        generated_file.close()

    def get_file(self, src, strBefore, strAfter):
        generated_file = open("listing.txt","w")
        for src, dirs, files in os.walk(src, topdown=True):
            del dirs[:]
            for f in files:
                generated_file.write(strBefore + (f) + strAfter + "\n")
        generated_file.close()

    def get_dir(self, src, strBefore, strAfter):
        generated_file = open("listing.txt","w")
        for _, dirs, _ in os.walk(src):
            for d in dirs:
                generated_file.write(strBefore + (d) + strAfter + "\n")
            del dirs[:]  
        generated_file.close()

    def setDir(self, mainWin):
        dir_to_scan = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.tbDir.setText(dir_to_scan)    

    def getTextBefore(self):
        return self.tbBefore.text()

    def getTextAfter(self):
        return self.tbAfter.text()

    def getTextDir(self):
        return self.tbDir.text()

    def getPattern(self):
        return self.tbPattern.text()

    def checkPath(self,src):
        if (os.path.isdir(src)):
            return True
        else:
            return False

    def listComponent(self):
        generated_file = open("listing.txt","w") 
        if(self.checkPath(self.getTextDir()) == True):
            if self.tbPattern.text() == "":
                if (self.ckSubDir.isChecked() and self.ckFile.isChecked() == False and self.ckFolder.isChecked() == False):
                    self.subDir_dir_file(self.getTextDir(), self.getTextBefore(), self.getTextAfter())
                elif (self.ckSubDir.isChecked() and self.ckFile.isChecked() and self.ckFolder.isChecked()):
                    self.subDir_dir_file(self.getTextDir(), self.getTextBefore(), self.getTextAfter())
                elif (self.ckSubDir.isChecked() and self.ckFile.isChecked() and self.ckFolder.isChecked() == False):
                    self.subDir_file(self.getTextDir(), self.getTextBefore(), self.getTextAfter())
                elif (self.ckSubDir.isChecked() and self.ckFile.isChecked() == False and self.ckFolder.isChecked() == True):
                    self.subDir_dir(self.getTextDir(), self.getTextBefore(), self.getTextAfter())
                elif (self.ckSubDir.isChecked() == False and self.ckFile.isChecked() == True and self.ckFolder.isChecked() == False):
                    self.get_file(self.getTextDir(), self.getTextBefore(), self.getTextAfter())
                elif (self.ckSubDir.isChecked() == False and self.ckFile.isChecked() == False and self.ckFolder.isChecked() == True):
                    self.get_dir(self.getTextDir(), self.getTextBefore(), self.getTextAfter())
                else:
                    for file in os.listdir(self.getTextDir()):
                        generated_file.write(self.getTextBefore() + file + self.getTextAfter() + "\n")
                self.msgBox("File has been generated!.", "Check out listing.txt")
            else:
                if (self.ckSubDir.isChecked() and self.ckFile.isChecked() == False and self.ckFolder.isChecked() == False):
                    self.get_dir_file_with_pattern(self.getTextDir(), self.getPattern(), self.getTextBefore(), self.getTextAfter())
                elif (self.ckSubDir.isChecked() and self.ckFile.isChecked() and self.ckFolder.isChecked()):
                    self.get_dir_file_with_pattern(self.getTextDir(), self.getPattern(), self.getTextBefore(), self.getTextAfter())
                elif (self.ckSubDir.isChecked() and self.ckFile.isChecked() and self.ckFolder.isChecked() == False):
                    self.get_file_with_pattern(self.getTextDir(), self.getPattern(), self.getTextBefore(), self.getTextAfter())
                elif (self.ckSubDir.isChecked() and self.ckFile.isChecked() == False and self.ckFolder.isChecked() == True):
                    self.get_dir_with_pattern(self.getTextDir(), self.getPattern(), self.getTextBefore(), self.getTextAfter())
                elif (self.ckSubDir.isChecked() == False and self.ckFile.isChecked() == True and self.ckFolder.isChecked() == False):
                    self.get_file_pattern(self.getTextDir(), self.getPattern(), self.getTextBefore(), self.getTextAfter())
                elif (self.ckSubDir.isChecked() == False and self.ckFile.isChecked() == False and self.ckFolder.isChecked() == True):
                    self.get_dir_pattern(self.getTextDir(), self.getPattern(), self.getTextBefore(), self.getTextAfter())
                else:
                    for file in os.listdir(self.getTextDir()):
                        generated_file.write(self.getTextBefore() + file + self.getTextAfter() + "\n")
                self.msgBox("File has been generated!.", "Check out listing.txt")
        else:
            self.msgBox("Oops, an error occured!", "Path does not exist.")
        
    def generateTree(self):
        if(self.checkPath(self.getTextDir()) == True):
            subprocess.call('tree /a "'+ self.getTextDir() +'"> tree.txt', shell=True)
            self.msgBox("File has been generated!.", "Check out tree.txt")
        else:
            self.msgBox("Oops, an error occured!", "Path does not exist.")

    def retranslateUi(self, mainWin):
        _translate = QtCore.QCoreApplication.translate
        mainWin.setWindowTitle(_translate("mainWin", "FListing"))
        self.gpBox.setTitle(_translate("mainWin", "Folder source"))
        self.lbDir.setText(_translate("mainWin", "Directory:"))
        self.btnDir.setText(_translate("mainWin", "Select"))
        self.ckSubDir.setText(_translate("mainWin", "Scan subdirectories"))
        self.gbRules.setTitle(_translate("mainWin", "Pattern rules"))
        self.lbPattern.setText(_translate("mainWin", "Specific pattern (regex):"))
        self.ckFile.setText(_translate("mainWin", "Files only"))
        self.ckFolder.setText(_translate("mainWin", "Folder only"))
        self.gbOutput.setTitle(_translate("mainWin", "Output editing"))
        self.lbAfter.setText(_translate("mainWin", "Text After"))
        self.lbBefore.setText(_translate("mainWin", "Text Before"))
        self.btnTree.setText(_translate("mainWin", "Tree structure"))
        self.btnList.setText(_translate("mainWin", "List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtWidgets.QDialog()
    ui = Ui_mainWin()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())

