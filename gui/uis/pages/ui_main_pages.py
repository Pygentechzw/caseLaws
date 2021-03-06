# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesQYnJBo.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1144, 665)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)


        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_1)
        self.caseLawHome = QWidget()
        self.caseLawHome.setObjectName(u"caseLawHome")
        self.gridLayout = QGridLayout(self.caseLawHome)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.caseLawHome)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QWidget{ background-color: transparent ;}\n"
"QScrollArea{\n"
"	background-color: transparent;\n"
"	border:none;}\n"
"\n"
"QScrollBar:horizontal\n"
"    {\n"
"        height: 15px;\n"
"        margin: 3px 15px 3px 15px;\n"
"        border: 3px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"        background-color: black;    /* #2A2929; */\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::handle:horizontal\n"
"    {\n"
"        background-color: white;      /* #605F5F; */\n"
"        min-width: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal\n"
"    {\n"
"        margin: 0px 3px 0px 3px;\n"
"        border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"        width: 10px;\n"
"        height: 10px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:horizontal\n"
"    {\n"
"        margin: 0px 3px 0px 3px;\n"
"        border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"       "
                        " height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar:vertical"
                        "\n"
"    {\n"
"        background-color:#EAEDED;\n"
"        width: 15px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical\n"
"    {\n"
"        background-color: #C7C7C7;         /* #605F5F; */\n"
"        min-height: 9px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical::hover{\n"
"background-color: rgb(0, 95, 184);\n"
" min-height: 25px;\n"
"        border-radius: 4px;\n"
"}\n"
"\n"
"    QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"        height: 10px;\n"
"    "
                        "    width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background: none;\n"
"    }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -82, 1101, 724))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 1, 0, 1, 1)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(15)
        self.gridLayout_4.setContentsMargins(-1, 11, -1, 11)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(600, 40))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	/*background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(58, 74, 99, 255), stop:1 rgba(84, 84, 160, 251));*/\n"
"	background-color: #fbfbfb;\n"
"	border-radius:4px;\n"
"	border:1px solid #d2d2d2;\n"
"	padding: 5px;\n"
"	selection-color:white;\n"
"	selection-background-color:rgb(113, 113, 113);\n"
"	color:rgb(118, 118, 118);\n"
"    \n"
"}\n"
"QLineEdit:focus {\n"
"	border:2px solid #005fb8;\n"
"color: black;\n"
"font-weight:600;}\n"
"")

        self.gridLayout_4.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-weight:800;\n"
