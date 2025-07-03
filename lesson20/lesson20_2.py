import numpy as np
import pandas as pd

df = pd.DataFrame({'key1':['a', 'a', 'b', 'b', 'a'],
                  'key2':['one', 'two', 'one', 'two', 'one'],
                  'data1': np.random.randn(5),
                  'data2':np.random.randn(5)});

df_group = df.groupby(by="key1")[["data1", "data2"]].sum();
print(df_group);



df1 = df.groupby(by=['key1','key2']).agg([("sum", "sum"), ("avg", "mean")]);
print(df1);
