from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget, QPushButton
import sys
from visualtools import VisualTools
from automata_grid import AutomataGrid
from itemlist import ItemList


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.main_widget = QWidget(self)
        self.visual_toolbox = VisualTools(self)
        self.automata_grid = AutomataGrid(self)
        self.item_list = ItemList(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1143, 732)
        self.setWindowTitle("FireDES")
        self.setCentralWidget(self.main_widget)

        layout = QGridLayout()
        self.main_widget.setLayout(layout)

        layout.addWidget(self.visual_toolbox, 1, 1)
        layout.addWidget(self.automata_grid, 1, 2)
        layout.addWidget(self.item_list, 1, 3)


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
