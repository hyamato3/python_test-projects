'''
Created on 2016/09/30

@author: H.Yamato
'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from read_text import *
from library_parts import *

class MakeWorkflow(QWidget):
    def __init__(self):
        self.dRp = {1:'Rp1', 2:'Rp2', 3:'Rp3', 4:'Rp4', 5:'Rp5', 6:'Rp6', 7:'Rp7', 8:'Rp8'}
        self.dDp = {1:'Dp1', 2:'Dp2', 3:'Dp3', 4:'Dp4', 5:'Dp5', 6:'Dp6', 7:'Dp7', 8:'Dp8'}
        self.dFp = {1:'Fp1', 2:'Fp2', 3:'Fp3', 4:'Fp4', 5:'Fp5', 6:'Fp6', 7:'Fp7', 8:'Fp8'}
    
    def startWindow(self, prodName):
        self.w = QWidget()
        self.w.resize(500, 400)
        self.w.setWindowTitle('制作物：' + prodName)
    
    def makeButton(self):
        g = QGridLayout(self.w)
        
        #ラフモデル段階
        gpR = QGroupBox('ラフモデル段階', self.w)
        gridR = QGridLayout(self.w)
        
        for i in range(8):
            if str(self.dRp[i+1]) != '':
                gpRp = QGroupBox(str(lb.getLb(self.dRp[i+1], 'name')), self.w)
                gridRp = QGridLayout(self.w)
                
                if str(lb.getLb(self.dRp[i+1], 'tech1')) != '' :
                    btnRp1 = QPushButton(str(lb.getLb(self.dRp[i+1], 'tech1')))
                    gridRp.addWidget(btnRp1)
                else:
                    print('')
            
                if str(lb.getLb(self.dRp[i+1], 'tech2')) != '' :
                    btnRp2 = QPushButton(str(lb.getLb(self.dRp[i+1], 'tech2')))
                    gridRp.addWidget(btnRp2)
                else:
                    print('')
                gridR.addWidget(gpRp, 1, 0+i)
                gpRp.setLayout(gridRp)
            else:
                gpRp = QGroupBox('', self.w)
                gridRp = QGridLayout(self.w)
                gridR.addWidget(gpRp, 1, 0+i)
                gpRp.setLayout(gridRp)
                
        
        gridR.addWidget(gpRp, 1, 0+i)
        gpR.setLayout(gridR)
        
        g.addWidget(gpR)
        
        #ディティールモデル段階
        gpD = QGroupBox('ディティールモデル段階', self.w)
        gridD = QGridLayout(self.w)
        
        for i in range(8):
            if str(self.dDp[i+1]) != '':
                gpDp = QGroupBox(str(lb.getLb(self.dDp[i+1], 'name')), self.w)
                gridDp = QGridLayout(self.w)
                
                if str(lb.getLb(self.dDp[i+1], 'tech1')) != '' :
                    btnDp1 = QPushButton(str(lb.getLb(self.dDp[i+1], 'tech1')))
                    gridDp.addWidget(btnDp1)
                else:
                    print('')
            
                if str(lb.getLb(self.dDp[i+1], 'tech2')) != '' :
                    btnDp2 = QPushButton(str(lb.getLb(self.dDp[i+1], 'tech2')))
                    gridDp.addWidget(btnDp2)
                else:
                    print('')
                gridD.addWidget(gpDp, 2, 0+i)
                gpDp.setLayout(gridDp)
                
            else:
                gpDp = QGroupBox('', self.w)
                gridDp = QGridLayout(self.w)
                gridD.addWidget(gpDp, 2, 0+i)
                gpDp.setLayout(gridDp)
            #else:
            #    print('?')
        
        gridD.addWidget(gpDp, 2, 0+i)
        gpD.setLayout(gridD)
        
        g.addWidget(gpD)
        
        #フィックスモデル段階
        gpF = QGroupBox('フィックスモデル段階', self.w)
        gridF = QGridLayout(self.w)
        
        for i in range(8):
            gpFp = QGroupBox(str(lb.getLb(self.dFp[i+1], 'name')), self.w)
            gridFp = QGridLayout(self.w)
            
            gridF.addWidget(gpFp, 3, 0+i)
            gpFp.setLayout(gridFp)
        
        gridF.addWidget(gpFp, 3, 0+i)
        gpF.setLayout(gridF)
        
        g.addWidget(gpF)

    def showWindow(self):
        self.w.show()

if __name__ == '__main__':
    rt = ReadText()
    rt.importText('workflow\workflow_car_v3.txt')

    lb = Library()
    lb.loadingLibrary(rt.getRt('layer1') ,rt.getRt('layer2'), rt.getRt('layer3'))
    
    app = QApplication(sys.argv)
    
    mw = MakeWorkflow()
    mw.startWindow(str(rt.getRt('prodName')))
    mw.makeButton()
    mw.showWindow()
    
    sys.exit(app.exec_())
