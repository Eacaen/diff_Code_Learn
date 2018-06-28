import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

sns.set()

Correlation = pd.DataFrame(train_data[['Embarked', 'Sex','Fare', 'Pclass', 'Age', 'Cabin']])

plt.figure( )
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(Correlation.corr(),linewidths=0.1,vmax=1.0, square=True\
	, cmap='YlGnBu', linecolor='white', annot=True)
plt.show()