"font-size:22px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 1, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 2)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setStyleSheet(u"QFrame{background-color: transparent;border: 0px solid #E5E5E5;border-radius: 8px;padding:2px;}\n"
"color: rgb(245, 245, 245);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(10, 10, 10, 10)
        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(10, -1, 10, -1)
        self.pushButton_17 = QPushButton(self.frame_2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_10.addWidget(self.pushButton_17, 3, 5, 1, 1)

        self.pushButton_18 = QPushButton(self.frame_2)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_18.setIconSize(QSize(60, 60))

        self.gridLayout_10.addWidget(self.pushButton_18, 2, 7, 1, 1)

        self.pushButton_14 = QPushButton(self.frame_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setIconSize(QSize(60, 60))

        self.gridLayout_10.addWidget(self.pushButton_14, 2, 1, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setIconSize(QSize(60, 60))

        self.gridLayout_6.addWidget(self.pushButton_8, 0, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_6.addWidget(self.pushButton_7, 1, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_6, 0, 7, 1, 1)

        self.pushButton_25 = QPushButton(self.frame_2)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.gridLayout_10.addWidget(self.pushButton_25, 8, 5, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_5, 6, 5, 1, 1)

        self.pushButton_21 = QPushButton(self.frame_2)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.gridLayout_10.addWidget(self.pushButton_21, 8, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setIconSize(QSize(60, 60))

        self.gridLayout_8.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_8.addWidget(self.pushButton_3, 1, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_8, 0, 3, 1, 1)

        self.pushButton_26 = QPushButton(self.frame_2)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setIconSize(QSize(60, 60))

        self.gridLayout_10.addWidget(self.pushButton_26, 7, 7, 1, 1)

        self.pushButton_27 = QPushButton(self.frame_2)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.gridLayout_10.addWidget(self.pushButton_27, 8, 7, 1, 1)

        self.pushButton_29 = QPushButton(self.frame_2)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setIconSize(QSize(60, 60))

        self.gridLayout_10.addWidget(self.pushButton_29, 10, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_6, 9, 3, 1, 1)

        self.pushButton_23 = QPushButton(self.frame_2)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setIconSize(QSize(60, 60))

        self.gridLayout_10.addWidget(self.pushButton_23, 7, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.pushButton_15 = QPushButton(self.frame_2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_10.addWidget(self.pushButton_15, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 1, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.pushButton_24 = QPushButton(self.frame_2)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.gridLayout_10.addWidget(self.pushButton_24, 8, 3, 1, 1)

        self.pushButton_22 = QPushButton(self.frame_2)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setIconSize(QSize(60, 60))

        self.gridLayout_10.addWidget(self.pushButton_22, 7, 1, 1, 1)

        self.pushButton_19 = QPushButton(self.frame_2)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_10.addWidget(self.pushButton_19, 3, 7, 1, 1)

        self.pushButton_16 = QPushButton(self.frame_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_16.setIconSize(QSize(60, 60))

        self.gridLayout_10.addWidget(self.pushButton_16, 2, 5, 1, 1)

        self.pushButton_10 = QPushButton(self.frame_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setIconSize(QSize(60, 60))

        self.gridLayout_10.addWidget(self.pushButton_10, 2, 3, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setIconSize(QSize(60, 60))

        self.gridLayout_7.addWidget(self.pushButton_6, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_7.addWidget(self.pushButton_5, 1, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_7, 0, 5, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setIconSize(QSize(60, 60))

        self.gridLayout_9.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.pushButton, 1, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.frame_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_10.addWidget(self.pushButton_11, 3, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_6, 0, 6, 1, 1)

        self.pushButton_28 = QPushButton(self.frame_2)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.gridLayout_10.addWidget(self.pushButton_28, 11, 1, 1, 1)

        self.pushButton_30 = QPushButton(self.frame_2)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.gridLayout_10.addWidget(self.pushButton_30, 11, 3, 1, 1)

        self.pushButton_31 = QPushButton(self.frame_2)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setIconSize(QSize(60, 60))

        self.gridLayout_10.addWidget(self.pushButton_31, 10, 3, 1, 1)

        self.pushButton_32 = QPushButton(self.frame_2)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setIconSize(QSize(60, 60))

        self.gridLayout_10.addWidget(self.pushButton_32, 7, 5, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_10, 1, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 2, 0, 1, 2)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.pages.addWidget(self.caseLawHome)
        self.caseLawJudgements = QWidget()
        self.caseLawJudgements.setObjectName(u"caseLawJudgements")
        self.gridLayout_11 = QGridLayout(self.caseLawJudgements)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.scrollArea_2 = QScrollArea(self.caseLawJudgements)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"QWidget{ background-color: transparent ;}\n"
"QScrollArea{\n"
"	background-color: transparent;\n"
"	border:none;}\n"
"\n"
"QScrollBar:horizontal\n"
"    {\n"
"        height: 15px;\n"
"        margin: 3px 15px 3px 15px;\n"
"        border: 3px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"        background-color: black;    /* #2A2929; */\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::handle:horizontal\n"
"    {\n"
"        background-color: white;      /* #605F5F; */\n"
"        min-width: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal\n"
"    {\n"
"        margin: 0px 3px 0px 3px;\n"
"        border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"        width: 10px;\n"
"        height: 10px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:horizontal\n"
"    {\n"
"        margin: 0px 3px 0px 3px;\n"
"        border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"       "
                        " height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar:vertical"
                        "\n"
"    {\n"
"        background-color:#EAEDED;\n"
"        width: 15px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical\n"
"    {\n"
"        background-color: #C7C7C7;         /* #605F5F; */\n"
"        min-height: 9px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical::hover{\n"
"background-color: rgb(0, 95, 184);\n"
" min-height: 25px;\n"
"        border-radius: 4px;\n"
"}\n"
"\n"
"    QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"        height: 10px;\n"
"    "
                        "    width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background: none;\n"
"    }")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1101, 746))
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_4)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.pushButton_9 = QPushButton(self.frame_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(100, 16777215))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"border: 1.3px solid rgb(136, 136, 136);\n"
"padding: 5px;\n"
"border-radius: 8px;")

        self.gridLayout_19.addWidget(self.pushButton_9, 2, 0, 1, 1)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_19.addWidget(self.label_4, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_8, 2, 1, 1, 1)

        self.scrollArea_3 = QScrollArea(self.frame_4)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1059, 66))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_19.addWidget(self.scrollArea_3, 1, 0, 1, 2)


        self.gridLayout_20.addLayout(self.gridLayout_19, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_4, 1, 0, 1, 1)

        self.line = QFrame(self.scrollAreaWidgetContents_2)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"border: 1.5px solid rgb(227, 227, 227);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_14.addWidget(self.line, 2, 0, 1, 1)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_6)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.pushButton_13 = QPushButton(self.frame_6)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMaximumSize(QSize(100, 16777215))
        self.pushButton_13.setStyleSheet(u"border: 1.3px solid rgb(136, 136, 136);\n"
"padding: 5px;\n"
"border-radius: 8px;")

        self.gridLayout_17.addWidget(self.pushButton_13, 2, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.frame_6)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(432, 0))
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
"	background-color: : red;\n"
"    border: 0px solid rgb(220, 220, 220);\n"
"    border-radius: 4px;\n"
"    min-width: 20em;\n"
"color: rgb(166, 166, 166);\n"
"font-weight: 600;\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"border:2px solid rgb(198, 198, 198);\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: transparent;\n"
"padding: 6px;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: rgb(0, 95, 184);\n"
"color:white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: red;\n"
"    border-left-style: solid; /* just"
                        " a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
" ")

        self.gridLayout_17.addWidget(self.comboBox_2, 0, 0, 1, 2)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_13, 0, 2, 1, 1)

        self.scrollArea_5 = QScrollArea(self.frame_6)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1059, 66))
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_17.addWidget(self.scrollArea_5, 1, 0, 1, 3)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_10, 2, 1, 1, 2)


        self.gridLayout_22.addLayout(self.gridLayout_17, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_6, 5, 0, 1, 1)

        self.line_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"border: 1.5px solid rgb(227, 227, 227);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_14.addWidget(self.line_2, 4, 0, 1, 1)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_5)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.pushButton_12 = QPushButton(self.frame_5)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(100, 16777215))
        self.pushButton_12.setStyleSheet(u"border: 1.3px solid rgb(136, 136, 136);\n"
"padding: 5px;\n"
"border-radius: 8px;")

        self.gridLayout_18.addWidget(self.pushButton_12, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.frame_5)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(432, 0))
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"	background-color: : red;\n"
"    border: 0px solid rgb(220, 220, 220);\n"
"    border-radius: 4px;\n"
"    min-width: 20em;\n"
"color: rgb(166, 166, 166);\n"
"font-weight: 600;\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"border:2px solid rgb(198, 198, 198);\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: transparent;\n"
"padding: 6px;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: rgb(0, 95, 184);\n"
"color:white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: red;\n"
"    border-left-style: solid; /* just"
                        " a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
