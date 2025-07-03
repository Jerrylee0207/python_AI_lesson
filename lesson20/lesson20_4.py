import numpy as np
import pandas as pd 

#美國球賽門票收入
tips_df = pd.read_csv('./data/tips.csv');
tips_df.columns = ['price', 'fee', 'smoker', 'day', 'time', 'size'];
tips_df['fee ratio'] = tips_df['fee']/tips_df['price'];

def top(df,n=5,column='fee ratio'):
    return df.sort_values(by=column)[-n:]


print(tips_df.groupby(by='smoker').apply(top,include_groups=False));
print(tips_df.groupby(by=['smoker','day']).apply(top,n=1,column='price',include_groups=False));
