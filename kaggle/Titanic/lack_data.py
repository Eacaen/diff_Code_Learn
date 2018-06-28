import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from xgboost import XGBClassifier

import warnings
warnings.filterwarnings('ignore')

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

train_data.info()
print("-" * 40)
test_data.info()

# train_data['Survived'].value_counts().plot.pie(autopct = '%1.2f%%')
# plt.show()

train_data.Embarked[train_data.Embarked.isnull()] = train_data.Embarked.dropna().mode().values

pc = train_data.loc[(train_data['Pclass'] == 1)]
print(pc)