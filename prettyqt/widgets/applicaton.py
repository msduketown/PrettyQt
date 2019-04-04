# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from qtpy import QtWidgets, QtCore
import qtawesome as qta


class Application(QtWidgets.QApplication):

    def set_icon(self, icon):
        if icon:
            if isinstance(icon, str):
                icon = qta.icon(icon, color="lightgray")
            self.setWindowIcon(icon)

    def set_language(self, path):
        translator = QtCore.QTranslator(self)
        translator.load(path)
        self.installTranslator(translator)
