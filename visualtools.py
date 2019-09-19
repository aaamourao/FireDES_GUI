from PyQt5.QtWidgets import QWidget, QGridLayout, QToolButton, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *


class VisualTools(QWidget):

    def __init__(self, *args, **kwargs):
        super(VisualTools, self).__init__(*args, **kwargs)
        self.setGeometry(6, 6, 144, 511)
        self.layout = QGridLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

        self._setup_button = QToolButton()
        self._alphabet_button = QToolButton()
        self._state_button = QToolButton()
        self._istate_button = QToolButton()
        self._fstate_button = QToolButton()
        self._trans_button = QToolButton()
        self._select_button = QToolButton()
        self._move_button = QToolButton()

        sizePolicy = QSizePolicy(QSizePolicy.Fixed,
                QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.initUI()

    def initUI(self):
        self._setup_button.setToolTip('New event')
        self._setup_button.setIcon(QIcon('./icons/settings/normal_on.svg'))

        self._alphabet_button.setToolTip('New event')
        self._alphabet_button.setIcon(QIcon('./icons/alfabeto/normal_on.svg'))

        self._state_button.setToolTip('New State')
        self._state_button.setIcon(QIcon('./icons/estado/normal_on.svg'))

        self._istate_button.setToolTip('Set as initial state')
        self._istate_button.setIcon(QIcon('./icons/estado_inicial/normal_on.svg'))

        self._fstate_button.setToolTip('Set as final state')
        self._fstate_button.setIcon(QIcon('./icons/estado_marcado/normal_on.svg'))

        self._trans_button.setToolTip('New Transition')
        self._trans_button.setIcon(QIcon('./icons/transicao/normal_on.svg'))

        self._select_button.setToolTip('Select')
        self._select_button.setIcon(QIcon('./icons/selecionar/normal_on.svg'))

        self._move_button.setToolTip('move')
        self._move_button.setIcon(QIcon('./icons/mover/normal_on.svg'))

        self.layout.addWidget(self._setup_button, 0, 0)
        self.layout.addWidget(self._alphabet_button, 0, 1)
        self.layout.addWidget(self._state_button, 0, 2)
        self.layout.addWidget(self._istate_button, 1, 0)
        self.layout.addWidget(self._fstate_button, 1, 1)
        self.layout.addWidget(self._trans_button, 1, 2)
        self.layout.addWidget(self._select_button, 2, 0)
        self.layout.addWidget(self._move_button, 2, 1)


