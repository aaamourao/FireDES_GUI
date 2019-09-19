from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, \
        QGridLayout, QWidget, QPushButton, QMenuBar, QMenu, \
        QStatusBar, QAction, QSizePolicy
import sys
from visualtools import VisualTools
from automatagrid import AutomataGrid
from itemlist import ItemList
from terminal import Terminal


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.resize(1143, 732)
        self.setWindowTitle("FireDES")

        self.centralWidget = QWidget(self)
        self.layout = QGridLayout(self.centralWidget)
        self.centralWidgetSetup()

        self.visualTools = VisualTools(self.centralWidget)
        self.layout.addWidget(self.visualTools, 0, 0)

        self.menuBarSetup()

        self.automataGrid = AutomataGrid(self.centralWidget)
        self.layout.addWidget(self.automataGrid, 0, 1)

        self.itemList = ItemList(self.centralWidget)
        self.layout.addWidget(self.itemList, 0, 2)

        self.terminal = Terminal(self.centralWidget)
        self.layout.addWidget(self.terminal, 1, 0, 1, 3)

    def centralWidgetSetup(self):
        self.setCentralWidget(self.centralWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum,
                QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)

    def menuBarSetup(self):
        self.menuFile = self.menuBar().addMenu("File")
        self.menuEdit = self.menuBar().addMenu("Edit")
        self.menuView = self.menuBar().addMenu("View")
        self.menuTools = self.menuBar().addMenu("Tools")
        self.menuRun = self.menuBar().addMenu("Run")
        self.menuHelp = self.menuBar().addMenu("Help")

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
