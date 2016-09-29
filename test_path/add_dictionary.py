'''
Created on 2016/09/30

@author: H.Yamato
'''
import os
from collections import Counter

#リファレンス1
#a = {2: 'integer', 'name': 'okada'}
#print(a)
#print(a[2])
#print(a['name'])

#リファレンス2
#a = {'name':'okada', 'value':{3:'ok', 4:'perfect'}}
#print(a['value'[3]])

#インポート確認
print("import_addDic")

#ディレクトリの中身を初期辞書に書き込む
for searchpath, dirs, files in os.walk('tech'):
    dict = {'name':files}
    
    print(dict)
    
    num = 1
    dictImport = {0:'dictImport'}
            
    counter = Counter(dict['name'])
    for word, cnt, in counter.most_common():
        dictImport[num] = word
        num += 1

#テスト用        
print(dictImport)
#print(dict[3])