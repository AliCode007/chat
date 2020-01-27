# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from post_login import Ui_Post_Login


class Ui_signUp(object):

    def __init__(self,client):
        self.client = client

    def insertData(self):
        username = self.uname_lineEdit.text()
        fullname = self.email_lineEdit.text()
        password = self.password_lineEdit.text()
        print(username,fullname,password)
        r = self.client.sign_up(username,fullname,password)
        if r['res'] == True:
            self.showPostLogin(r['keyPath'],r['certPath'])


    def showPostLogin(self,keyPath,certPath):
        self.postLoginWindow =QtWidgets.QDialog()
        self.ui = Ui_Post_Login(self.client)
        #######################################
        self.ui.setupUi(self.postLoginWindow,{"keyPath" :keyPath,"certPath" : certPath})
        #######################################
        self.postLoginWindow.show()
        self.Dialog.hide()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(334, 410)
        self.Dialog = Dialog
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.verticalLayout.addWidget(self.uname_lineEdit)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.email_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.verticalLayout.addWidget(self.email_lineEdit)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.verticalLayout.addWidget(self.password_lineEdit)
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
        ########################### Event #############################3
        self.signup_btn.clicked.connect(self.insertData)
        ################################################################
        self.verticalLayout.addWidget(self.signup_btn)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Create Account"))
        self.label.setText(_translate("Dialog", "USERNAME"))
        self.label_3.setText(_translate("Dialog", "FULLNAME"))
        self.label_2.setText(_translate("Dialog", "PASSWORD"))
        self.signup_btn.setText(_translate("Dialog", "Sign Up"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_signUp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

