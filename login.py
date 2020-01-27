# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from client import Client
from signup import Ui_signUp
from post_login import Ui_Post_Login
class Ui_Dialog(object):

    def __init__(self,client):
        self.client = client

    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
    def showPostLogin(self,paths):
        self.postLoginWindow =QtWidgets.QDialog()
        self.ui = Ui_Post_Login(client)
        #######################################
        self.ui.setupUi(self.postLoginWindow,paths)
        #######################################
        self.postLoginWindow.show()
        self.Dialog.hide()

    def signUpShow(self):
        self.signUpWindow = QtWidgets.QDialog()
        self.ui = Ui_signUp(client)
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()
        self.Dialog.hide()

    def loginCheck(self):
        username = self.uname_lineEdit.text()
        password = self.pass_lineEdit.text()
        certif = str(self.plainTextEdit.toPlainText())
        res = self.client.sign_in(username,password,certif)
        if res['res'] == True :
            paths = self.client.check_certif_key(username)
            self.showPostLogin(paths)


        
    def signUpCheck(self):
        print(" Sign Up Button Clicked !")
        self.signUpShow()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(334, 410)
        Dialog.setStyleSheet("")
        self.Dialog = Dialog
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setStyleSheet("QPushButton#evilButton {\n"
"    background-color: red;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.gridLayout.addWidget(self.uname_lineEdit, 3, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pass_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass_label.setFont(font)
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.gridLayout.addWidget(self.pass_label, 4, 0, 1, 1)
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setStyleSheet("QPushButton {\n"
"    background-color: #59B2E0;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}")
        self.login_btn.setObjectName("login_btn")
        ######################### Button Event ##############################3
        self.login_btn.clicked.connect(self.loginCheck)
        #####################################################################
        self.gridLayout.addWidget(self.login_btn, 9, 0, 1, 1)
        self.pass_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.pass_lineEdit.setText("")
        self.pass_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.gridLayout.addWidget(self.pass_lineEdit, 5, 0, 1, 1)
        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setStyleSheet("QPushButton {\n"
"    background-color: #59B2E0;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}")
        self.signup_btn.setObjectName("signup_btn")
        ######################### Button Event ##############################3
        self.signup_btn.clicked.connect(self.signUpCheck)
        #####################################################################
        self.gridLayout.addWidget(self.signup_btn, 10, 0, 1, 1)
        self.u_name_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.u_name_label.setFont(font)
        self.u_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.u_name_label.setObjectName("u_name_label")
        self.gridLayout.addWidget(self.u_name_label, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "CERTIFICAT"))
        self.label.setText(_translate("Dialog", "Sign in"))
        self.pass_label.setText(_translate("Dialog", "PASSWORD"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.signup_btn.setText(_translate("Dialog", "Sign Up"))
        self.u_name_label.setText(_translate("Dialog", "PSEUDO"))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    client = Client()
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(client)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

