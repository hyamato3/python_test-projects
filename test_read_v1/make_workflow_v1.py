'''
Created on 2016/09/30

@author: H.Yamato
'''
import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from read_text import *

print('import make_workflow!')

class workFlow(QWidget):
    
    def makeWorkFlow(self, numName):      
        self.w = QWidget()
        self.w.resize(500, 700)
        self.w.move(300, 300)
        self.w.setWindowTitle('Workflow')
        g = QGridLayout(self.w)
        
        #ラフモデル段階
        for i in range(numName):
            layout1 = QGridLayout()
            self.groupBoxRP = QGroupBox("ラフパーツ", self.w)
            
            g.addWidget(self.groupBoxRP, 1, 0+i)
            
            btnA1 = QPushButton('手法系1', self.w)
            layout1.addWidget(btnA1, 1, 0+i)
            
            btnA2 = QPushButton('手法系2', self.w)
            layout1.addWidget(btnA2, 2, 0+i)
            
            self.groupBoxRP.setLayout(layout1)
        
        #ディティールモデル段階
        for i in range(numName):
            layout2 = QGridLayout()
            self.groupBoxDP = QGroupBox("ディティールパーツ", self.w)
            
            g.addWidget(self.groupBoxDP, 2, 0+i)
            
            btnB1 = QPushButton('手法系1', self.w)
            layout2.addWidget(btnB1, 1, 0+i)
            
            btnB2 = QPushButton('手法系2', self.w)
            layout2.addWidget(btnB2, 2, 0+i)
            
            self.groupBoxDP.setLayout(layout2)
        
        #ディティールモデル段階
        for i in range(numName):
            layout3 = QGridLayout()
            self.groupBoxFP = QGroupBox("フィックスパーツ", self.w)
            
            g.addWidget(self.groupBoxFP, 3, 0+i)
            
            self.groupBoxFP.setLayout(layout3)
            
    def EndWindow(self):
        self.w.show()
        
    def PushButtonA(self):
        print('Push A!')
        
#このモジュール単体でのテスト用
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    
    wf = workFlow()
    wf.makeWorkFlow(4)
    wf.EndWindow()
    
    sys.exit(app.exec_())
    
    