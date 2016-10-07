'''
Created on 2016/09/30

@author: H.Yamato
'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from read_text import *
from library_parts import *
from make_workflow import *

class mainWindow(QWidget):
    def makeMainWindow(self):
        self.w = QWidget()
        self.w.resize(250, 150)
        self.w.move(300, 300)
        self.w.setWindowTitle('GUI')
           
        btnStart = QPushButton('Start!', self.w)
        btnStart.clicked.connect(self.MakeUI)
            
        self.w.show()
            
    def MakeUI(self):
        print('makeUI!')
        
        self.mw = MakeWorkflow()
        mw = MakeWorkflow()
        mw.startWindow(str(rt.getRt('prodName')))
        mw.makeButton()
        
        self.mw.showWindow()
        
#このモジュール単体でのテスト用
if __name__ == '__main__':
    rt = ReadText()
    rt.importText('workflow\workflow_car_v2.txt')

    lb = Library()
    lb.loadingLibrary(rt.getRt('layer1') ,rt.getRt('layer2'), rt.getRt('layer3'))
    
    app = QApplication(sys.argv)
    
    m = mainWindow()
    m.makeMainWindow()
    
    sys.exit(app.exec_())