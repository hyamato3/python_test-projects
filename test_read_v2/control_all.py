'''
Created on 2016/09/30

@author: H.Yamato
'''
from read_text import *
from library_parts import *
from make_workflow import *

if __name__=='__main__':
    rt = ReadText()
    rt.importText('workflow\workflow_car_v2.txt')

    lb = Library()
    lb.loadingLibrary(rt.getRt('layer1') ,rt.getRt('layer2'), rt.getRt('layer3'))
    
    app = QApplication(sys.argv)
    
    mw = MakeWorkflow()
    mw.startWindow(str(rt.getRt('prodName')))
    
    numR = lb.getLb('numR')
    numD = lb.getLb('numD')
    numF = lb.getLb('numF')
    
    RpTech1 = str(lb.getLb(self.dRp[i+1], 'tech1'))
    RpTech2 = str(lb.getLb(self.dRp[i+1], 'tech2'))
    DpTech1 = str(lb.getLb(self.dDp[i+1], 'tech1'))
    DpTech2 = str(lb.getLb(self.dDp[i+1], 'tech2'))
    FpTech1 = str(lb.getLb(self.dFp[i+1], 'tech1'))
    FpTech2 = str(lb.getLb(self.dFp[i+1], 'tech2'))
    
    mw.makeButton(numR, numD, numF, RpTech1, RpTech2, DpTech1, DpTech2, FpTech1, FpTech2)
    mw.showWindow()
    
    sys.exit(app.exec_())
