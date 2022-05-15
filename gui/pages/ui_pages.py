# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesZmETFc.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# IMPORT QT CORE
from qt_core import *


class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName("application_pages")
        application_pages.resize(938, 644)
        self.page_1 = QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName("label_1")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_1)

        application_pages.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        application_pages.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        application_pages.addWidget(self.page_2)

        self.retranslateUi(application_pages)

        QMetaObject.connectSlotsByName(application_pages)

    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(
            QCoreApplication.translate("application_pages", "StackedWidget", None)
        )
        self.label_1.setText(
            QCoreApplication.translate("application_pages", "P\u00e1gina 1", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("application_pages", "P\u00e1gina 3", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("application_pages", "P\u00e1gina 2", None)
        )

    # retranslateUi
