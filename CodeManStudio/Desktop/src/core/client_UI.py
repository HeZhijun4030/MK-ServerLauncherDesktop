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
        Form.resize(820, 558)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 229, 153))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/res/Copyright_He.png"))

        self.verticalLayout.addWidget(self.label_2)

        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(230, 0, 591, 481))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.console = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.console.setObjectName(u"console")

        self.verticalLayout_2.addWidget(self.console)

        self.command_input = QLineEdit(self.verticalLayoutWidget_2)
        self.command_input.setObjectName(u"command_input")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.command_input.sizePolicy().hasHeightForWidth())
        self.command_input.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        self.command_input.setFont(font1)

        self.verticalLayout_2.addWidget(self.command_input)

        self.verticalLayoutWidget_3 = QWidget(Form)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 150, 160, 111))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Start = QPushButton(self.verticalLayoutWidget_3)
        self.Start.setObjectName(u"Start")
        self.Start.setFont(font)

        self.verticalLayout_3.addWidget(self.Start)

        self.Stop = QPushButton(self.verticalLayoutWidget_3)
        self.Stop.setObjectName(u"Stop")
        self.Stop.setFont(font)

        self.verticalLayout_3.addWidget(self.Stop)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u53cd\u6b63\u662fMK-ServerLauncher\u684c\u9762\u7248\u5c31\u5bf9\u4e86", None))
        self.label_2.setText("")
        self.Start.setText(QCoreApplication.translate("Form", u"Start", None))
        self.Stop.setText(QCoreApplication.translate("Form", u"Stop", None))
    # retranslateUi

