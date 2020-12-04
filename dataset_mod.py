import os
import pandas as pd
import numpy as np

print('Imported Libraries')
combined_csv = pd.read_csv('./dataset/combined_1_csv.csv')
print('OLD Shape : '+str(combined_csv.shape))

combined_csv.drop(columns=['Timestamp'],inplace=True)
print('Dropping Timestamp Done')

combined_csv.replace([np.inf, -np.inf], np.nan,inplace=True)
print('Replacing Inf Done')

combined_csv.dropna(axis=0,how="any",inplace=True)
print('Dropping NaN Done')

# combined_csv = combined_csv.rename(columns={'ACK Flag Cnt' : 'ack_fl_cnt'})
# print('Renaming')
# combined_csv = combined_csv[combined_csv.ack_fl_cnt !='ACK Flag Cnt']
# print(df2.shape)
print('NEW Shape : '+ str(combined_csv.shape))
combined_csv.to_csv( "combined_v2_csv.csv", index=False, encoding='utf-8-sig')
print('Dataset Saved as V2')