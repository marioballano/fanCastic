# fanCastic

fanCastic is a simple PyQt5 application that streams TV channels to Chromecast devices, don't expect anything too fancy, I wrote this application as a quick hack to easily stream tv channels from my laptop and to have an up-to-date public template for PyQt5 apps.

# usage

fanCastic can either consume a local tv channels config file from the command line:

    $ ./fancastic.pyw <config-file>

or use the default configuration file ([channels.json](https://github.com/marioballano/fanCastic/blob/master/cfg/channels.json)), which is retrieved from github upon launching the app, feel free to send pull requests to add new channels :)

# builds 

I have generated an OSX build that does not require any additional dependencies, you can grab a copy from [here](https://github.com/marioballano/fanCastic/releases/tag/v0.1)

# screenshots

![fanCastic](/pics/fancastic.png "fanCastic")

# requirements

The following requirements are needed in order to build the application or to run it from sources:

* Python >= 3.4
* [Qt 5.9](https://www1.qt.io/download/)
* [PyQt5](https://pypi.python.org/pypi/PyQt5)
* [pychromecast](https://github.com/balloob/pychromecast)
