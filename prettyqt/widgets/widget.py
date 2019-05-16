# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from typing import Dict
from contextlib import contextmanager

from qtpy import QtWidgets


class Widget(QtWidgets.QWidget):

    def __getstate__(self):
        return dict(layout=self.layout())

    def __setstate__(self, state):
        self.__init__()
        self.setLayout(state["layout"])

    def resize(self, *size):
        if isinstance(size[0], tuple):
            super().resize(*size[0])
        else:
            super().resize(*size)

    def set_enabled(self):
        self.setEnabled(True)

    def set_disabled(self):
        self.setEnabled(False)

    @contextmanager
    def block_signals(self):
        self.blockSignals(True)
        yield None
        self.blockSignals(False)

    def set_expanding(self):
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                           QtWidgets.QSizePolicy.Expanding)

    def set_color(self, color):
        self.setStyleSheet(f"background-color: {color};")

    def set_stylesheet(self, item, dct: Dict[str, str]) -> str:
        ss = "; ".join(f"{k.replace('_', '-')}: {v}" for k, v in dct.items())
        stylesheet = f"{item} {{{ss};}}"
        self.setStyleSheet(stylesheet)
        return stylesheet


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Widget()
    widget.show()
    app.exec_()
