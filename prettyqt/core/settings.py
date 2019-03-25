# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

import contextlib

from qtpy import QtCore

FORMATS = dict(native=QtCore.QSettings.NativeFormat,
               ini=QtCore.QSettings.IniFormat)

SCOPES = dict(user=QtCore.QSettings.UserScope,
              system=QtCore.QSettings.SystemScope)


class Settings(QtCore.QSettings):

    def __init__(self, settings_id=None):
        self.settings_id = settings_id
        super().__init__()

    def __enter__(self):
        if self.settings_id:
            self.beginGroup(self.settings_id)
        return self

    def __contains__(self, key):
        return self.contains(key)

    def __exit__(self, exc_type, exc_value, traceback):
        if self.settings_id:
            self.endGroup()

    def set_value(self, key, value):
        self.setValue(key, value)

    def value(self, value, default=None):
        self.value(value, default)

    @staticmethod
    def set_default_format(fmt):
        if fmt not in FORMATS:
            raise ValueError("Format must be either 'native' or 'ini'")
        QtCore.QSettings.setDefaultFormat(FORMATS[fmt])

    @staticmethod
    def set_path(fmt, scope, path):
        if fmt not in FORMATS:
            raise ValueError("Format must be either 'native' or 'ini'")
        if scope not in SCOPES:
            raise ValueError("Format must be either 'native' or 'ini'")
        QtCore.QSettings.setPath(FORMATS[fmt], SCOPES[scope], path)

    @contextlib.contextmanager
    def group(self, prefix):
        self.beginGroup(prefix)
        yield None
        self.endGroup()

    @contextlib.contextmanager
    def write_array(self, prefix, size=-1):
        self.beginWriteArray(prefix, size)
        yield None
        self.endArray()

    @contextlib.contextmanager
    def read_array(self, prefix):
        self.beginReadArray(prefix)
        yield None
        self.endArray()