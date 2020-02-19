

import sys, KT_UI
import PyQt5
import pandas as pd
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox


class WindowClass(QDialog , KT_UI.Ui_Dialog ):
    
    global data
    global data_3
    global kt_1
    global kt_2
    
    global code_table
    global sc_exe
    
    
    code_table=pd.read_csv("code_table.csv",encoding='utf-8')
    
    
    def __init__(self) :
        
        QDialog.__init__(self, None)
        self.setupUi(self)
        
        self.pushButton_4.clicked.connect( self.data_input )
        self.pushButton_1.clicked.connect( self.output_1 )
        self.pushButton_2.clicked.connect( self.output_2 )
        self.pushButton_3.clicked.connect( self.output_3 )
        
        self.pushButton_5.clicked.connect( self.sinario_input )
        self.pushButton_6.clicked.connect( self.sinario_output )
        
############################################################################
        
    def data_input(self):
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            print(' Born to be yours ')
            
        
        dummy = fileName.split('/')
        path = dummy[0]
        for i in range( 1 , len(dummy) - 1 ):
            path = path + '/' + dummy[i]
        
        #print(path)
        
        os.chdir(path)
        print('dir : ',os.getcwd() )
        print('file name : ' , fileName )
        
        global data
        data = pd.read_csv( fileName , delimiter = '\t', header = None ,encoding = 'latin-1' )
        
        
    def output_1(self):
        
        global data
        global data_3
        
        data_2 = data.iloc[ 1: , :]

        data_3 = data_2.iloc[ : , [12,11,1,0,0,2,4,7,22,23]]
        
        data_3.columns = ['Scode1','Scode2','Bcode','Ccode1','Ccode2','Fcode','Ocode','Wcode','Lcode','Mcode']
        data_3['Lcode']=data_3['Lcode'].astype(float)
        data_3['Mcode']=data_3['Mcode'].astype(float)
        data_3['Scode1']=data_3['Scode1'].astype(int)
        data_3['Scode2']=data_3['Scode2'].astype(int)
        data_3['Bcode']=data_3['Bcode'].astype(int)
        data_3['Ccode1']=data_3['Ccode1'].astype(int)
        data_3['Ccode2']=data_3['Ccode2'].astype(int)
        data_3['Fcode']=data_3['Fcode'].astype(int)
        data_3['Ocode']=data_3['Ocode'].astype(int)
        data_3['Wcode']=data_3['Wcode'].astype(int)
        data_3['LMcode']=data_3['Lcode']*data_3['Mcode']
        
        data_3.to_csv('kt_trans1_1.txt')
        
        QMessageBox.about(self , 'pop up' , 'work is done !')
        
        
    def output_2(self):
        
        global data_3
        global kt_1
        global kt_2
        
        Scode1=[]
        real_Scode1=[]
                
        Scode2=[]
        real_Scode2=[]
                
        Bcode=[]
        real_Bcode=[]
                
        Ccode1=[]
        real_Ccode1=[]
                
        Ccode2=[]
        real_Ccode2=[]
                
        Fcode=[]
        real_Fcode=[]
                
        Ocode=[]
        real_Ocode=[]
                
        Wcode=[]
        real_Wcode=[]
                
        Scode1=list(data_3['Scode1'])
        Scode2=list(data_3['Scode2'])
        Bcode=list(data_3['Bcode'])
        Ccode1=list(data_3['Ccode1'])
        Ccode2=list(data_3['Ccode2'])
        Fcode=list(data_3['Fcode'])
        Ocode=list(data_3['Ocode'])
        Wcode=list(data_3['Wcode'])
                
        real_Lcode=[]
        real_Mcode=[]
        real_LMcode=[]
                
        Lcode=list(data_3['Lcode'])
        Mcode=list(data_3['Mcode'])
        LMcode=list(data_3['LMcode'])
        
               
        count_1=0
                
        while count_1< len(data_3):
                    
            a1=Scode1[count_1]
            a1=self.invert_Scode_1(a1)
            real_Scode1.append(a1)
                    
            a2=Scode2[count_1]
            a2=self.invert_Scode_2(a2)
            real_Scode2.append(a2)
                    
            a3=Bcode[count_1]
            a3=self.invert_Bcode(a3)
            real_Bcode.append(a3)
                    
            a4=Ccode1[count_1]
            a4=self.invert_Ccode_1(a4)
            real_Ccode1.append(a4)
                    
            a5=Ccode2[count_1]
            a5=self.invert_Ccode_2(a5)    
            real_Ccode2.append(a5)
                    
            a6=Fcode[count_1]
            a6=self.invert_Fcode(a6)
            real_Fcode.append(a6)
                    
            a7=Ocode[count_1]
            a7=self.invert_Ocode(a7)
            real_Ocode.append(a7)
                    
            a8=Wcode[count_1]
            a8=self.invert_Wcode(a8)
            real_Wcode.append(a8)
                    
                    
            L=Lcode[count_1]
            real_Lcode.append(L)
                    
            M=Mcode[count_1]
            real_Mcode.append(M)
                    
            LM=LMcode[count_1]
            real_LMcode.append(LM)
                    
                    
            count_1=count_1+1
                    
            if count_1%1000000==0:
                print(count_1)
        
        print('step 1 over ')
        
                
        Ncode=[]
        new_Ncode=[]
                
        count_1=0
                
        
        while count_1< len(data_3):
                    
            ncode1=str(real_Scode2[count_1])
            ncode2=str(real_Bcode[count_1])
            ncode3=str(real_Ccode1[count_1])
            ncode4=str(real_Ccode2[count_1])
            ncode5=str(real_Fcode[count_1])
                    
            fin_ncode=ncode1+ncode2+ncode3+ncode4+ncode5
                    
            new_ncode1=str(real_Scode2[count_1])
            new_ncode2=str(real_Bcode[count_1])
            new_ncode3=str(real_Ccode1[count_1])
            new_ncode4=str(real_Ccode2[count_1])
            new_ncode5=str(real_Fcode[count_1])
            new_ncode6=str(real_Ocode[count_1])
                    
            fin_new_ncode=new_ncode1+new_ncode2+new_ncode3+new_ncode4+new_ncode5+new_ncode6
                    
            Ncode.append(fin_ncode)
            new_Ncode.append(fin_new_ncode)
                    
            count_1=count_1+1
                    
            if count_1%1000000==0:
                print(count_1)
                
        print('Step 2 Over ! ')
                
                
        fin_1=[Ncode,real_Scode1,real_Scode2,real_Bcode,real_Ccode1,real_Ccode2,real_Fcode,real_Ocode,real_Wcode,real_Lcode,real_Mcode,real_LMcode]
        fin_2=[new_Ncode,real_Scode1,real_Scode2,real_Bcode,real_Ccode1,real_Ccode2,real_Fcode,real_Ocode,real_Wcode,real_Lcode,real_Mcode,real_LMcode]
                
        kt_1=pd.DataFrame(fin_1)
        kt_1=kt_1.T
        kt_1.columns=['Ncode','Scode1','Scode2','Bcode','Ccode1','Ccode2','Fcode','Ocode','Wcode','Lcode','Mcode','LMcode']
        kt_2=pd.DataFrame(fin_2)
        kt_2=kt_2.T
        kt_2.columns=['Ncode','Scode1','Scode2','Bcode','Ccode1','Ccode2','Fcode','Ocode','Wcode','Lcode','Mcode','LMcode']
                
        kt_1.to_csv("kt_trans1_2_A.txt")
        kt_2.to_csv("kt_trans1_2_B.txt")
        
        QMessageBox.about(self , 'pop up' , 'work is done !')
        
    def output_3(self):
        
        global kt_1
        global kt_2
        
        test_1=kt_1.groupby('Ncode')
        df_test_1=pd.DataFrame({'count':test_1.size(),'Lcode_sum':test_1['Lcode'].sum(),'Mcode_sum':test_1['Mcode'].sum(),'LMcode_sum':test_1['LMcode'].sum()})
        df_test_1['Lcode_avg']=df_test_1['Lcode_sum']/df_test_1['count']
        df_test_1['Mcode_avg']=df_test_1['Mcode_sum']/df_test_1['count']
        df_test_1['LMcode_avg']=df_test_1['LMcode_sum']/df_test_1['count']
                
        del df_test_1['Lcode_sum']
        del df_test_1['Mcode_sum']
        del df_test_1['LMcode_sum']
                
        test_2=kt_2.groupby('Ncode')
        df_test_2=pd.DataFrame({'count':test_2.size(),'Lcode_sum':test_2['Lcode'].sum(),'Mcode_sum':test_2['Mcode'].sum(),'LMcode_sum':test_2['LMcode'].sum()})
        df_test_2['Lcode_avg']=df_test_2['Lcode_sum']/df_test_2['count']
        df_test_2['Mcode_avg']=df_test_2['Mcode_sum']/df_test_2['count']
        df_test_2['LMcode_avg']=df_test_2['LMcode_sum']/df_test_2['count']
                
        del df_test_2['Lcode_sum']
        del df_test_2['Mcode_sum']
        del df_test_2['LMcode_sum']
                
        df_test_1.to_csv('kt_trans2_A.txt')
        df_test_2.to_csv('kt_trans2_B.txt')
                
        QMessageBox.about(self , 'pop up' , 'work is done !')
                
        
    def invert_Scode_1(self, num):
       
        if num >=1 and num <= 25 : return 1
        
        elif num >= 26 and num <= 41:
            return 2
        
        elif num >= 42 and num <= 49:
            return 3
        
        elif num >= 50 and num <= 59:
            return 4
        
        elif num >= 60 and num <= 64:
            return 5
        
        elif num >= 65 and num <= 69:
            return 6
        
        elif num >= 70 and num <= 74:
            return 7
        
        elif num == 75  :
            return 8
    
        elif num >= 76 and num <= 106 :
            return 9
    
        elif num >= 107 and num <= 124 :
            return 10
        
        elif num >= 125 and num <= 135 :
            return 11
        
        elif num >= 136 and num <= 150 :
            return 12
        
        elif num >= 151 and num <= 164 :
            return 13
        
        elif num >= 165 and num <= 186 :
            return 14
        
        elif num >= 187 and num <= 209 :
            return 15
        
        elif num >= 210 and num <= 227 :
            return 16
        
        elif num >= 228 and num <= 229 :
            return 17
        
    def invert_Scode_2(self, num):
       
        if num ==1 : return 100
        elif num ==2: return 101
        elif num ==3: return 102
        elif num ==4: return 103
        elif num ==5: return 104
        elif num ==6: return 105
        elif num ==7: return 106
        elif num ==8: return 107
        elif num ==9: return 108
        elif num ==10: return 109
        elif num ==11: return 110
        elif num ==12: return 111
        elif num ==13: return 112
        elif num ==14: return 113
        elif num ==15: return 114
        elif num ==16: return 115
        elif num ==17: return 116
        elif num ==18: return 117
        elif num ==19: return 118
        elif num ==20: return 119
        elif num ==21: return 120
        elif num ==22: return 121
        elif num ==23: return 122
        elif num ==24: return 123
        elif num ==25: return 124
        elif num ==26: return 130
        elif num ==27: return 131
        elif num ==28: return 132
        elif num ==29: return 133
        elif num ==30: return 134
        elif num ==31: return 135
        elif num ==32: return 136
        elif num ==33: return 137
        elif num ==34: return 138
        elif num ==35: return 139
        elif num ==36: return 140
        elif num ==37: return 141
        elif num ==38: return 142
        elif num ==39: return 143
        elif num ==40: return 144
        elif num ==41: return 145
        elif num ==42: return 150
        elif num ==43: return 151
        elif num ==44: return 152
        elif num ==45: return 153
        elif num ==46: return 154
        elif num ==47: return 155
        elif num ==48: return 156
        elif num ==49: return 157
        elif num ==50: return 161
        elif num ==51: return 162
        elif num ==52: return 163
        elif num ==53: return 164
        elif num ==54: return 165
        elif num ==55: return 166
        elif num ==56: return 167
        elif num ==57: return 168
        elif num ==58: return 169
        elif num ==59: return 170
        elif num ==60: return 175
        elif num ==61: return 176
        elif num ==62: return 177
        elif num ==63: return 178
        elif num ==64: return 179
        elif num ==65: return 183
        elif num ==66: return 184
        elif num ==67: return 185
        elif num ==68: return 186
        elif num ==69: return 187
        elif num ==70: return 192
        elif num ==71: return 193
        elif num ==72: return 194
        elif num ==73: return 195
        elif num ==74: return 196
        elif num ==75: return 301
        elif num ==76: return 200
        elif num ==76: return 200
        elif num ==76: return 200
        elif num ==76: return 200
        elif num ==77: return 204
        elif num ==77: return 204
        elif num ==77: return 204
        elif num ==78: return 207
        elif num ==79: return 208
        elif num ==79: return 208
        elif num ==80: return 210
        elif num ==81: return 213
        elif num ==82: return 214
        elif num ==83: return 215
        elif num ==84: return 216
        elif num ==84: return 216
        elif num ==85: return 218
        elif num ==85: return 218
        elif num ==85: return 218
        elif num ==86: return 220
        elif num ==87: return 221
        elif num ==88: return 222
        elif num ==89: return 223
        elif num ==90: return 224
        elif num ==91: return 225
        elif num ==92: return 226
        elif num ==93: return 227
        elif num ==94: return 228
        elif num ==94: return 228
        elif num ==94: return 228
        elif num ==95: return 229
        elif num ==96: return 230
        elif num ==97: return 231
        elif num ==98: return 232
        elif num ==99: return 233
        elif num ==100: return 234
        elif num ==101: return 235
        elif num ==102: return 236
        elif num ==103: return 237
        elif num ==104: return 238
        elif num ==105: return 239
        elif num ==106: return 240
        elif num ==107: return 250
        elif num ==108: return 251
        elif num ==109: return 252
        elif num ==110: return 253
        elif num ==111: return 254
        elif num ==112: return 255
        elif num ==113: return 256
        elif num ==114: return 257
        elif num ==115: return 258
        elif num ==116: return 259
        elif num ==117: return 260
        elif num ==118: return 261
        elif num ==119: return 262
        elif num ==120: return 263
        elif num ==121: return 264
        elif num ==122: return 265
        elif num ==123: return 266
        elif num ==124: return 267
        elif num ==125: return 270
        elif num ==125: return 270
        elif num ==125: return 270
        elif num ==125: return 270
        elif num ==126: return 272
        elif num ==127: return 273
        elif num ==125: return 270
        elif num ==128: return 275
        elif num ==129: return 276
        elif num ==130: return 277
        elif num ==131: return 278
        elif num ==132: return 279
        elif num ==133: return 280
        elif num ==134: return 281
        elif num ==135: return 282
        elif num ==136: return 285
        elif num ==136: return 285
        elif num ==137: return 286
        elif num ==138: return 287
        elif num ==139: return 288
        elif num ==140: return 289
        elif num ==141: return 290
        elif num ==142: return 291
        elif num ==143: return 300
        elif num ==144: return 292
        elif num ==145: return 294
        elif num ==146: return 295
        elif num ==147: return 296
        elif num ==148: return 297
        elif num ==149: return 298
        elif num ==150: return 299
        elif num ==151: return 305
        elif num ==151: return 305
        elif num ==152: return 307
        elif num ==153: return 308
        elif num ==154: return 309
        elif num ==155: return 310
        elif num ==156: return 311
        elif num ==157: return 312
        elif num ==158: return 313
        elif num ==159: return 314
        elif num ==160: return 315
        elif num ==161: return 316
        elif num ==162: return 317
        elif num ==163: return 318
        elif num ==164: return 319
        elif num ==165: return 324
        elif num ==166: return 325
        elif num ==167: return 326
        elif num ==168: return 327
        elif num ==169: return 328
        elif num ==170: return 329
        elif num ==171: return 330
        elif num ==172: return 331
        elif num ==173: return 332
        elif num ==174: return 333
        elif num ==175: return 334
        elif num ==176: return 335
        elif num ==177: return 336
        elif num ==178: return 337
        elif num ==179: return 338
        elif num ==180: return 339
        elif num ==181: return 340
        elif num ==182: return 341
        elif num ==183: return 342
        elif num ==184: return 343
        elif num ==185: return 344
        elif num ==186: return 345
        elif num ==187: return 350
        elif num ==187: return 350
        elif num ==188: return 352
        elif num ==189: return 353
        elif num ==190: return 354
        elif num ==191: return 355
        elif num ==192: return 356
        elif num ==193: return 357
        elif num ==194: return 358
        elif num ==195: return 359
        elif num ==196: return 360
        elif num ==197: return 361
        elif num ==198: return 362
        elif num ==199: return 363
        elif num ==200: return 364
        elif num ==201: return 365
        elif num ==202: return 366
        elif num ==203: return 367
        elif num ==204: return 368
        elif num ==205: return 369
        elif num ==206: return 370
        elif num ==207: return 371
        elif num ==208: return 372
        elif num ==209: return 373
        elif num ==210: return 379
        elif num ==210: return 379
        elif num ==210: return 379
        elif num ==210: return 379
        elif num ==210: return 379
        elif num ==211: return 381
        elif num ==212: return 383
        elif num ==213: return 384
        elif num ==214: return 385
        elif num ==215: return 386
        elif num ==216: return 387
        elif num ==217: return 388
        elif num ==218: return 389
        elif num ==219: return 390
        elif num ==220: return 391
        elif num ==221: return 392
        elif num ==222: return 393
        elif num ==223: return 394
        elif num ==224: return 395
        elif num ==225: return 396
        elif num ==226: return 397
        elif num ==227: return 398
        elif num ==228: return 405
        elif num ==229: return 405
    
    
    def invert_Bcode(self, num) :
        
        if num == 1 : return 1
        elif num == 2 : return 2
        elif num == 3 : return 3
        elif num == 4 : return 3
        
    def invert_Ccode_1(self, num) :  # Ccode1
        
        if num >=1 and num <= 16 : return 1
        
        elif num >= 17 and num <= 24:
            return 2
        
        elif num >= 25 and num <= 53 :
            return 3
        
        elif num >= 54 and num <= 65 :
            return 4
    
        
    def invert_Ccode_2(self, num) :  # Ccode2
        
        if num == 1 : return 1
        elif num ==2: return 2
        elif num ==3: return 3
        elif num ==4: return 4
        elif num ==5: return 1
        elif num ==6: return 2
        elif num ==7: return 3
        elif num ==8: return 4
        elif num ==9: return 1
        elif num ==10: return 2
        elif num ==11: return 3
        elif num ==12: return 4
        elif num ==13: return 1
        elif num ==14: return 2
        elif num ==15: return 3
        elif num ==16: return 4
        elif num ==17: return 1
        elif num ==18: return 2
        elif num ==19: return 3
        elif num ==20: return 4
        elif num ==21: return 1
        elif num ==22: return 2
        elif num ==23: return 3
        elif num ==23: return 3
        elif num ==24: return 4
        elif num ==25: return 1
        elif num ==25: return 1
        elif num ==25: return 1
        elif num ==26: return 2
        elif num ==26: return 2
        elif num ==26: return 2
        elif num ==27: return 3
        elif num ==27: return 3
        elif num ==27: return 3
        elif num ==28: return 4
        elif num ==28: return 4
        elif num ==28: return 4
        elif num ==29: return 1
        elif num ==30: return 2
        elif num ==31: return 3
        elif num ==32: return 4
        elif num ==33: return 1
        elif num ==34: return 2
        elif num ==35: return 3
        elif num ==36: return 4
        elif num ==37: return 1
        elif num ==37: return 1
        elif num ==38: return 2
        elif num ==38: return 2
        elif num ==39: return 3
        elif num ==39: return 3
        elif num ==40: return 4
        elif num ==40: return 4
        elif num ==41: return 1
        elif num ==41: return 1
        elif num ==42: return 2
        elif num ==42: return 2
        elif num ==43: return 3
        elif num ==43: return 3
        elif num ==44: return 4
        elif num ==44: return 4
        elif num ==45: return 1
        elif num ==46: return 2
        elif num ==47: return 3
        elif num ==48: return 4
        elif num ==49: return 4
        elif num ==50: return 4
        elif num ==51: return 4
        elif num ==52: return 4
        elif num ==52: return 4
        elif num ==53: return 4
        elif num ==54: return 1
        elif num ==55: return 2
        elif num ==56: return 3
        elif num ==57: return 4
        elif num ==58: return 1
        elif num ==59: return 2
        elif num ==60: return 3
        elif num ==61: return 4
        elif num ==62: return 1
        elif num ==63: return 2
        elif num ==63: return 2
        elif num ==64: return 3
        elif num ==65: return 4
    
        
    def invert_Fcode(self, num) :
        
        if num >=1 and num <= 3 : return 1
        
        elif num == 4 :
            return 2
        
        elif num == 5 :
            return 3
        
        elif num >= 6 and num <= 7:
            return 4
    
        elif num >= 8 and num <= 12:
            return 5
    
        elif num >= 13 and num <= 15:
            return 6
        
        elif num >= 16 and num <= 17:
            return 7
    
        
    def invert_Ocode(self, num) :
        
        if num >=2015 and num <= 2018 : return 1
        
        elif num >=2010 and num <= 2014 :
            return 2
        
        elif num >=2005 and num <= 2009 :
            return 3
        
        elif num >= 1934 and num <= 2004:
            return 4
        
        
    def invert_Wcode(self, num) :
        
        if num >=1000 and num <= 1200 : return 1
        
        else :
            return 2
    

