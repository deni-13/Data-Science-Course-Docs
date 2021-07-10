#%%pandas review


#matplotlib--gorsellestirme
#lineplot scatter bar plot subplot histogram ..
#csv gorsellestirme


import pandas as pd
df =pd.read_csv("iris.csv")


print(df.columns) #kolumn

print(df.Species)

#benzersiz turler
print(df.Species.unique())


print(df.info())

print(df.describe())
#numeric info

setosa=df[df.Species== "Iris-setosa"]
versi=df[df.Species== "Iris-versicolor"]


print(setosa.describe())

print(versi.describe())



#%%line plot

import matplotlib.pyplot as plt
"""
df1=df.drop(["Id"],axis=1)






df1.plot()
plt.show()

"""

setosa=df[df.Species== "Iris-setosa"]
versicolor=df[df.Species== "Iris-versicolor"]
virginica=df[df.Species=="Iris-virginica"]

#ayrı--tek plot

plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="setosa-PedalLengthCm")

plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="blue",label="versicolor-PealLengthCm")
plt.plot(virginica.Id,virginica.PetalLengthCm,color="green",label="virginica-PetalLengthCm")

plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()


#setosa id ve patelelngth label ne cizdiyoruz



#id 0-50 setosa 60-100 versi gerisi virginica



#grid ekleme


df1.plot(grid=True)
plt.show()

#linstyle var ama cok onemli degil
#alpha=0.5 gibi ozwellikler var bunlar cizgi saydamlıgı özelliklerinde



#%%scatter

#karsılastırmalarda kullanılır

setosa=df[df.Species== "Iris-setosa"]
versicolor=df[df.Species== "Iris-versicolor"]
virginica=df[df.Species=="Iris-virginica"]



plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="red",label="setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color="purple",label="versic")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="blue",label="virginica")

plt.xlabel("length")
plt.legend() #onemli
plt.ylabel("Width")
plt.title("scatter plot")
plt.show()




#%%histogram
#kac tane var? 
#setosa da petal lenghtin frekansı??
plt.hist(setosa.PetalLengthCm,bins=20)



plt.xlabel("cm")
plt.ylabel("frekansı")
plt.title("histogram")
plt.show()




#%%bar plot

import numpy as np
c=np.array([1,2,3,5,6,9])
y=c*2+5


plt.bar(c,y)

plt.xlabel("c")
plt.ylabel("y")
plt.title("bar")
plt.show()


#dogru grafigi mantıgı var burda zaten dogru denklemine gore eslesiyor 



#%%subplot

df1.plot(grid=True,alpha=0.9,subplots=True)
plt.show()






#1.column 1si
plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="setosa-PedalLengthCm")

#2.column 2si
plt.subplot(2,1,2)
plt.plot(virginica.Id,virginica.PetalLengthCm,color="green",label="virginica-PetalLengthCm")


plt.show()

#ikisini bir arada gosterdik !

#%% son

import pandas as pd

import numpy as np
"""
dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],

              "AGE":[15,16,17,33,45,66],

              "MAAS": [100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

ortalama_maas = dataFrame1.MAAS.mean()

s = np.sum([True if ortalama_maas > each else False for each in dataFrame1.MAAS])
"""

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],

              "AGE":[15,16,17,33,45,66],

              "MAAS": [100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

dataFrame1.describe()


#%%
import pandas as pd

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],

              "AGE":[15,16,17,33,45,66],

              "MAAS": [100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

dataFrame1.iloc[:,2] 