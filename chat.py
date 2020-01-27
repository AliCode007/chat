# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Chat(object):
    def __init__(self,client):
        self.client = client
        self.lastMessage = ''

    def send_message(self):
        msg = self.message_lineEdit.text()
        text = self.chat_textEdit.toPlainText() + '\n' +"You : "+msg
        self.chat_textEdit.clear()
        self.chat_textEdit.setText(text)
        self.client.send(msg,self.user['user'])

    def add_message(self,msg):
        print("current : ",msg,", last : ",self.lastMessage)
        if msg != self.lastMessage :
            fromm = self.user['user']
            text = self.chat_textEdit.toPlainText() + '\n' + fromm +' : '+msg
            print("the text to be added ",text)
            self.chat_textEdit.clear()
            self.chat_textEdit.setText(text)
            self.lastMessage = msg
        else:
            print("here")

    def setupUi(self, Form,user):
        self.user = user
        Form.setObjectName("Form")
        Form.resize(334, 410)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.chat_textEdit = QtWidgets.QTextEdit(Form)
        self.chat_textEdit.setObjectName("chat_textEdit")
        self.verticalLayout.addWidget(self.chat_textEdit)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.message_lineEdit = QtWidgets.QLineEdit(Form)
        self.message_lineEdit.setObjectName("message_lineEdit")
        ################################################
        self.message_lineEdit.returnPressed.connect(self.send_message)
        ################################################
        self.verticalLayout.addWidget(self.message_lineEdit)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form",'chat'))
        self.chat_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Form", "message"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Chat()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