" ")
        self.comboBox.setIconSize(QSize(12, 12))

        self.gridLayout_18.addWidget(self.comboBox, 0, 0, 1, 2)

        self.scrollArea_4 = QScrollArea(self.frame_5)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1059, 66))
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_18.addWidget(self.scrollArea_4, 1, 0, 1, 3)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_12, 0, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_9, 2, 1, 1, 2)


        self.gridLayout_21.addLayout(self.gridLayout_18, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_5, 3, 0, 1, 1)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_7)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.dateEdit = QDateEdit(self.frame_7)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.dateEdit.setLayoutDirection(Qt.RightToLeft)
        self.dateEdit.setStyleSheet(u"color: rgb(166, 166, 166);\n"
"font-weight: 600;\n"
"font-size: 16px;\n"
"background:transparent;")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2022, 1, 1))

        self.gridLayout_16.addWidget(self.dateEdit, 0, 0, 1, 2)

        self.pushButton_20 = QPushButton(self.frame_7)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(100, 0))
        self.pushButton_20.setMaximumSize(QSize(100, 16777215))
        self.pushButton_20.setStyleSheet(u"border: 1.3px solid rgb(136, 136, 136);\n"
"padding: 5px;\n"
"border-radius: 8px;")

        self.gridLayout_16.addWidget(self.pushButton_20, 2, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_14, 0, 2, 1, 1)

        self.scrollArea_6 = QScrollArea(self.frame_7)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1059, 66))
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.gridLayout_16.addWidget(self.scrollArea_6, 1, 0, 1, 3)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_11, 2, 1, 1, 2)


        self.gridLayout_23.addLayout(self.gridLayout_16, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_7, 7, 0, 1, 1)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_3)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	/*background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(58, 74, 99, 255), stop:1 rgba(84, 84, 160, 251));*/\n"
