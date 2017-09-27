import utils
from channels import *
from chromecast import *
from flowlayout import FlowLayout
from PyQt5 import uic, QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):

  def __init__(self,args=None):
    super(MainWindow, self).__init__()
    uic.loadUi(utils.get_file('mainwindow.ui'), self)
    self.show()
    self.args = args
    self.scan_button = self.findChild(QtWidgets.QPushButton, "scanButton")
    self.combo_cast = self.findChild(QtWidgets.QComboBox,"comboCast")
    self.channels_layout = FlowLayout()
    self.scroll_contents = self.findChild(QtWidgets.QWidget,"scroll_contents")
    self.scroll_contents.setLayout(self.channels_layout)
    self.get_channels()
    self.get_chromecasts()

  def get_channels(self):
    self.channels = {}
    self.cp = ChannelParser(self.args)
    self.cp.newChannel.connect(self.onNewChannel)
    self.cp.cannotRetrieveChannels.connect(self.onCannotRetrieveChannels)
    self.cp.start()

  def get_chromecasts(self):
    self.combo_cast.clear()
    self.cs = ChromecastScanner()
    self.cs.newChromecast.connect(self.onNewChromecast)
    self.cs.start()

  def get_selected_chromecast(self):
    sci = self.combo_cast.currentIndex()
    cast = self.combo_cast.itemData(sci)
    return cast

  # Slots
 
  def onScan(self):
    self.get_chromecasts()
 
  def onPlay(self):
    button = self.sender()
    channel = self.channels[button]
    cast = self.get_selected_chromecast()
    if(cast):
      cast.wait()
      cast.media_controller.play_media(channel['stream'],'video/mp4')

  @QtCore.pyqtSlot()
  def onCannotRetrieveChannels(self):
    QtWidgets.QMessageBox.warning(self,"Error","Cannot retrieve channels")
 
  @QtCore.pyqtSlot(object)
  def onNewChannel(self,channel):
    button = QtWidgets.QPushButton()
    button.setMaximumWidth(60)
    button.setMinimumHeight(60)
    button.clicked.connect(self.onPlay)
    button.setToolTip(channel['name'])
    self.channels[button] = channel
    tf = channel.get('icon-tempfile')
    if(tf):
      button.setIcon(QtGui.QIcon(tf.fileName()))
      tf.remove()
    self.channels_layout.addWidget(button)

  @QtCore.pyqtSlot(object)
  def onNewChromecast(self,cast):
    self.combo_cast.addItem(cast.device.friendly_name,userData=cast)
