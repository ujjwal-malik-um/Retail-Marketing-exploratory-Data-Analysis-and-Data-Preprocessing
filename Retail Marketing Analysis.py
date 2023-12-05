import numpy as np
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt

df = pd.read_csv('marketing_data.csv')

df.head(5)
df.info()
df.describe()

#check for and handle missing values
df.isnull().sum()/len(df)*100
df=df.dropna(inplace=True)

#handle special variables
df[' Income '] = df[' Income '].str.replace('$','').str.replace(',','')

#find age
df['Age'] = df['Year_Birth'].apply(lambda x: 2022-x)

#find total amount spent on products
df['Total_amount_spent'] = np.sum(df.filter(regex='Mnt'), axis=1)

#find total purchases made
df['TotalPurchases'] = np.sum(df.filter(regex='Purchases'),axis=1)

#visualize which campaign is most successful
cmp = df.filter(regex='Cmp').sum()
plt.pie(cmp,autopct='%0.2f',labels=cmp.index,explode=[0,0.2,0,0,0])
plt.show()

#Visualize (Bar Chart) the distribution of the age with respect to customers who accepted the last campaign
customers_accepted = df[df['Response']==1]
sns.displot(customers_accepted['Age'])
plt.show()

#Visualize (Box Plot) the distribution of Total amount spent Vs Dependents. (Dependents=['Kidhome']+['Teenhome'])
df["Dependents"] = df["Kidhome"] + df["Teenhome"]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
sns.boxplot(y=df["Total_amount_spent"],x=df["Dependents"])
plt.subplot(1,2,2)
sns.boxplot(y=df["TotalPurchases"],x=df["Dependents"])
plt.show()

#Perform Correlation Analysis (Heat Map)
dff = df.drop('ID',axis=1)
plt.figure(figsize=[18,7])
sns.heatmap(dff.corr(),annot=True,cmap='viridis')
plt.show()
