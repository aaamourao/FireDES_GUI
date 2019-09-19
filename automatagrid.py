from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QTabWidget, QSizePolicy, QWidget


class DrawingArea(QWidget):
    def __init__(self, *args, **kwargs):
        super(DrawingArea, self).__init__(*args, **kwargs)
        self.sizePolicySetup()
        self.points = QPolygon()

    def sizePolicySetup(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.points << event.pos()
            self.update()
        super(DrawingArea, self).mousePressEvent(event)

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)
        radx = 30
        rady = 30
        # draw red circles
        paint.setPen(Qt.red)
        for i in range(self.points.count()):
            paint.drawEllipse(self.points.point(i), radx, rady)
        print("DEBUG: created state")
        paint.end()

class AutomataGrid(QTabWidget):

    def __init__(self, *args, **kwargs):
        super(AutomataGrid, self).__init__(*args, **kwargs)
        self.setGeometry(156, 6, 707, 511)
        self.sizePolicySetup()
        self.newTab()

    def sizePolicySetup(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

    def newTab(self, label="unnamed_automaton"):
        drawingArea = DrawingArea(self)
        drawingArea.setAutoFillBackground(True)
        p = drawingArea.palette()
        p.setColor(drawingArea.backgroundRole(), Qt.white)
        drawingArea.setPalette(p)
        drawingArea.setMouseTracking(True)
        self.addTab(drawingArea, label)


