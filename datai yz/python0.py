# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:00:59 2021

@author: deno
"""
#%%
#variable
#fnc
#objects

var="pazartesi"

var1=10
var2=3

#%%
#%%
s="bugun pzt"
a= type(s)
print(s)
 #%%
# numbers
a= 5.3

 
 #%%
 #built in func
 """
a=8.4
round(a)
"""
#user defined
def ilkfunc(var1,var2):
    
  out=var1*var2/6
  return out

#%%

#default and flexible func

# def cember(r,pi=3.14):
#     out=2*pi*r
    
#     return out
  
    
#flexible kısmı args ile ilgili

#%%
#ornek
yas=10
name="ali"
soy="veli"


def funct(yas,name,*args,ayakk=36):
    print(yas,name,ayakk)

    print(float(yas))
    
    
    out=args[0]*yas
    
    return out
 
son = funct(yas,name,soy)

print("args[0]*yas",son)

#args0 soyada denk geliyor


#%%
#lambda

def hesap(x):
    a=x*x
    
    return a
#lambdalı kullanım 

sonuc = lambda x:x*x
print(sonuc(4))







