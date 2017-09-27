#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from mainwindow import *
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    args = None
    if len(sys.argv) > 1:
      args = sys.argv[1]
    window = MainWindow(args=args)
    sys.exit(app.exec_())
