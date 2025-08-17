# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import client_Res

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(1280, 720)
        self.verticalLayoutWidget_3 = QWidget(Form)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 40, 131, 681))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.overview = QPushButton(self.verticalLayoutWidget_3)
        self.overview.setObjectName(u"overview")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setBold(True)
        font.setWeight(75)
        self.overview.setFont(font)

        self.verticalLayout_3.addWidget(self.overview)

        self.server = QPushButton(self.verticalLayoutWidget_3)
        self.server.setObjectName(u"server")
        self.server.setFont(font)

        self.verticalLayout_3.addWidget(self.server)

        self.environment = QPushButton(self.verticalLayoutWidget_3)
        self.environment.setObjectName(u"environment")
        self.environment.setFont(font)

        self.verticalLayout_3.addWidget(self.environment)

        self.pushButton = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.verticalLayout_3.addWidget(self.pushButton)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 363, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.info2 = QLabel(self.horizontalLayoutWidget)
        self.info2.setObjectName(u"info2")
        self.info2.setPixmap(QPixmap(u":/res/Copyright_He.png"))

        self.horizontalLayout.addWidget(self.info2)

        self.info1 = QLabel(self.horizontalLayoutWidget)
        self.info1.setObjectName(u"info1")
        self.info1.setFont(font)

        self.horizontalLayout.addWidget(self.info1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(130, 40, 1151, 681))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.main = QStackedWidget(self.frame)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(0, -1, 1151, 681))
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Plain)
        self.Overview = QWidget()
        self.Overview.setObjectName(u"Overview")
        self.main.addWidget(self.Overview)
        self.Server = QWidget()
        self.Server.setObjectName(u"Server")
        self.main.addWidget(self.Server)

        self.retranslateUi(Form)

        self.main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.overview.setText(QCoreApplication.translate("Form", u"Overview", None))
        self.server.setText(QCoreApplication.translate("Form", u"Server", None))
        self.environment.setText(QCoreApplication.translate("Form", u"Environment", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"About", None))
        self.info2.setText("")
        self.info1.setText(QCoreApplication.translate("Form", u"\u53cd\u6b63\u662fMK-ServerLauncher\u684c\u9762\u7248\u5c31\u5bf9\u4e86", None))
    # retranslateUi

