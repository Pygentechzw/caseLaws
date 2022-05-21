from gui.uis.windows.main_window import UI_MainWindow
from gui.uis.windows.main_window.functions_main_window import MainFunctions


class CaseLawButtons:
    def __init__(self):
        super().__init__()

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    def home_button_clicks(self):
        self.ui.load_pages.pushButton_2.clicked.connect(
            lambda: MainFunctions.set_page(self, self.ui.load_pages.caseLawJudgements))
        self.ui.load_pages.pushButton.clicked.connect(
            lambda: MainFunctions.set_page(self, self.ui.load_pages.caseLawJudgements))
