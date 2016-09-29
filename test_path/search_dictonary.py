'''
Created on 2016/09/30

@author: H.Yamato
'''
import add_dictionary as addDict

#初期辞書に任意の検索をかけて、合致するものの辞書を作る
num = len(addDict.dictImport)
print(num)

dictSearch = {0:'dictSearch'}

for i in range(num):
    search = addDict.dictImport[i].startswith('image_01')
    
    if search == True:
        dictSearch[i] = addDict.dictImport[i]
        
print(dictSearch)
