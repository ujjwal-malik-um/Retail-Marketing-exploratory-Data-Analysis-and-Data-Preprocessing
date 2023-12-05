import numpy as np
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('marketing_data.csv')
df.head(5)
df.info()
df.describe()
df.isna().sum()
df=df.dropna()
import re
if(bool(re.match('^[a-zA-Z0-9]*$',o))==True):
    print("valid")
else:
    print("invalid")
#create our dictionary, shopping items as keys and price of items as values
shoppingDict = {"Apple":40.00,"Banana":30.00,"Fish":100.00,"Bread":45.00,"Milk":20.00}
#iterate through the dictionaries items printing them out in a certain format
for k,v in shoppingDict.items():print(f'{k}: Php {v}')
while True:
    #prompt user to enter an item
    choice=input('\nChoose an item: Apple, Banana, Fish, Bread, Milk\n')
    #check if that item is found in the dictionary
    #if so add the key's value(price) to price
    try:price += shoppingDict.get(choice)
    #if the user does not enter a valid item, we will print error
    except KeyError:print('Error')
    #ask them if they want to play again
    if input('Would you like to go again? y/n') == 'n':
        print(f'Total Cost: {price}')
        break
from scipy.stats.stats import pearsonr
#calculation correlation coefficient and p-value between x and y
pearsonr(x, y)
import seaborn
import matplotlib.pyplot as plt
############# Main Section ############
# loading dataset using seaborn
# pairplot with hue sex
seaborn.pairplot(df, hue='Response')
# to show
plt.show()
seaborn.pairplot(df, hue='Education')
# to show
plt.show()
seaborn.pairplot(df, hue='Marital Status')
# to show
plt.show()
