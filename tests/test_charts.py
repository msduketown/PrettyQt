#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `prettyqt` package."""

from qtpy import QtCore
from prettyqt import charts


def test_chart():
    chart = charts.Chart(parent=None)
    chart.hide_legend()
    chart.show_legend()
    chart.set_legend_alignment("right")
    chart.set_theme("Dark")
    chart.set_animation_options("series")


def test_chartview(qtbot):
    widget = charts.ChartView(parent=None)
    widget.get_image()
    qtbot.addWidget(widget)
    qtbot.keyPress(widget, QtCore.Qt.Key_F11)
    # qtbot.keyPress(widget, QtCore.Qt.Key_Minus)
    # qtbot.keyPress(widget, QtCore.Qt.Key_Plus)
    qtbot.keyPress(widget, QtCore.Qt.Key_Left)
    qtbot.keyPress(widget, QtCore.Qt.Key_Right)
    qtbot.keyPress(widget, QtCore.Qt.Key_Up)
    qtbot.keyPress(widget, QtCore.Qt.Key_Down)


def test_lineseries():
    charts.LineSeries()


def test_scatterseries():
    charts.ScatterSeries()