##########################################################################
            
        
    def sinario_input(self):
        
        global sc_exe
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            print(' Born to be yours ')
            
        
        dummy = fileName.split('/')
        path = dummy[0]
        for i in range( 1 , len(dummy) - 1 ):
            path = path + '/' + dummy[i]
        
        #print(path)
        
        os.chdir(path)
        print('dir : ',os.getcwd() )
        print('file name : ' , fileName )
        
        sc_exe=pd.read_csv(fileName ,encoding='utf-8')
        
    def sinario_output(self):
        
        global sc_exe
        
        total_a=0
        total_b=1

        co2=[]
        ch4=[]
        n2o=[]
        tot_sum=[]

        in_Scode_1=1


        while(in_Scode_1<9):

            dummy_0=[]
            c_code=1

            while(c_code<5):

                # 변경 !  #############

                dummy_0=sc_exe[ (sc_exe.Scode1 == in_Scode_1) & (sc_exe.Ccode1==c_code) ]

                med_co2=[]
                med_ch4=[]
                med_n2o=[]
                med_tot_sum=[]

                int_co2=0
                int_ch4=0
                int_n2o=0
                int_sum=0

                float(int_co2)
                float(int_ch4)
                float(int_n2o)
                float(int_sum)


                med_co2=dummy_0.EMI_CO2
                med_ch4=dummy_0.EMI_CH4
                med_n2o=dummy_0.EMI_N2O
                med_tot_sum=dummy_0.EMI_CO2eq

                int_co2=med_co2.sum()
                int_ch4=med_ch4.sum()
                int_n2o=med_n2o.sum()
                int_sum=med_tot_sum.sum()

                co2.append(int_co2)
                ch4.append(int_ch4)
                n2o.append(int_n2o)
                tot_sum.append(int_sum)

                c_code=c_code+1

            in_Scode_1=in_Scode_1+1

        ##########################################

        # step 3 - 일반시도 작업 - scode1 , scode2 , ccode1 사용

        #######################################
        while(total_b<153):

            code_a=0
            code_b=0
            #step_1

            dummy_list=[]
            dummy_list=code_table[ total_a : total_b ]

            dummy_list.iloc[0,1]
            code_a=dummy_list.iloc[0,2]
            code_b=dummy_list.iloc[0,1]
            int(code_a)
            int(code_b)

            #step_2

            dummy_1=[]

            c_code=1

            while(c_code<5):

            # 여기를 건들여 주세요. ##########

                dummy_1=sc_exe[ (sc_exe.Scode1==code_a) & (sc_exe.Scode2==code_b) & (sc_exe.Ccode1==c_code) ]


                #step_3

                med_co2=[]
                med_ch4=[]
                med_n2o=[]
                med_tot_sum=[]

                int_co2=0
                int_ch4=0
                int_n2o=0
                int_sum=0

                float(int_co2)
                float(int_ch4)
                float(int_n2o)
                float(int_sum)


                med_co2=dummy_1.EMI_CO2
                med_ch4=dummy_1.EMI_CH4
                med_n2o=dummy_1.EMI_N2O
                med_tot_sum=dummy_1.EMI_CO2eq

                int_co2=med_co2.sum()
                int_ch4=med_ch4.sum()
                int_n2o=med_n2o.sum()
                int_sum=med_tot_sum.sum()

                co2.append(int_co2)
                ch4.append(int_ch4)
                n2o.append(int_n2o)
                tot_sum.append(int_sum)

                c_code=c_code+1


            #print(code_table[a:b])
            total_a=total_a+1
            total_b=total_b+1

        #############################################    


        # step 4 - 제주도 용도

        ###############################
            # 제주도 용

        c_code=1
        while(c_code<5):

                ########### 여기도 염 #######

            dummy_0=sc_exe[ (sc_exe.Scode1 == 17) & (sc_exe.Ccode1==c_code) ]

            med_co2=[]
            med_ch4=[]
            med_n2o=[]
            med_tot_sum=[]

            int_co2=0
            int_ch4=0
            int_n2o=0
            int_sum=0

            float(int_co2)
            float(int_ch4)
            float(int_n2o)
            float(int_sum)


            med_co2=dummy_0.EMI_CO2
            med_ch4=dummy_0.EMI_CH4
            med_n2o=dummy_0.EMI_N2O
            med_tot_sum=dummy_0.EMI_CO2eq

            int_co2=med_co2.sum()
            int_ch4=med_ch4.sum()
            int_n2o=med_n2o.sum()
            int_sum=med_tot_sum.sum()

            co2.append(int_co2)
            ch4.append(int_ch4)
            n2o.append(int_n2o)
            tot_sum.append(int_sum)

            c_code=c_code+1

        #step 5  - 갯수 확인 및 데이터형식 list -> DataFrame 치환 
        # 치환 후 csv로 output           

        real_ar=[]

        real_ar.append(co2)
        real_ar.append(ch4)
        real_ar.append(n2o)
        real_ar.append(tot_sum)


        print(len(co2),len(ch4),len(n2o),len(tot_sum))

        final_df=pd.DataFrame(real_ar)
        final_df=final_df.T

        # 여기도요

        final_df.to_csv('output.csv')
        
        QMessageBox.about(self , 'pop up' , 'work is done !')
        
    
#######################################################################################
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()