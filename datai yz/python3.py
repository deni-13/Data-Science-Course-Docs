# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 21:13:38 2021

@author: deno
"""
#%%
#Numpy
#basics1

import numpy as np
array=np.array([1,2,3,45]) #burda array
print(array.shape) #4 boyutlu metodu printle bastık

s=array.reshape(2,2)
g=array.ndim #boyut
d=array.size #reshape oncesi boyut

h=np.array([[1,2,3],[13,6,8],[13,64,3]])



np.zeros((3,4))

#append mem'i yorar 0 ları allocate edip güncelleme

k=np.ones((4,4))

y=np.arange(15,30,5)
t=np.linspace(0,13,7)
#%% basics 2
o=np.array([1,2,4,6])
m=np.array([3,25,2,5])

print(o+m)
print(np.sin(o)) #o'nun sin
print(m<2) #2den kucuk mu?


o=np.array([1,2,4,6])
m=np.array([3,25,2,5])
print(o*m) #carpma



#o.dot(p)boyutları carpımı aynı olcak oyuzden olmaz
#%%
r=np.random.random((5,5))

t=r.sum()
print(t) #toplamı
print(r.max())

#columnları topla

print(r.sum(axis=0))

#rowları topla

print(r.sum(axis=1))

g=np.square((r)) 
#karesi

#%%
a = np.array([[1,2,3],[4,5,6]])

b = np.array([[1,2,3],[4,5,6]])

j=a.dot(b.T)


#indexing and slicing
t=np.array([1,2,3,4,5,6,7])

print(t[1])
print(t[0:4]) #slicing
reverse_array=t[::-1] #ters cevr
print(reverse_array)

#bunlar tek boyutlu


#2 boyutlu

u=np.array([[1,2,4,5],[7,3,11,34]])

#4 alalım 0 2
print(u[0][2])
#2 45 3 11 34
print(u[1,1:3])
#%%
#shape manip.

p=np.array([[1,2,3],[4,5,6],[44,35,2]])

#flatten

a=p.ravel() #vektor
a2=a.reshape(3,3)
a3=a2.T #tranpose

#resize - reshape farkı

a3=np.array([[2,43],[64,69],[43,456]])
s=a3.reshape(2,3)
#resize de degisken kullanmaya gerek yok direk kayıt
#ikiside aynı isi yapıyor
#%%
#stacking arrays

arr=np.array([[2,4],[35,6]])
arr1=np.array([[23,47],[32,0]])

#ikisini brilestir vertical veya horiz.


arr2=np.vstack((arr,arr1))

arr3=np.hstack((arr,arr1))