"	background-color: #fbfbfb;\n"
"	border-radius:4px;\n"
"	border:1px solid #d2d2d2;\n"
"	padding: 5px;\n"
"	selection-color:white;\n"
"	selection-background-color:rgb(113, 113, 113);\n"
"	color:rgb(118, 118, 118);\n"
"    \n"
"}\n"
"QLineEdit:focus {\n"
"	border:2px solid #005fb8;\n"
"color: black;\n"
"font-weight:600;}\n"
"")

        self.gridLayout_24.addWidget(self.lineEdit_2, 0, 2, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-weight:600;\n"
"font-size:22px;")

        self.gridLayout_24.addWidget(self.label_3, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)


        self.gridLayout_14.addWidget(self.frame_3, 0, 0, 1, 1)

        self.line_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"border: 1.5px solid rgb(227, 227, 227);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_14.addWidget(self.line_3, 6, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_11.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.pages.addWidget(self.caseLawJudgements)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 214, 266))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.empty_page_label = QLabel(self.page_3)
        self.empty_page_label.setObjectName(u"empty_page_label")
        self.empty_page_label.setFont(font)
        self.empty_page_label.setAlignment(Qt.AlignCenter)

        self.page_3_layout.addWidget(self.empty_page_label)

        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To PyOneDark GUI", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainPages", u"Search Judgements, Legislation, Gazzettes, Covid-19 Legislation", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Good Morning, Jorja", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainPages", u"Speeches", None))
        self.pushButton_18.setText("")
        self.pushButton_14.setText("")
        self.pushButton_8.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainPages", u"Gazettes", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainPages", u"Zimbabwe Statutes", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainPages", u"Rules of Court", None))
        self.pushButton_4.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainPages", u"Legislation", None))
        self.pushButton_26.setText("")
        self.pushButton_27.setText(QCoreApplication.translate("MainPages", u"Speeches", None))
        self.pushButton_29.setText("")
        self.pushButton_23.setText("")
        self.pushButton_15.setText(QCoreApplication.translate("MainPages", u"Judges", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainPages", u"Causelist", None))
        self.pushButton_22.setText("")
        self.pushButton_19.setText(QCoreApplication.translate("MainPages", u"Documents", None))
        self.pushButton_16.setText("")
        self.pushButton_10.setText("")
        self.pushButton_6.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainPages", u"Covid-19 Legislation", None))
        self.pushButton_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainPages", u"Judgements", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainPages", u"Courts", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainPages", u"Results", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainPages", u"Legal Year Calendar", None))
        self.pushButton_31.setText("")
        self.pushButton_32.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("MainPages", u"Show More", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Latest Judgements", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainPages", u"Show More", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainPages", u"Show More", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainPages", u"dd MMMM yyyy", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainPages", u"Show More", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainPages", u"Search", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Judgements", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.empty_page_label.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
    # retranslateUi

