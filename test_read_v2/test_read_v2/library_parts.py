'''
Created on 2016/09/30

@author: H.Yamato
'''
from read_text import *

print('import library_parts')

class Library():
    def __init__(self):
        self.numR = 1
        self.RNm = {}
        self.RTc1 = {}
        self.RTc2 = {}
        self.RCt1 = {}
        self.RCt2 = {}
        #ラフパーツ
        self.Rp1 = {}
        self.Rp2 = {}
        self.Rp3 = {}
        self.Rp4 = {}
        self.Rp5 = {}
        self.Rp6 = {}
        self.Rp7 = {}
        self.Rp8 = {}
        
        self.numD = 1
        self.DNm = {}
        self.DRh = {}
        self.DTc1 = {}
        self.DTc2 = {}
        self.DCt1 = {}
        self.DCt2 = {}
        #ディティールパーツ
        self.Dp1 = {}
        self.Dp2 = {}
        self.Dp3 = {}
        self.Dp4 = {}
        self.Dp5 = {}
        self.Dp6 = {}
        self.Dp7 = {}
        self.Dp8 = {}
        
        self.numF = 1
        self.FNm = {}
        self.FCt1 = {}
        self.FCt2 = {}
        #フィックスパーツ
        self.Fp1 = {}
        self.Fp2 = {}
        self.Fp3 = {}
        self.Fp4 = {}
        self.Fp5 = {}
        self.Fp6 = {}
        self.Fp7 = {}
        self.Fp8 = {}
        
        self.pMother = {}

    def filingRoughDatas(self, layer1):
        #読み込んだ辞書からネームだけを選び出して辞書に突っ込む
        num1 = len(layer1)
        num2 = 1
        numRTc1 = 1
        numRTc2 = 1
        numRCt1 = 1
        numRCt2 = 1
        
        for i in range(num1):
            if layer1[i + 1].startswith('name_') == True:
                self.RNm[self.numR] = layer1[i + 1]
                self.numR += 1
            elif layer1[i + 1].startswith('tech1_') == True:
                self.RTc1[numRTc1] = layer1[i + 1]
                numRTc1 += 1
            elif layer1[i + 1].startswith('tech2_') == True:
                self.RTc2[numRTc2] = layer1[i + 1]
                numRTc2 += 1
            elif layer1[i + 1].startswith('comment1_') == True:
                self.RCt1[numRCt1] = layer1[i + 1]
                numRCt1 += 1
            elif layer1[i + 1].startswith('comment2_') == True:
                self.RCt2[numRCt2] = layer1[i + 1]
                numRCt2 += 1
            num2 += 1
        self.numR -= 1
        return self.numR, self.RNm, self.RTc1, self.RTc2, self.RCt1, self.RCt2
    
    def filingDetailDatas(self, layer2):
        #読み込んだ辞書からネームだけを選び出して辞書に突っ込む
        num1 = len(layer2)
        num2 = 1
        numDRh = 1
        numDTc1 = 1
        numDTc2 = 1
        numDCt1 = 1
        numDCt2 = 1
        
        for i in range(num1):
            if layer2[i + 1].startswith('name_') == True:
                self.DNm[self.numD] = layer2[i + 1]
                self.numD += 1
            elif layer2[i + 1].startswith('rough_') == True:
                self.DRh[numDRh] = layer2[i + 1]
                numDRh += 1
            elif layer2[i + 1].startswith('tech1_') == True:
                self.DTc1[numDTc1] = layer2[i + 1]
                numDTc1 += 1
            elif layer2[i + 1].startswith('tech2_') == True:
                self.DTc2[numDTc2] = layer2[i + 1]
                numDTc2 += 1
            elif layer2[i + 1].startswith('comment1_') == True:
                self.DCt1[numDCt1] = layer2[i + 1]
                numDCt1 += 1
            elif layer2[i + 1].startswith('comment2_') == True:
                self.DCt2[numDCt2] = layer2[i + 1]
                numDCt2 += 1
            num2 += 1
        self.numD -= 1
        return self.numD, self.DNm, self.DRh, self.DTc1, self.DTc2, self.DCt1, self.DCt2

    def filingFixDatas(self, layer3):
        #読み込んだ辞書からネームだけを選び出して辞書に突っ込む
        num1 = len(layer3)
        num2 = 1
        numFTc1 = 1
        numFTc2 = 1
        numFCt1 = 1
        numFCt2 = 1
        
        for i in range(num1):
            if layer3[i + 1].startswith('name_') == True:
                self.FNm[self.numF] = layer3[i + 1]
                self.numF += 1
            elif layer3[i + 1].startswith('comment1_') == True:
                self.FCt1[numFCt1] = layer3[i + 1]
                numFCt1 += 1
            elif layer3[i + 1].startswith('comment2_') == True:
                self.FCt2[numFCt2] = layer3[i + 1]
                numFCt2 += 1
            num2 += 1
        self.numF -= 1
        return self.numF, self.FNm, self.FCt1, self.FCt2

    def filingRoughParts(self):
        if self.numR >= 1:
            self.Rp1['name'] = str(self.RNm[1]).lstrip('name_')
            self.Rp1['tech1'] = str(self.RTc1[1]).lstrip('tech1_')
            self.Rp1['tech2'] = str(self.RTc2[1]).lstrip('tech2_')
            self.Rp1['comment1'] = str(self.RCt1[1]).lstrip('cooment1_')
            self.Rp1['comment2'] = str(self.RCt2[1]).lstrip('comment2_')
        if self.numR >= 2:
            self.Rp2['name'] = str(self.RNm[2]).lstrip('name_')
            self.Rp2['tech1'] = str(self.RTc1[2]).lstrip('tech1_')
            self.Rp2['tech2'] = str(self.RTc2[2]).lstrip('tech2_')
            self.Rp2['comment1'] = str(self.RCt1[2]).lstrip('cooment1_')
            self.Rp2['comment2'] = str(self.RCt2[2]).lstrip('comment2_')
        if self.numR >= 3:
            self.Rp3['name'] = str(self.RNm[3]).lstrip('name_')
            self.Rp3['tech1'] = str(self.RTc1[3]).lstrip('tech1_')
            self.Rp3['tech2'] = str(self.RTc2[3]).lstrip('tech2_')
            self.Rp3['comment1'] = str(self.RCt1[3]).lstrip('cooment1_')
            self.Rp3['comment2'] = str(self.RCt2[3]).lstrip('comment2_')
        if self.numR >= 4:
            self.Rp4['name'] = str(self.RNm[4]).lstrip('name_')
            self.Rp4['tech1'] = str(self.RTc1[4]).lstrip('tech1_')
            self.Rp4['tech2'] = str(self.RTc2[4]).lstrip('tech2_')
            self.Rp4['comment1'] = str(self.RCt1[4]).lstrip('cooment1_')
            self.Rp4['comment2'] = str(self.RCt2[4]).lstrip('comment2_')
        if self.numR >= 5:
            self.Rp5['name'] = str(self.RNm[5]).lstrip('name_')
            self.Rp5['tech1'] = str(self.RTc1[5]).lstrip('tech1_')
            self.Rp5['tech2'] = str(self.RTc2[5]).lstrip('tech2_')
            self.Rp5['comment1'] = str(self.RCt1[5]).lstrip('cooment1_')
            self.Rp5['comment2'] = str(self.RCt2[5]).lstrip('comment2_')
        if self.numR >= 6:
            self.Rp6['name'] = str(self.RNm[6]).lstrip('name_')
            self.Rp6['tech1'] = str(self.RTc1[6]).lstrip('tech1_')
            self.Rp6['tech2'] = str(self.RTc2[6]).lstrip('tech2_')
            self.Rp6['comment1'] = str(self.RCt1[6]).lstrip('cooment1_')
            self.Rp6['comment2'] = str(self.RCt2[6]).lstrip('comment2_')
        if self.numR >= 7:
            self.Rp7['name'] = str(self.RNm[7]).lstrip('name_')
            self.Rp7['tech1'] = str(self.RTc1[7]).lstrip('tech1_')
            self.Rp7['tech2'] = str(self.RTc2[7]).lstrip('tech2_')
            self.Rp7['comment1'] = str(self.RCt1[7]).lstrip('cooment1_')
            self.Rp7['comment2'] = str(self.RCt2[7]).lstrip('comment2_')
        if self.numR >= 8:
            self.Rp8['name'] = str(self.RNm[8]).lstrip('name_')
            self.Rp8['tech1'] = str(self.RTc1[8]).lstrip('tech1_')
            self.Rp8['tech2'] = str(self.RTc2[8]).lstrip('tech2_')
            self.Rp8['comment1'] = str(self.RCt1[8]).lstrip('cooment1_')
            self.Rp8['comment2'] = str(self.RCt2[8]).lstrip('comment2_')
        print('辞書への書き込みを終了します (by FilingRoughParts)')
        return self.Rp1, self.Rp2, self.Rp3, self.Rp4, self.Rp5, self.Rp6, self.Rp7, self.Rp8
    
    def filingDetailParts(self):
        if self.numD >= 1:
            self.Dp1['name'] = str(self.DNm[1]).lstrip('name_')
            self.Dp1['rough'] = str(self.DRh[1]).lstrip('rough_')
            self.Dp1['tech1'] = str(self.DTc1[1]).lstrip('tech1_')
            self.Dp1['tech2'] = str(self.DTc2[1]).lstrip('tech2_')
            self.Dp1['comment1'] = str(self.DCt1[1]).lstrip('comment1_')
            self.Dp1['comment2'] = str(self.DCt2[1]).lstrip('comment2_')
        if self.numD >= 2:
            self.Dp2['name'] = str(self.DNm[2]).lstrip('name_')
            self.Dp2['rough'] = str(self.DRh[2]).lstrip('rough_')
            self.Dp2['tech1'] = str(self.DTc1[2]).lstrip('tech1_')
            self.Dp2['tech2'] = str(self.DTc2[2]).lstrip('tech2_')
            self.Dp2['comment1'] = str(self.DCt1[2]).lstrip('comment1_')
            self.Dp2['comment2'] = str(self.DCt2[2]).lstrip('comment2_')
        if self.numD >= 3:
            self.Dp3['name'] = str(self.DNm[3]).lstrip('name_')
            self.Dp3['rough'] = str(self.DRh[3]).lstrip('rough_')
            self.Dp3['tech1'] = str(self.DTc1[3]).lstrip('tech1_')
            self.Dp3['tech2'] = str(self.DTc2[3]).lstrip('tech2_')
            self.Dp3['comment1'] = str(self.DCt1[3]).lstrip('comment1_')
            self.Dp3['comment2'] = str(self.DCt2[3]).lstrip('comment2_')
        if self.numD >= 1:
            self.Dp4['name'] = str(self.DNm[4]).lstrip('name_')
            self.Dp4['rough'] = str(self.DRh[4]).lstrip('rough_')
            self.Dp4['tech1'] = str(self.DTc1[4]).lstrip('tech1_')
            self.Dp4['tech2'] = str(self.DTc2[4]).lstrip('tech2_')
            self.Dp4['comment1'] = str(self.DCt1[4]).lstrip('comment1_')
            self.Dp4['comment2'] = str(self.DCt2[4]).lstrip('comment2_')
        if self.numD >= 1:
            self.Dp5['name'] = str(self.DNm[5]).lstrip('name_')
            self.Dp5['rough'] = str(self.DRh[5]).lstrip('rough_')
            self.Dp5['tech1'] = str(self.DTc1[5]).lstrip('tech1_')
            self.Dp5['tech2'] = str(self.DTc2[5]).lstrip('tech2_')
            self.Dp5['comment1'] = str(self.DCt1[5]).lstrip('comment1_')
            self.Dp5['comment2'] = str(self.DCt2[5]).lstrip('comment2_')
        if self.numD >= 1:
            self.Dp6['name'] = str(self.DNm[6]).lstrip('name_')
            self.Dp6['rough'] = str(self.DRh[6]).lstrip('rough_')
            self.Dp6['tech1'] = str(self.DTc1[6]).lstrip('tech1_')
            self.Dp6['tech2'] = str(self.DTc2[6]).lstrip('tech2_')
            self.Dp6['comment1'] = str(self.DCt1[6]).lstrip('comment1_')
            self.Dp6['comment2'] = str(self.DCt2[6]).lstrip('comment2_')
        if self.numD >= 1:
            self.Dp7['name'] = str(self.DNm[7]).lstrip('name_')
            self.Dp7['rough'] = str(self.DRh[7]).lstrip('rough_')
            self.Dp7['tech1'] = str(self.DTc1[7]).lstrip('tech1_')
            self.Dp7['tech2'] = str(self.DTc2[7]).lstrip('tech2_')
            self.Dp7['comment1'] = str(self.DCt1[7]).lstrip('comment1_')
            self.Dp7['comment2'] = str(self.DCt2[7]).lstrip('comment2_')
        if self.numD >= 1:
            self.Dp8['name'] = str(self.DNm[8]).lstrip('name_')
            self.Dp8['rough'] = str(self.DRh[8]).lstrip('rough_')
            self.Dp8['tech1'] = str(self.DTc1[8]).lstrip('tech1_')
            self.Dp8['tech2'] = str(self.DTc2[8]).lstrip('tech2_')
            self.Dp8['comment1'] = str(self.DCt1[8]).lstrip('comment1_')
            self.Dp8['comment2'] = str(self.DCt2[8]).lstrip('comment2_')

        print('辞書への書き込みを終了します (by FilingDetailParts)')
        return self.Dp1, self.Dp2, self.Dp3, self.Dp4, self.Dp5, self.Dp6, self.Dp7, self.Dp8
    
    def filingFixParts(self):
        if self.numF >= 1:
            self.Fp1['name'] = str(self.FNm[1]).lstrip('name_')
            self.Fp1['comment1'] = str(self.FCt1[1]).lstrip('comment1_')
            self.Fp1['comment2'] = str(self.FCt2[1]).lstrip('comment2_')
        if self.numF >= 2:
            self.Fp2['name'] = str(self.FNm[2]).lstrip('name_')
            self.Fp2['comment1'] = str(self.FCt1[2]).lstrip('comment1_')
            self.Fp2['comment2'] = str(self.FCt2[2]).lstrip('comment2_')
        if self.numF >= 3:
            self.Fp3['name'] = str(self.FNm[3]).lstrip('name_')
            self.Fp3['comment1'] = str(self.FCt1[3]).lstrip('comment1_')
            self.Fp3['comment2'] = str(self.FCt2[3]).lstrip('comment2_')
        if self.numF >= 4:
            self.Fp4['name'] = str(self.FNm[4]).lstrip('name_')
            self.Fp4['comment1'] = str(self.FCt1[4]).lstrip('comment1_')
            self.Fp4['comment2'] = str(self.FCt2[4]).lstrip('comment2_')
        if self.numF >= 5:
            self.Fp5['name'] = str(self.FNm[5]).lstrip('name_')
            self.Fp5['comment1'] = str(self.FCt1[5]).lstrip('comment1_')
            self.Fp5['comment2'] = str(self.FCt2[5]).lstrip('comment2_')
        if self.numF >= 6:
            self.Fp6['name'] = str(self.FNm[6]).lstrip('name_')
            self.Fp6['comment1'] = str(self.FCt1[6]).lstrip('comment1_')
            self.Fp6['comment2'] = str(self.FCt2[6]).lstrip('comment2_')
        if self.numF >= 7:
            self.Fp7['name'] = str(self.FNm[7]).lstrip('name_')
            self.Fp7['comment1'] = str(self.FCt1[7]).lstrip('comment1_')
            self.Fp7['comment2'] = str(self.FCt2[7]).lstrip('comment2_')
        if self.numF >= 8:
            self.Fp8['name'] = str(self.FNm[8]).lstrip('name_')
            self.Fp8['comment1'] = str(self.FCt1[8]).lstrip('comment1_')
            self.Fp8['comment2'] = str(self.FCt2[8]).lstrip('comment2_')
        print('辞書への書き込みを終了します (by FilingFixParts)')
        return self.Fp1, self.Fp2, self.Fp3, self.Fp4, self.Fp5, self.Fp6, self.Fp7, self.Fp8

    def getLb(self, tag, element=0):
        #ラフパーツパーツ数を聞かれた時の返答
        if tag == 'numR':
            if element == 0:
                return self.numR
            else:
                print('これに引数はないです！(by getLb)')
                return None
        
        #ディティールパーツパーツ数を聞かれた時の返答
        if tag == 'numD':
            if element == 0:
                return self.numD
            else:
                print('これに引数はないです！(by getLb)')
                return None
        
        #フィックスパーツパーツ数を聞かれた時の返答
        if tag == 'numF':
            if element == 0:
                return self.numF
            else:
                print('これに引数はないです！(by getLb)')
                return None
        
        #ラフパーツについて聞かれた時の返答
        elif (str(tag).startswith('Rp')) == True:
            numb = 'Rp1Rp2Rp2Rp3Rp3Rp3Rp4Rp4Rp4Rp4Rp5Rp5Rp5Rp5Rp5Rp6Rp6Rp6Rp6Rp6Rp6Rp7Rp7Rp7Rp7Rp7Rp7Rp7Rp8Rp8Rp8Rp8Rp8Rp8Rp8Rp8'.count(str(tag))
            elm = ['name', 'tech1', 'tech2', 'comment1', 'comment2']
            if element == 0:
                if numb <= self.numR:
                    if numb == 1:
                        return self.Rp1
                    elif numb == 2:
                        return self.Rp2
                    elif numb == 3:
                        return self.Rp3
                    elif numb == 4:
                        return self.Rp4
                    elif numb == 5:
                        return self.Rp5
                    elif numb == 6:
                        return self.Rp6
                    elif numb == 7:
                        return self.Rp7
                    elif numb == 8:
                        return self.Rp8
                else:
                    print('そんなパーツないです！(by getLb)')
                    return None
            elif (elm.count(str(element))) != 0:
                if numb <= self.numR:
                    if numb == 1:
                        return self.Rp1[element]
                    elif numb == 2:
                        return self.Rp2[element]
                    elif numb == 3:
                        return self.Rp3[element]
                    elif numb == 4:
                        return self.Rp4[element]
                    elif numb == 5:
                        return self.Rp5[element]
                    elif numb == 6:
                        return self.Rp6[element]
                    elif numb == 7:
                        return self.Rp7[element]
                    elif numb == 8:
                        return self.Rp8[element]
                else:
                    print('そんなにパーツ数は登録されていないです！(by getLb)')
                    return None
            else:
                print('そんな要素パーツにはないです！(by getLb)')
                return None
        
        #ディティールパーツについて聞かれた時の返答
        elif (str(tag).startswith('Dp')) == True:
            numb = 'Dp1 Dp2Dp2 Dp3Dp3Dp3 Dp4Dp4Dp4Dp4 Dp5Dp5Dp5Dp5Dp5 Dp6Dp6Dp6Dp6Dp6Dp6 Dp7Dp7Dp7Dp7Dp7Dp7Dp7 Dp8Dp8Dp8Dp8Dp8Dp8Dp8Dp8'.count(str(tag))
            elm = ['name', 'rough', 'tech1', 'tech2', 'comment1', 'comment2']
            if element == 0:
                if numb <= self.numD:
                    if numb == 1:
                        return self.Dp1
                    elif numb == 2:
                        return self.Dp2
                    elif numb == 3:
                        return self.Dp3
                    elif numb == 4:
                        return self.Dp4
                    elif numb == 5:
                        return self.Dp5
                    elif numb == 6:
                        return self.Dp6
                    elif numb == 7:
                        return self.Dp7
                    elif numb == 8:
                        return self.Dp8
                else:
                    print('そんなパーツないです！(by getLb)')
                    return None
            elif (elm.count(str(element))) != 0:
                if numb <= self.numD:
                    if numb == 1:
                        return self.Dp1[element]
                    elif numb == 2:
                        return self.Dp2[element]
                    elif numb == 3:
                        return self.Dp3[element]
                    elif numb == 4:
                        return self.Dp4[element]
                    elif numb == 5:
                        return self.Dp5[element]
                    elif numb == 6:
                        return self.Dp6[element]
                    elif numb == 7:
                        return self.Dp7[element]
                    elif numb == 8:
                        return self.Dp8[element]
                else:
                    print('そんなにパーツ数は登録されていないです！(by getLb)')
                    return None
            else:
                print('そんな要素パーツにはないです！(by getLb)')
                return None
        
        #フィックスパーツについて聞かれた時の返答
        elif (str(tag).startswith('Fp')) == True:
            numb = 'Fp1 Fp2Fp2 Fp3Fp3Fp3 Fp4Fp4Fp4Fp4 Fp5Fp5Fp5Fp5Fp5 Fp6Fp6Fp6Fp6Fp6Fp6 Fp7Fp7Fp7Fp7Fp7Fp7Fp7 Fp8Fp8Fp8Fp8Fp8Fp8Fp8Fp8'.count(str(tag))
            elm = ['name', 'comment1', 'comment2']
            if element == 0:
                if numb <= self.numF:
                    if numb == 1:
                        return self.Fp1
                    elif numb == 2:
                        return self.Fp2
                    elif numb == 3:
                        return self.Fp3
                    elif numb == 4:
                        return self.Fp4
                    elif numb == 5:
                        return self.Fp5
                    elif numb == 6:
                        return self.Fp6
                    elif numb == 7:
                        return self.Fp7
                    elif numb == 8:
                        return self.Fp8
                else:
                    print('そんなパーツないです！(by getLb)')
                    return None
            elif (elm.count(str(element))) != 0:
                if numb <= self.numF:
                    if numb == 1:
                        return self.Fp1[element]
                    elif numb == 2:
                        return self.Fp2[element]
                    elif numb == 3:
                        return self.Fp3[element]
                    elif numb == 4:
                        return self.Fp4[element]
                    elif numb == 5:
                        return self.Fp5[element]
                    elif numb == 6:
                        return self.Fp6[element]
                    elif numb == 7:
                        return self.Fp7[element]
                    elif numb == 8:
                        return self.Fp8[element]
                else:
                    print('そんなにパーツ数は登録されていないです！(by getLb)')
                    return None
            else:
                print('そんな要素パーツにはないです！(by getLb)')
                return None
        
        
        #ラフパーツの要素について聞かれた時の返答
        elif (str(tag).startswith('R')) == True:
            if element == 0:
                if tag == 'RNm':
                    return self.RNm
                if tag == 'RTc1':
                    return self.RTc1
                if tag == 'RTc2':
                    return self.RTc2
                if tag == 'RCt1':
                    return self.RCt1
                if tag == 'RCt2':
                    return self.RCt2
            elif (0 < element <= self.numR) == True:
                if tag == 'RNm':
                    return self.RNm[element]
                if tag == 'RTc1':
                    return self.RTc1[element]
                if tag == 'RTc2':
                    return self.RTc2[element]
                if tag == 'RCt1':
                    return self.RCt1[element]
                if tag == 'RCt2':
                    return self.RCt2[element]
            else:
                print('そんなにパーツ数ないです!(by getLb)')
                return None
            
        #ディティールパーツの要素について聞かれた時の返答
        elif (str(tag).startswith('D')) == True:
            if element == 0:
                if tag == 'DNm':
                    return self.DNm
                if tag == 'DRh':
                    return self.DRh
                if tag == 'DTc1':
                    return self.DTc1
                if tag == 'DTc2':
                    return self.DTc2
                if tag == 'DCt1':
                    return self.DCt1
                if tag == 'DCt2':
                    return self.DCt2
            elif (0 < element <= self.numD) == True:
                if tag == 'DNm':
                    return self.DNm[element]
                if tag == 'DTc1':
                    return self.DTc1[element]
                if tag == 'DTc2':
                    return self.DTc2[element]
                if tag == 'DCt1':
                    return self.DCt1[element]
                if tag == 'DCt2':
                    return self.DCt2[element]
            else:
                print('そんなにパーツ数ないです!(by getLb)')
                return None
            
        #フィックスパーツの要素について聞かれた時の返答
        elif (str(tag).startswith('F')) == True:
            if element == 0:
                if tag == 'FNm':
                    return self.FNm
                if tag == 'FCt1':
                    return self.FCt1
                if tag == 'FCt2':
                    return self.FCt2
            elif (0 < element <= self.numD) == True:
                if tag == 'FNm':
                    return self.FNm[element]
                if tag == 'FCt1':
                    return self.Ct1[element]
                if tag == 'FCt2':
                    return self.FCt2[element]
            else:
                print('そんなにパーツ数ないです!(by getLb)')
                return None
        else:
            return 'なんか変！'

    def loadingLibrary(self, layer1, layer2, layer3):
        self.filingRoughDatas(layer1)
        self.filingRoughParts()
        self.filingDetailDatas(layer2)
        self.filingDetailParts()
        self.filingFixDatas(layer3)
        self.filingFixParts()

if __name__=='__main__':
    rt = ReadText()
    rt.importText('workflow\workflow_car_v3.txt')

    lib = Library()
    lib.loadingLibrary(rt.getRt('layer1') ,rt.getRt('layer2'), rt.getRt('layer3'))
    
    #print(lib.getLb('numR', 1))
    #print(lib.getLb('numR'))
    
    #print(lib.getLb('RNm'))
    #print(lib.getLb('RNm', 1))
    #print(lib.getLb('RNm', 3))
    
    #print(lib.getLb('Rp1', 'tech1'))
    #print(lib.getLb('Rp1', 'tech'))
    #print(lib.getLb('Rp2'))
    
    #print(lib.getLb('numD'))
    
    #print(lib.getLb('DNm'))
    #print(lib.getLb('DNm', 1))
    #print(lib.getLb('DNm', 3))
    
    #print(lib.getLb('Dp1', 'name'))
    #print(lib.getLb('Dp2', 'name'))
    #print(lib.getLb('Dp8', 'tech1'))
    #print(lib.getLb('Dp1'))
    #print(lib.getLb('Dp8'))

    #print(lib.getLb('FNm'))
    #print(lib.getLb('Fp8'))
    #print(lib.getLb('Fp8', 'name'))
