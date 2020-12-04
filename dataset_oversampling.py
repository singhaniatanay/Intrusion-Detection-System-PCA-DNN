import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE

print('Importing Done')
df2 = pd.read_csv('./dataset/combined_v4_csv.csv')
print('OLD Shape : '+ str(df2.shape))
Y = df2.loc[:,'Label']
X = df2.drop(columns=['Label'])
print('Data Brokedown to X and Y')
X = X.astype('float64')
print('As type done')

sm = SMOTE('minority')
print('SMOTE Initialized')
print(X.shape)
print(Y.shape)


X_rs, Y_rs = sm.fit_sample(X, Y)
print('Over-Sampling Done')
print(X_rs.shape)
print(Y_rs.shape)
X_rs.to_csv('X_resampled.csv', index=False, encoding='utf-8-sig')
Y_rs.to_csv( "Y_resampled.csv", index=False, encoding='utf-8-sig')
print('Dataset Saved')