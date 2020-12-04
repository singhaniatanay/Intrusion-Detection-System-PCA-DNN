import pandas as pd
import numpy as np

print('Importing Done')
c_df = pd.read_csv('./dataset/combined_v2_csv.csv')
print('OLD Shape : '+ str(c_df.shape))

for i in c_df.columns:
    print(i)
    if i=='Label':
        continue
    c_df = c_df[c_df[i].apply(type)!=type('abc')]
    print(c_df.shape)
    break

print('NEW Shape : '+ str(c_df.shape))
c_df.to_csv( "combined_v3_csv.csv", index=False, encoding='utf-8-sig')
print('DataSet Saved v3')