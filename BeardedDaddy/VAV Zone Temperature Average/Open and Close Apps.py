import os

def openFile() :
    try:
        os.startfile("C:\AHU Supply Return Daily Report WO# 02400 April 29 Thursday.xlsm")
        
    except Exception, e:
        print str(e)