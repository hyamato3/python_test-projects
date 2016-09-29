'''
Created on 2016/09/29

@author: H.Yamato
'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import make_workflow as mk

class mainWindow(QWidget):
    def makeMainWindow(self):
        self.w = QWidget()
        self.w.resize(250, 150)
        self.w.move(300, 300)
        self.w.setWindowTitle('MainWindow')
           
        btnStart = QPushButton('Start!', self.w)
        btnStart.clicked.connect(self.MakeUI)
            
        self.w.show()
            
    def MakeUI(self):
        print('makeUI!')
        
        wf = mk.workFlow()
        wf.makeWorkFlow()
        
#このモジュール単体でのテスト用
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    mw = mainWindow()
    mw.makeMainWindow()
    
    sys.exit(app.exec_())
    