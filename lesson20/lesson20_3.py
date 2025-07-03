
import numpy as np
import pandas as pd 

#美國球賽門票收入
tips_df = pd.read_csv('./data/tips.csv');
tips_df.columns = ['price', 'fee', 'smoker', 'day', 'time', 'size'];


tips_df['fee ratio'] = tips_df['fee'] / tips_df['price'];
grouped = tips_df.groupby(by=['day','smoker']);
grouped['fee'].agg([('avg fee','mean'),('sum','sum')]);

def peak_to_peak(arr):
    return arr.max() - arr.min()

grouped = tips_df.groupby(by=['day','smoker'])
tips_df2 = grouped['fee'].agg([('avg fee','mean'),('sum','sum'),('stddev','std'),('max min diff',peak_to_peak)]);

grouped = tips_df.groupby(by=['smoker','day'])
functions = [('cnt','count'),('avg','mean'),('max','max')]
tips_df3 = grouped[['fee','price']].agg(functions)
print(tips_df3['fee'][['cnt','avg']])


