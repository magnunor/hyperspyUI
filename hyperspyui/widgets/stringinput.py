# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 02:43:41 2016

@author: Vidar Tonaas Fauske
"""

from python_qt_binding import QtGui, QtCore
from QtCore import *
from QtGui import *


class StringInputDialog(QDialog):

    def __init__(self, prompt="", default="", parent=None):
        super(StringInputDialog, self).__init__(parent=parent)
        self.setWindowTitle("Input prompt")
        self.setWindowFlags(Qt.Tool)

        frm = QFormLayout()
        self.edit = QLineEdit(default)
        frm.addRow(prompt, self.edit)

        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
                                Qt.Horizontal, self)
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)

        box = QVBoxLayout(self)
        box.addLayout(frm)
        box.addWidget(btns)
        self.setLayout(box)

    def prompt_modal(self, rejection=None):
        dr = self.exec_()
        if dr == QDialog.Accepted:
            return self.edit.text()
        else:
            return rejection

    def _on_completed(self, result):
        (callback, rejection) = self._on_completed_info
        if result == QDialog.Accepted:
            value = self.edit.text()
        else:
            value = rejection
        callback(value)

    def prompt_modeless(self, callback, rejection=None):
        self._on_completed_info = (callback, rejection)
        dr = self.show()
        dr.finished.connect(self._on_completed)