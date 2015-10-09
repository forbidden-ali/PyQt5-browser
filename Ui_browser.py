# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\workspace\browser\browser.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(730, 540)
        Dialog.setSizeGripEnabled(True)
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(21, 21, 75, 41))
        self.back.setObjectName("back")
        self.next = QtWidgets.QPushButton(Dialog)
        self.next.setGeometry(QtCore.QRect(102, 21, 75, 41))
        self.next.setObjectName("next")
        self.stop = QtWidgets.QPushButton(Dialog)
        self.stop.setGeometry(QtCore.QRect(183, 21, 75, 41))
        self.stop.setObjectName("stop")
        self.reload = QtWidgets.QPushButton(Dialog)
        self.reload.setGeometry(QtCore.QRect(264, 21, 75, 41))
        self.reload.setObjectName("reload")
        self.webView = QtWebKitWidgets.QWebView(Dialog)
        self.webView.setGeometry(QtCore.QRect(0, 80, 731, 461))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.url = QtWidgets.QLineEdit(Dialog)
        self.url.setGeometry(QtCore.QRect(345, 22, 361, 41))
        self.url.setObjectName("url")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "browser"))
        self.back.setText(_translate("Dialog", "back"))
        self.next.setText(_translate("Dialog", "next"))
        self.stop.setText(_translate("Dialog", "stop"))
        self.reload.setText(_translate("Dialog", "reload"))

from PyQt5 import QtWebKitWidgets



