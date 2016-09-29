'''
Created on 2016/09/30

@author: H.Yamato
'''
import os
print('import read_text!')

class ReadText():
    def ImportText(self, filename):
        #読み込んで辞書に突っ込む
        f = open(filename, 'r')
        lines1 = f.readlines()
        f.close
        #テスト用
        #print(lines1)
        #print(type(lines1))
        
        #\nを削除する
        lines2 = ['lines2']
        for i in range(len(lines1)):
            after = lines1[i].rstrip('\n')
            lines2.append(after)
        #テスト用
        #print(lines2)
        #print(type(afterN))
        
        num = 1
        n = 0
        
        numRough = 1
        numDetail = 1
        
        ProdName = '制作物の名称'
        dictDetail = {0: 'dictDetail'}
        dictRough = {0: 'dictRough'}
        
        for line in lines2:
            if line == '___':
                n += 1
            elif n == 0:
                ProdName = line
            elif n == 1: 
                dictDetail[numDetail] = line
                numDetail += 1
            elif n == 2:
                dictRough[numRough] = line
                numRough += 1
            else:
                print('あれ、なんかデータおかしくない…？')
            num += 1
        
        return ProdName, dictDetail, dictRough

    def SearchDetail(self, dictDetail):
        #読み込んだ辞書からネームだけを選び出して辞書に突っ込む
        num1 = len(dictDetail)
        numD1 = 1
        
        numName = 1
        numRoughSymbol =1         
        numDetailNumber = 1
        numTech1 = 1
        numTech2 = 1
        numComment = 1        
        
        dictName = {0: 'dictName'}
        dictRoughSymbol = {0: 'dictRoughSymbol'}         
        dictDetailNumber = {0: 'dictDetailNumber'}
        dictTech1 = {0: 'dictTech1'}
        dictTech2 = {0: 'dictTech2'}
        dictComment = {0: 'dictComment'}

        for i in range(num1):
            if dictDetail[i].startswith('name_') == True:
                dictName[numName] = dictDetail[i]
                numName += 1
                
            elif dictDetail[i].startswith('rough_') == True: 
                dictRoughSymbol[numRoughSymbol] = dictDetail[i]
                numRoughSymbol += 1
                
            elif dictDetail[i].startswith('detail_') == True:
                dictDetailNumber[numDetailNumber] = dictDetail[i]
                numDetailNumber += 1
                
            elif dictDetail[i].startswith('tech1_') == True:
                dictTech1[numTech1] = dictDetail[i]
                numTech1 += 1
                
            elif dictDetail[i].startswith('tech2_') == True:
                dictTech2[numTech2] = dictDetail[i]
                numTech2 += 1
            
            elif dictDetail[i].startswith('comment_') == True:
                dictComment[numComment] = dictDetail[i]
                numComment += 1
            numD1 += 1        
            
        return dictName, dictRoughSymbol, dictDetailNumber, dictTech1, dictTech2, dictComment

if __name__=='__main__':
    rt = ReadText()
    ProdName, dictDetail, dictRough = rt.ImportText('workflow\workflow_car_v1.txt')
    #ReadTextのテスト用
    print(ProdName)
    #print(dictDetail)
    #print(dictRough)
    
    dictName, dictRoughSymbol, dictDetailNumber, dictTech1, dictTech2, dictComment = rt.SearchDetail(dictDetail)
       
    print(dictName)
    print(dictRoughSymbol)
    print(dictDetailNumber)
    print(dictTech1)
    print(dictTech2)
    print(dictComment)
    