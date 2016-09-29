'''
Created on 2016/09/29

@author: H.Yamato
'''
#パス確認
import os
#from collections import Counter

print('import search_text!')

#パスチェック用
#print(os.getcwd())

class SearchText():
    def ImportText(self):
        f = open('workflow\workflow_car.txt', 'r')
        lines1 = f.readlines()
        f.close
        
        num = 1
        dictImport = {0: 'dictImport'}
        for line in lines1:
            #テスト用
            #print(line)
            
            dictImport[num] = line
            num += 1
        #テスト用
        #print(dictImport)
        return dictImport
        
    def SearchType(self, dictImport):
        #読み込んだ辞書からタイプだけを選び出して辞書に突っ込む
        dictType = {0: "dictType"}
        num2 = len(dictImport)
        numN1 = 1
        
        for i in range(num2):
            search = dictImport[i].startswith('type_')    
            if search == True:
                dictType[numN1] = dictImport[i]
                numN1 += 1
        #テスト用
        #print(dictType)
        return dictType
        
    def SearchName(self, dictImport):
        #読み込んだ辞書からネームだけを選び出して辞書に突っ込む
        dictName = {0: "dictName"}
        num2 = len(dictImport)
        numN2 = 1
        
        for i in range(num2):
            search = dictImport[i].startswith('name_')    
            if search == True:
                dictName[numN2] = dictImport[i]
                numN2 += 1
        #テスト用
        #print(dictName)
        return dictName
        
    def NumberType(self, dictType):
        numType = len(dictType) - 1
        return numType
        
    def NumberName(self, dictName):
        numName = len(dictName) - 1
        return numName
    
#このモジュール単体でのテスト用
if __name__ == '__main__':    
    st = SearchText()
    
    a = st.ImportText()
    b = st.SearchType(a)
    c = st.NumberType(b)
    
    print(a)
    print(b)
    print(c)
    
    