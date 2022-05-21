from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QLineEdit

from gui.uis.windows.main_window import UI_MainWindow


class CaseLawDesigns:
    def __init__(self):
        super().__init__()

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    def design_home_page(self):
        self.ui.load_pages.pushButton_2.setIcon(QIcon('gui/images/png_icons/icons8-scales-96.png'))
        self.ui.load_pages.pushButton_4.setIcon(QIcon('gui/images/png_icons/icons8-petition-96.png'))
        self.ui.load_pages.pushButton_6.setIcon(QIcon('gui/images/png_icons/icons8-covid-19-96.png'))
        self.ui.load_pages.pushButton_8.setIcon(QIcon('gui/images/png_icons/icons8-policy-document-96.png'))
        self.ui.load_pages.pushButton_14.setIcon(QIcon('gui/images/png_icons/icons8-law-96.png'))
        self.ui.load_pages.pushButton_10.setIcon(QIcon('gui/images/png_icons/icons8-courthouse-96 (1).png'))
        self.ui.load_pages.pushButton_16.setIcon(QIcon('gui/images/png_icons/icons8-voice-recognition-96.png'))
        self.ui.load_pages.pushButton_18.setIcon(QIcon('gui/images/png_icons/icons8-subpoena-96.png'))

        self.ui.load_pages.lineEdit.addAction(QIcon('gui/images/png_icons/icons8-law-962.png'),
                                              QLineEdit.TrailingPosition)
        self.ui.load_pages.lineEdit.addAction(QIcon('gui/images/png_icons/icons8-search-96.png'),
                                              QLineEdit.LeadingPosition)

        # self.ui.load_pages.pushButton_28.setIcon(QIcon('gui/images/png_icons/icons8-menu-vertical-96 - Copy.png'))
        # self.ui.load_pages.pushButton_29.setIcon(QIcon('gui/images/png_icons/icons8-menu-vertical-96 - Copy.png'))

    def design_judgement_page(self):
        self.ui.load_pages.pushButton_2.setIcon(QIcon('gui/images/png_icons/icons8-scales-96.png'))

        self.ui.load_pages.lineEdit_2.addAction(QIcon('gui/images/png_icons/icons8-law-962.png'),
                                                QLineEdit.TrailingPosition)
        self.ui.load_pages.lineEdit_2.addAction(QIcon('gui/images/png_icons/icons8-search-96.png'),
                                                QLineEdit.LeadingPosition)

        ico = QIcon('gui/images/png_icons/icons8-expand-arrow-96.png')
        self.ui.load_pages.comboBox.addItem(ico, 'Select Court')
        ico = QIcon('gui/images/png_icons/icons8-expand-arrow-96.png')
        self.ui.load_pages.comboBox_2.addItem(ico, 'Select Judge')
