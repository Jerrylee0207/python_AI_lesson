import numpy as np
import pandas as pd
'''
data = pd.Series(np.random.randn(9),
                index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                       [1, 2, 3, 1, 2, 3, 1, 2, 3]]);
data.index.names = ('key1','key2');
print(data);
print(data.unstack(level='key1'));
'''

df = pd.DataFrame(np.arange(12).reshape((4,3)),
                  index=[['a','a','b','b'],[1, 2, 1, 2]],
                  columns=[['TPE','TPE','TCH'],['Green','Red','Green']])
df.index.names=['key1','key2']
df.columns.names = ['city',"color"]
print(df);

df1 = df.stack(level=['city',"color"],future_stack=True)
print(df1)

df2 = df1.unstack(level=['key1','city','key2'],fill_value=0)
print(df2);