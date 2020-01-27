# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'post_login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import time

from PyQt5.QtCore import pyqtSignal
from timeloop import  Timeloop


from PyQt5 import QtCore, QtGui, QtWidgets
from chat import Ui_Chat
from PyQt5.QtWidgets import QListWidgetItem

class QThread1(QtCore.QThread):

    sig1 = pyqtSignal(object)

    def __init__(self,client,parent=None):
        QtCore.QThread.__init__(self, parent)
        self.client =client

    def run(self):
        self.running = True
        while self.running:
            self.sig1.emit(self.client.get_logged_users())
            time.sleep(10)

class QThread2(QtCore.QThread):

    sig2 = pyqtSignal(object)

    def __init__(self,client,parent=None):
        QtCore.QThread.__init__(self, parent)
        self.client = client

    def run(self):
        self.running = True
        while self.running:
            if self.client.new == True :
                self.client.new = False
                message = self.client.message
                self.sig2.emit(message)
                time.sleep(5)




class Ui_Post_Login(object):

    def __init__(self,client):

        self.client = client
        self.thread1 = QThread1(self.client)
        self.users = []
        self.ui = None

    def handle_message(self,message):
        user = next(user for user in self.users if user["user"] == message['from'])
        if self.ui == None :
            self.showChat(user,message['msg'])
        else :
            self.ui.add_message(message['msg'])


   
    def showChat(self,user,msg = None):
        self.chatWindow =QtWidgets.QDialog()
        self.ui = Ui_Chat(self.client)
        #######################################
        self.ui.setupUi(self.chatWindow,user)
        #######################################
        self.chatWindow.show()
        if msg != None :
            self.ui.add_message(msg)

    def setupUsersList(self,users):
        self.listWidget.clear()
        self.users = users
        for user in users:
            if user['user'] != self.client.commonName:
                item = QtWidgets.QListWidgetItem()
                item.setText(user['user'])
                self.listWidget.addItem(item)
        self.listWidget.itemClicked.connect(lambda: self.showChat(
            next(user for user in users if user["user"] == self.listWidget.currentItem().text())))
        self.verticalLayout.addWidget(self.listWidget)

    def setupUi(self, Form , data):
        print(self.client.message)
        self.thread1 = QThread1(self.client)
        self.thread2 = QThread2(self.client)
        self.thread1.start()
        self.thread1.sig1.connect(self.setupUsersList)
        self.thread2.start()
        self.thread2.sig2.connect(self.handle_message)
        Form.setObjectName("Form")
        Form.resize(334, 410)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 311, 381))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.key_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.key_lineEdit.setObjectName("key_lineEdit")
        #######################################
        self.key_lineEdit.setText(data["keyPath"])
        #######################################
        self.verticalLayout.addWidget(self.key_lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.cert_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.cert_lineEdit.setObjectName("cert_lineEdit")
        #######################################
        self.cert_lineEdit.setText(data["certPath"])
        #######################################
        self.verticalLayout.addWidget(self.cert_lineEdit)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.thread1.start()
        self.thread1.sig1.connect(self.setupUsersList)
        self.thread2.start()
        self.thread2.sig2.connect(self.handle_message)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Post Login"))
        self.label.setText(_translate("Form", "your key path"))
        self.label_2.setText(_translate("Form", "your certificate path"))
        self.label_3.setText(_translate("Form", "Online Users"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Post_Login()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

