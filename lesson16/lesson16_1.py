import pandas as pd
import numpy as np


df = pd.DataFrame(np.arange(9).reshape((3, 3)),
                  index=['a', 'b', 'c'],
                  columns=['TPE', 'TCH', 'KAO']);
##print(df);

df4 = pd.DataFrame(np.arange(16).reshape((4, 4)),
                  index=["a", "b", "c", "d"],
                  columns=["i", "j", "k", "l"]);

df5 = df4.drop(index=["b", "c"]);

print(df4);
print(df5);