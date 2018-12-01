#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


import os

os.getcwd()
os.chdir("C:/Users\임상현/Desktop/업무/배출체계/181106_분석배출량/181112")
os.getcwd()
os.listdir(".")


# In[3]:


# step 1 - 파일 불러오기 

#####################################

sc_3=pd.read_csv("sc3.csv",encoding='utf-8')
sc_4=pd.read_csv("sc4.csv",encoding='utf-8')
sc_5=pd.read_csv("sc5.csv",encoding='utf-8')
sc_6=pd.read_csv("sc6.csv",encoding='utf-8')
sc_7=pd.read_csv("sc7.csv",encoding='utf-8')
sc_8=pd.read_csv("sc8.csv",encoding='utf-8')
sc_9=pd.read_csv("sc9.csv",encoding='utf-8')
code_table=pd.read_csv("code_table.csv",encoding='utf-8')

#####################################


# In[4]:


# step 2 특별광역시도 작업 - 특별광역시도에는 scode1 , ccode1 만 필요해서 그것만 사용

#############################################

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
        
        dummy_0=sc_9[ (sc_9.Scode1 == in_Scode_1) & (sc_9.Ccode1==c_code) ]
        
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
    
    print(dummy_list," check ! ")
    print()
    #step_2
    
    dummy_1=[]
    
    c_code=1
    
    while(c_code<5):
        
    # 여기를 건들여 주세요. ##########
    
        dummy_1=sc_9[ (sc_9.Scode1==code_a) & (sc_9.Scode2==code_b) & (sc_9.Ccode1==c_code) ]

    
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

        print(" check 2  =  ",code_a,"  : ",code_b,"  : ",c_code)

        co2.append(int_co2)
        ch4.append(int_ch4)
        n2o.append(int_n2o)
        tot_sum.append(int_sum)
        
        c_code=c_code+1
        
    print("bye",total_b)

    
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
        
    dummy_0=sc_9[ (sc_9.Scode1 == 17) & (sc_9.Ccode1==c_code) ]
        
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
    
###################################


# In[5]:


#step 5  - 갯수 확인 및 데이터형식 list -> DataFrame 치환 
# 치환 후 csv로 output           

real_ar=[]

real_ar.append(co2)
real_ar.append(ch4)
real_ar.append(n2o)
real_ar.append(tot_sum)


print(len(co2),len(ch4),len(n2o),len(tot_sum))


# In[6]:


final_df=pd.DataFrame(real_ar)

# 여기도요

final_df.to_csv("fin_sc9_re.csv")

##################################

