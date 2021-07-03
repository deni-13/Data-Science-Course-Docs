# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 21:37:31 2021

@author: deno
"""
#%%
lls=["pzr","salı","car"]
type(lls)

last=lls[-1]

listdiv=lls[0:2]
f=lls.append("per")

#tuple
a=(1,2,455,332,11,2)

v=a.count(1)
#%% #dict
dicti={"ali":34,"john":80}
d=dicti.keys()

#%% #cond

i=[9,34,1,35,734,3]

if 1 in i:
    print("evet")
    #%%
 #quiz2
 #1690 yılı 17.yy
 #2000-->20.yy
 #300 3.yy yy donduren fonk
 
 
 # 1640. yil == 17. yuzyil
# 109. yil == 2. yuzyil
# 2000. yil = 20. yuzyil
    
# metod yazin.
    # input integer yillar
    # output integer yuzyil

# input = year  >> 1 <= year <= 2005
    
def year2Century(year):
    """
    year to century
    """
    str_year = str(year)
    
    if(len(str_year)<3):
        return 1
    elif(len(str_year) == 3):
        if(str_year[1:3] == "00"):  # 100 ,200 300, 400 ... 900
            return int(str_year[0])
        else:                       # 190, 250, 450
            return int(str_year[0])+1
    else:                           # 1750, 1700, 1805
        if(str_year[2:4]=="00"):    # 1700, 1900, 1100
            return int(str_year[:2])
        else:                       # 1705, 1645, 1258
            return int(str_year[:2])+1

year2Century(1800)



#%%
#for

for each in range(1,10):
    print(each)

count=0
a=[1,2,3,4,54]

for i in a:
    count+=i
    print(count)

#%%
#while loop

i=0
while i<4:
    print(i)
    i+=1
    
#%% quiz3

#listenin içindeki en kücük sayı bul

liste=[122,4,3,563,32,72,2]

mini=1000 #keyword fonk old için deistirdik mini yazdık 

for i in liste:

    if i<mini :
        mini=i
        
    else:
       continue
        
print(mini)
        
    
    




   