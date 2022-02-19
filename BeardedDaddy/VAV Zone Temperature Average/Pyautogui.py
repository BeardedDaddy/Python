import pywinauto,time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
app = Application ().start(cmd_line=u'""')
time.sleep(1)
app.
