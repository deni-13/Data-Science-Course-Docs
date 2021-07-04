# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 20:19:05 2021

@author: deno
"""
#%%
#init constructor 


class Isci():
    
    oran=1.2 #clas var
    def __init__(self,isim,soyad,maas):
        self.isim=isim
        self.soyad=soyad
        self.maas=maas
        
    def givenameSurname(self):
        return self.isim+""+self.soyad
        
    def zam(self):
        self.maas=self.maas*self.oran
        
        
isci1=Isci("ali","veli",3500)
print(isci1.maas)
         
#self bu calısanı insaa ederkenki ki
#ismi alıyor


print(isci1.givenameSurname())

#class calısan
#init construtor isim soy isim maas 
#self class variableina tanımlama 
#give name surname --> metod


#class variables
isci2=Isci("john","kerry",600)
print(isci2.maas)


isci2.zam()
print("2.iscinin maası--->",isci2.maas)


#example

isci3=Isci("kate","johnson",8000)
isci4=Isci("daniel","taylor",7400)

liste=[isci1,isci2,isci3,isci4]

maxi=-1


for i in liste:
    if i.maas>maxi:
        maxi=i.maas
    else:
        continue
    
print(maxi)
print(i.givenameSurname())

#%%
#errors
#1-syntax error
#print(9) -->print 9

#1-try -except
#type error düzelttik
"""a=17
b=2
liste=[1,2,4,68]
print(sum(liste))
print(a+b)
"""
k=8
zero=0
d=k/zero

if zero==0:
    d=0
else:
    d=k/zero
    
    
try:
    d=k/zero
except:
    d=0

#dene eger cıkmazsa 0 bas

#%%
#index error

liste1=[1,2,4,6,57,4]
#liste1[15]--->error tabikide 
#module not found ---> import kdhdıg ama bole bise yok
#file not found---> asc.csv yok bole bi dosya
#type error str+int 


try:
    1/0
except:
    print("except")
finally:
    print("bitti")
    
    #finally hep basılcak
    
    
    
    #%%
   """ s = "fffggg"
    s[::-2]

    print(int(51.88+4/5))
   """ 
l = [lambda x:x**2, lambda x:x+2,lambda x:x*2]

for i in l:

    print(i(5))
    
a = {1:"A",2:"B"}

for i,j in a.items():

    print(i,j,end = "-")
    
    #%%
    
   class DataiTeam:

   

    def __init__(self, x = "hi"):

        self.x = x



    def show(self):

        print(self.x)



my_class = DataiTeam()

my_class.show()




