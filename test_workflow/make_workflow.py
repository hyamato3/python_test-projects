'''
Created on 2016/09/29

@author: H.Yamato
'''
import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from search_text import *

class workFlow(QWidget):
    print('import makeWorkFlow')
    
    def makeWorkFlow(self, numType, numName):      
        self.w = QWidget()
        self.w.resize(300, 500)
        self.w.move(300, 300)
        
        self.w.setWindowTitle('Workflow')
        
        grid = QGridLayout(self.w)
        
        #btnUse1 = QRadioButton("pre - Rendering", self.w)
        #btnUse1.clicked.connect(self.onClickedPre)
        #layout1.addWidget(btnUse1, 1, 0)
        
        #btnUse2 = QRadioButton("real time - Rendering", self.w)
        #btnUse2.clicked.connect(self.onClickedReal)
        #layout1.addWidget(btnUse2, 2, 0)        
        
        for i in range(numType):
            self.groupBoxUse = QGroupBox("model", self.w)
            layout1 = QGridLayout()
            
            for j in range(numName):
                btnA = QPushButton('button', self.w)
                layout1.addWidget(btnA, 1, j)
                btnA.clicked.connect(self.PushButtonA)
            
            self.groupBoxUse.setLayout(layout1)
            grid.addWidget(self.groupBoxUse, 1, i)
            
            print('makeButtonA!')
        self.w.show()
        
    def PushButtonA(self):
        print('Push A!')
        
#このモジュール単体でのテスト用
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    
    st = SearchText()
    it = st.ImportText()
    
    stype = st.SearchType(it)
    nt = st.NumberType(stype)
    
    sname = st.SearchName(it)
    nn = st.NumberName(sname)
    
    print(stype)
    print(sname)
    
    wf = workFlow()
    wf.makeWorkFlow(nt, nn)
    
    print(type(nt))
    print(type(nn))
    
    sys.exit(app.exec_())