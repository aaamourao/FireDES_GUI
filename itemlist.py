from PyQt5.QtWidgets import QWidget, QGridLayout, QToolButton


class ItemList(QWidget):

    def __init__(self, *args, **kwargs):
        super(ItemList, self).__init__(*args, **kwargs)
        self._initUI()

    def _initUI(self):
        self.setGeometry(869, 6, 511, 144)
        layout = QGridLayout()
        self.setLayout(layout)
