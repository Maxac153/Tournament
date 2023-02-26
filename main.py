#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main_form import Ui_MainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec())
