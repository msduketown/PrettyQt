# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from bidict import bidict

from qtpy import QtWidgets, QtCore

from prettyqt import widgets

area = QtWidgets.QAbstractScrollArea

SIZE_POLICIES = bidict(dict(content=area.AdjustToContents,
                            first_show=area.AdjustToContentsOnFirstShow,
                            ignored=area.AdjustIgnored))


SCROLLBAR_POLICY = dict(always_on=QtCore.Qt.ScrollBarAlwaysOn,
                        always_off=QtCore.Qt.ScrollBarAlwaysOff,
                        as_needed=QtCore.Qt.ScrollBarAsNeeded)


class AbstractScrollArea(QtWidgets.QAbstractScrollArea):

    def set_size_policy(self, policy: str):
        """set size policy

        Args:
            policy: size policy to use

        Raises:
            ValueError: invalid size policy
        """
        if policy not in SIZE_POLICIES:
            raise ValueError("Policy not available")
        policy = SIZE_POLICIES.get(policy)
        self.setSizeAdjustPolicy(policy)

    def get_size_policy(self):
        return SIZE_POLICIES.inv[self.sizePolicy()]

    def set_horizontal_scrollbar_visibility(self, mode: str):
        self.setHorizontalScrollBarPolicy(SCROLLBAR_POLICY[mode])

    def set_vertical_scrollbar_visibility(self, mode: str):
        self.setVerticalScrollBarPolicy(SCROLLBAR_POLICY[mode])

    def set_horizontal_scrollbar_width(self, width):
        stylesheet = f"QScrollBar:horizontal {{height: {width}px;}}"
        self.horizontalScrollBar().setStyleSheet(stylesheet)

    def set_vertical_scrollbar_width(self, width):
        stylesheet = f"QScrollBar:vertical {{height: {width}px;}}"
        self.verticalScrollBar().setStyleSheet(stylesheet)

    def scroll_to_end(self):
        """scroll to the end of the text
        """
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())


AbstractScrollArea.__bases__[0].__bases__ = (widgets.Frame,)


if __name__ == "__main__":
    app = widgets.app()
    widget = AbstractScrollArea("This is a test")
    widget.show()
    app.exec_()