import json
import requests
from PyQt5 import QtCore

class ChannelParser(QtCore.QThread):

  newChannel = QtCore.pyqtSignal(object)
  cannotRetrieveChannels = QtCore.pyqtSignal()
  default_uri = 'https://raw.githubusercontent.com/marioballano/fanCastic/master/cfg/channels.json'

  def __init__(self,uri):
    super(ChannelParser, self).__init__()
    self.uri = uri
    if self.uri == None:
      self.uri = self.default_uri

  def download_icon(self,channel):
    try:
      r = requests.get(channel['icon'])
      f = QtCore.QTemporaryFile()
      if (f.open()):
        f.write(r.content)
        f.close()
        channel['icon-tempfile'] = f
    except: pass

  def run(self):
    try:
      if(self.uri.startswith('http')):
        r = requests.get(self.uri)
        channels = r.json()
      else:
        with open(self.uri,'r') as fh:
          channels = json.loads(fh.read())
          fh.close()
      for channel in channels:
        self.download_icon(channel)
        self.newChannel.emit(channel)
    except:
      self.cannotRetrieveChannels.emit()
