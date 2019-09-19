from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QTableWidget


class ItemList(QWidget):

    def __init__(self, *args, **kwargs):
        super(ItemList, self).__init__(*args, **kwargs)
        self.setGeometry(869, 6, 144, 511)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed,
                QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.tableWidget = QTableWidget()
        self.tableWidgetSetup()

    def tableWidgetSetup(self):
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(2)

        self.layout.addWidget(self.tableWidget)


