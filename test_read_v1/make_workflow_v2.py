'''
Created on 2016/09/30

@author: H.Yamato
'''
import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from read_text import *

print('import make_workflow_v1!')

class workFlow(QWidget):
    
    def makeWorkFlow(self, ProdName, dictName, dictRoughSymbol, dictDetailNumber, dictTech1, dictTech2, dictComment, numName):      
        self.w = QWidget()
        self.w.resize(500, 700)
        self.w.move(100, 100)
        self.w.setWindowTitle('制作物：' + ProdName)
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
            self.groupBoxDP = QGroupBox(dictName[i+1], self.w)
            
            g.addWidget(self.groupBoxDP, 2, 0+i)
            
            if dictTech1[i+1] == 'tech1_':
                print('手法系なし')
            else:
                btnB1 = QPushButton(dictTech1[i+1], self.w)
                layout2.addWidget(btnB1, 1, 0+i)
            
            if dictTech2[i+1] == 'tech2_':
                print('手法系なし')
            else:
                btnB2 = QPushButton(dictTech2[i+1], self.w)
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
    
    rt = ReadText()
    ProdName, dictDetail, dictRough = rt.ImportText('workflow\workflow_car_v1.txt')
    
    dictName, dictRoughSymbol, dictDetailNumber, dictTech1, dictTech2, dictComment, numName = rt.SearchDetail(dictDetail)
    
    wf = workFlow()
    wf.makeWorkFlow(ProdName, dictName, dictRoughSymbol, dictDetailNumber, dictTech1, dictTech2, dictComment, numName)
    wf.EndWindow()
    
    sys.exit(app.exec_())
    