import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.axis import Axis
import numpy as np

data = pd.read_csv('2022_02_08-02_30_31_AM.csv')
# Ques1
print(data['price_string'].isnull().sum())
#Ques2
data['CategoryWithoutPrices'] = data.price_string.isnull().groupby([data['category']]).transform('sum').astype(str,errors='ignore')
data['CategoryWithPrices'] = data.price_string.notnull().groupby([data['category']]).transform('sum').astype(str,errors='ignore')
data['Level1WithoutPrices'] = data.price_string.isnull().groupby([data['level_1']]).transform('sum').astype(str,errors='ignore')
data['Level1WithPrices'] = data.price_string.notnull().groupby([data['level_1']]).transform('sum').astype(str,errors='ignore')
data['ProductTypeWithoutPrices'] = data.price_string.isnull().groupby([data['product_type']]).transform('sum').astype(str,errors='ignore')
data['ProductTypeWithPrices'] = data.price_string.notnull().groupby([data['product_type']]).transform('sum').astype(str,errors='ignore')
CPW = data.groupby(['category','CategoryWithoutPrices'])['category','CategoryWithoutPrices'].groups
CP = data.groupby(['category','CategoryWithPrices'])['category','CategoryWithPrices'].groups
LPW = data.groupby(['level_1','Level1WithoutPrices'])['level_1','Level1WithoutPrices'].groups
LP = data.groupby(['level_1','Level1WithPrices'])['level_1','Level1WithPrices'].groups
PPW = data.groupby(['product_type','ProductTypeWithoutPrices'])['product_type','ProductTypeWithoutPrices'].groups
PP = data.groupby(['product_type','ProductTypeWithPrices'])['product_type','ProductTypeWithPrices'].groups

arr1 = []
arr2 = []
arr3 = []
arr4 = []
for i in CPW.keys():
  arr1.append(i[0])
  arr2.append(i[1])
for i in CP.keys():
  arr4.append(i[0])
  arr3.append(i[1])
plt.plot(arr2,arr1,label ="Price empty")
plt.plot(arr3,arr4,label = "Price Not Empty")
plt.legend()
plt.savefig("On the basis of category")
plt.show()
fig, ax = plt.subplots() 
ax.plot(arr2,arr1,color='green', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='yellow', markersize=12,label ="Price empty")
ax.plot(arr3,arr4,color='red', linestyle='dashed', linewidth = 3,marker='x', markerfacecolor='blue', markersize=12,label = "Price Not Empty")  
ax.legend()
ax.xaxis.zoom(4)
ax.grid() 
fig.suptitle("""On the Basis of Category \n""", fontweight ="bold")
plt.savefig("On the basis of category Zoomed")
plt.show() 
arr1 = []
arr2 = []
arr3 = []
arr4 = []
for i in LPW.keys():
  arr1.append(i[0])
  arr2.append(i[1])
for i in LP.keys():
  arr4.append(i[0])
  arr3.append(i[1])
plt.plot(arr2,arr1,label ="Price empty")
plt.plot(arr3,arr4,label = "Price Not Empty")
plt.legend()
plt.savefig("On the basis of level_1")
plt.show()
fig, ax = plt.subplots() 
ax.plot(arr2,arr1,color='green', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='yellow', markersize=12,label ="Price empty")
ax.plot(arr3,arr4,color='red', linestyle='dashed', linewidth = 3,marker='x', markerfacecolor='blue', markersize=12,label = "Price Not Empty")  
ax.legend()
ax.margins(x=0, y=-0.25)
fig.suptitle("""On the Basis of Level 1 \n""", fontweight ="bold")
plt.savefig("On the basis of level_1 zoomed")
plt.show() 
arr1 = []
arr2 = []
arr3 = []
arr4 = []
for i in PPW.keys():
  arr1.append(i[0])
  arr2.append(i[1])
for i in PP.keys():
  arr4.append(i[0])
  arr3.append(i[1])
plt.plot(arr2,arr1,label ="Price empty")
plt.plot(arr3,arr4,label = "Price Not Empty")
plt.legend()
plt.savefig("On the basis of product_type")
plt.show()
fig, ax = plt.subplots() 
ax.plot(arr2,arr1,color='green', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='yellow', markersize=12,label ="Price empty")
ax.plot(arr3,arr4,color='red', linestyle='dashed', linewidth = 3,marker='x', markerfacecolor='blue', markersize=12,label = "Price Not Empty")  
ax.legend()
ax.margins(x=0, y=-0.25)
ax.grid() 
fig.suptitle("""On the Basis of Product type \n""", fontweight ="bold")
plt.savefig("On the basis of product_type zoomed") 
plt.show()
#Ques 3
data['price_string'] = data['price_string'].replace(np.nan, 0)
data['value'] = data["price_string"].replace("[$,]", "", regex=True).astype(float,errors='ignore')
data['price_string'] = data['price_string'].replace(0, np.nan)
data['currency'] = '$'