# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from typing import Union

import qtawesome as qta
from qtpy import QtWidgets, QtGui

from prettyqt import core, widgets, gui

STYLES = dict(close=QtWidgets.QStyle.SP_TitleBarCloseButton,
              maximise=QtWidgets.QStyle.SP_TitleBarMaxButton)


QtWidgets.QAbstractButton.__bases__ = (widgets.Widget,)


class AbstractButton(QtWidgets.QAbstractButton):

    def __getstate__(self):
        return dict(object_name=self.id,
                    text=self.text(),
                    icon=gui.Icon(self.icon()) if not self.icon().isNull() else None,
                    checkable=self.isCheckable(),
                    checked=self.isChecked(),
                    tooltip=self.toolTip(),
                    statustip=self.statusTip(),
                    enabled=self.isEnabled())

    def __setstate__(self, state):
        self.__init__()
        self.setText(state["text"])
        self.id = state.get("object_name", "")
        self.set_icon(state["icon"])
        self.setEnabled(state.get("enabled", True))
        self.setChecked(state.get("checked", False))
        self.setCheckable(state["checkable"])
        self.setToolTip(state.get("tooltip", ""))
        self.setStatusTip(state.get("statustip", ""))

    def set_icon(self, icon: Union[QtGui.QIcon, str, None]):
        """set the icon for the button

        Args:
            icon: icon to use
        """
        if not icon:
            icon = gui.Icon()
        elif isinstance(icon, str):
            icon = qta.icon(icon)
        self.setIcon(icon)

    def set_style_icon(self, icon: str, size: int = 15):
        if icon not in STYLES:
            raise ValueError(f"{icon!r} not a valid icon.")
        qicon = self.style().standardIcon(STYLES[icon], None, self)
        self.set_icon(qicon)
        self.setIconSize(core.Size(size, size))

    def set_shortcut(self, shortcut):
        if shortcut:
            self.setShortcut(shortcut)


if __name__ == "__main__":
    app = widgets.app()
    widget = AbstractButton()
    widget.show()
    app.exec_()
