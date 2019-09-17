from PyQt5.QtWidgets import QTabWidget


class AutomataGrid(QTabWidget):

    def __init__(self, *args, **kwargs):
        super(AutomataGrid, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setGeometry(156, 6, 511, 707)
