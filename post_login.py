# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'post_login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from chat import Ui_Chat
from PyQt5.QtWidgets import QListWidgetItem  
class Ui_Post_Login(object):

    def __init__(self,client):
        self.client = client
   
    def showChat(self,user):
        self.chatWindow =QtWidgets.QDialog()
        self.ui = Ui_Chat(self.client)
        #######################################
        self.ui.setupUi(self.chatWindow,user)
        #######################################
        self.chatWindow.show()

    def setupUi(self, Form , data):
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
        users = self.client.get_logged_users()
        self.listWidget.setObjectName("listWidget")
        for user in users:
            if user['user'] != self.client.commonName :
                item = QtWidgets.QListWidgetItem()
                item.setText(user['user'])
                self.listWidget.addItem(item)
        self.listWidget.itemClicked.connect(lambda: self.showChat(next(user for user in users if user["user"] == self.listWidget.currentItem().text())))
        self.verticalLayout.addWidget(self.listWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        def setupUsersList(self):


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

