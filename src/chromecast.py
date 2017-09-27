import pychromecast
from PyQt5 import QtCore

class ChromecastScanner(QtCore.QThread):
  
  newChromecast = QtCore.pyqtSignal(object)

  def __init__(self):
    super(ChromecastScanner,self).__init__()

  def run(self):
    for cast in pychromecast.get_chromecasts():
      self.newChromecast.emit(cast)
