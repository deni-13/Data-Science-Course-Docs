# -*- coding: utf-8 -*-

#Pandas 
#pandas hızlı ve etkili
#csv ve txt için çok efaktif
#missing data için kolay
#reshape icin data etkili 
#slicing 
#time series data zamanla gelen data depolanabilir.
#%%
import pandas as pd

dicti={"Name":["John","Casey","James","Elliot","Bella"],
      "Age":[40,16,34,45,12],
      "Salary":[3455,540,9000,5490,0]}

dataframe1=pd.DataFrame(dicti)

head=dataframe1.head()
tail=dataframe1.tail()
#%%basic methods

#sutun isimleri 
print(dataframe1.columns)
#sadece yasa ve maasa gore filtrelemede ise yarıyor

print(dataframe1.info())#bilgi 

print(dataframe1.dtypes)#type yazdırma



print(dataframe1.describe())#sadece numerik feature alıyor
#std ort vb var burda

#%% indexing slicing 

print(dataframe1["Name"]) #columndan 

print(dataframe1["Age"])
print(dataframe1.Age)  #aynı sekilde alabildik


#feature ekleme

dataframe1["Job"]=["mechanicalengineer","student","banker","programmer","student"]


print(dataframe1.Job)

#LOC 
print(dataframe1.loc[:,"Age"])
#tıum satır istedigm sutun

#index sonu dahil pandasta

print(dataframe1.loc[:,"Age":"Job"])


print(dataframe1.loc[:3,["Age","Name"]])
#3.indexe kadar yazdır 

print(dataframe1.loc[::-1,["Age","Name"]])
#ters yazdık 



print(dataframe1.loc[:,:"Age"])
#age dahil e kadar yaz


print(dataframe1.iloc[:,2])
#sutun olarak indexi iki olanı yazıdr
#maas'ı bastık

#%% filtering data frame
#Boolean seri yaratmak amaç
#veriyi filtre etmek df icinde

filt=dataframe1.Salary>2000
#☻pandas seri dtype'i
filtData=dataframe1[filt]


filt2=dataframe1.Age<20


dataframe1[filt&filt2]
#iki filtre birlesti



k=dataframe1[dataframe1.Age>40]
#elliot


#%%list comp
#liste icerisinde if else dongusu kuruyor



#ort maas
ort=dataframe1.Salary.mean()

dataframe1["maas_seviyesi"] = ["dusuk" if ort > each else "yuksek" for each in dataframe1.Salary]


for each in dataframe1.Salary:
    if ort>each:
        print("DUSUK")
    else:
        print("YUKSEK")




#%%drop & concataneting data



dataframe1.drop(["Salary"],axis=1,inplace=True)
#axis1  sutun drop

#concataneting
#vstack gibi nump'De

dq=dataframe1.head()
dq1=dataframe1.tail()


dconc=pd.concat([dq,dq1],axis=0)

#vertical



#%%transforming data

#yas*2

dataframe1["list_comp"] = [ each*2 for each in dataframe1.Age]

# apply()

def multiply(Age):
    return Age*2
    
dataframe1["apply_metodu"] = dataframe1.Age.apply(multiply)


