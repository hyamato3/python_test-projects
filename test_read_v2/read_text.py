'''
Created on 2016/09/30

@author: H.Yamato
'''
import os

print('import read_text')

class ReadText():
    def __init__(self):
        self.prodName = ''
        self.layer1 = {}
        self.layer2 = {}
        self.layer3 = {}
        self.numlay1 = 1
        self.numlay2 = 1
        self.numlay3 = 1
    
    def importText(self, filename):
        #読み込んでとりあえず辞書に突っ込む
        f = open(filename, 'r')
        l = f.readlines()
        f.close
        
        #\nを削除する
        lines = ['lines']
        for i in range(len(l)):
            after = l[i].rstrip('\n')
            lines.append(after)
            
        #段階ごとに分ける
        num1 = 1
        num2 = 0

        for line in lines:
            if line == '___':
                num2 += 1
            elif num2 == 0:
                self.prodName = line
            elif num2 == 1: 
                self.layer1[self.numlay1] = line
                self.numlay1 += 1
            elif num2 == 2:
                self.layer2[self.numlay2] = line
                self.numlay2 += 1
            elif num2 == 3:
                self.layer3[self.numlay3] = line
                self.numlay3 += 1
            else:
                print('あれ、なんかデータおかしくない…？')
            num1 += 1
        
        self.numlay1 -= 1
        self.numlay2 -= 1
        self.numlay3 -= 1
        
        return self.prodName, self.layer1, self.layer2, self.layer3, self.numlay1, self.numlay2, self.numlay3
    
    def library(self):
        
        num1 = 1
        num2 = 1
        
        for i in range(self.numlay1):
            "dict" + str(i) = {}
            if self.layer1[i].wtartswitch('name_') == True:
                "dict" + str(i)['name']  = self.layer1[i]
        
    
    def getLib(self, tag):
        if tag == 'prodName':
            return self.prodName
        elif tag == 'layer1':
            return self.layer1
        elif tag == 'layer2':
            return self.layer2
        elif tag == 'layer3':
            return self.layer3
        elif tag == 'numlay1':
            return self.numlay1
        elif tag == 'numlay2':
            return self.numlay2
        elif tag == 'numlay3':
            return self.numlay3
    
if __name__=='__main__':
    rt = ReadText()
    rt.importText('workflow\workflow_car_v2.txt')
    
    print (rt.getLib('layer1'))
    print (rt.getLib('numlay1'))
    
    