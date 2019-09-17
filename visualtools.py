from PyQt5.QtWidgets import QWidget, QGridLayout, QToolButton
from PyQt5.QtGui import QIcon


class VisualTools(QWidget):

    def __init__(self, *args, **kwargs):
        super(VisualTools, self).__init__(*args, **kwargs)
        self._setup_button = QToolButton()
        self._alphabet_button = QToolButton()
        self._state_button = QToolButton()
        self._istate_button = QToolButton()
        self._fstate_button = QToolButton()
        self._trans_button = QToolButton()
        self._select_button = QToolButton()
        self._move_button = QToolButton()

        self.initUI()

    def initUI(self):
        self.setGeometry(6, 6, 511, 144)

        layout = QGridLayout()
        self.setLayout(layout)

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

        layout.addWidget(self._setup_button, 1, 1)
        layout.addWidget(self._alphabet_button, 1, 2)
        layout.addWidget(self._state_button, 1, 3)
        layout.addWidget(self._istate_button, 2, 1)
        layout.addWidget(self._fstate_button, 2, 2)
        layout.addWidget(self._trans_button, 2, 3)
        layout.addWidget(self._select_button, 3, 1)
        layout.addWidget(self._move_button, 3, 2)

