import numpy as np
import pandas as pd

np.random.seed(678);
df = pd.DataFrame(np.random.randn(10, 4),columns=['A', 'B', 'C', 'D']);

def style_negative(v,props=''):
    return props if v < 0 else None

df1 = df.style.map(style_negative, props="color:red");

print(type(df1.to_html()));
##df.style.map(style_negative, props="color:red",subset=['A']);
##df.style.map(style_negative, props="color:red",subset=['A','C']);
##df.style.map(style_negative, props="color:red",subset=(slice(0,4)))\
##.map(lambda v: 'opacity:20%' if (v<0.3) and (v>-0.3) else None);

