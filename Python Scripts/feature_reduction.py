import pandas as pd
import numpy as np


print('Importing Done')
c_df = pd.read_csv('./dataset/combined_v3_csv.csv')
print('OLD Shape : '+ str(c_df.shape))

string_col = 'Dst Port, Flow Duration, Tot Fwd Pkts, TotLen Fwd Pkts, Fwd Pkt Len Max, Fwd Pkt Len Min, Fwd Pkt Len Mean, Fwd Pkt Len Std, Bwd Pkt Len Max, Flow Byts/s, Flow Pkts/s, Flow IAT Mean, Flow IAT Std, Flow IAT Max, Flow IAT Min, Fwd IAT Mean, Fwd IAT Std, Fwd IAT Min, Bwd IAT Tot, Bwd IAT Mean, Bwd IAT Std, Bwd IAT Max, Fwd Header Len, Bwd Header Len, Bwd Pkts/s, Pkt Len Min, Pkt Len Mean, Pkt Len Var, PSH Flag Cnt, ACK Flag Cnt, Down/Up Ratio, Init Fwd Win Byts, Init Bwd Win Byts, Fwd Act Data Pkts, Fwd Seg Size Min, Active Min'
list_of_col = string_col.split(', ')
list_of_col.append('Label')
print('------ LIST of Columns to keep ------')
print(list_of_col)
print('------- End of List ------')

print(len(list_of_col))
c_df = c_df.loc[:,list_of_col]

print('NEW Shape : '+ str(c_df.shape))
c_df.to_csv( "combined_v4_csv.csv", index=False, encoding='utf-8-sig')
print('DataSet Saved v4')