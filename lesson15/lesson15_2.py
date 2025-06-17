import numpy as np
import pandas as pd

score_length = 10;
score = np.random.randint(50, 101, size=(score_length, 5));

df = pd.DataFrame(score,
    columns = ["CN", "EN", "MAT", "SCI", "GEO"],
    index = [f"stu{i}" for i in range(1, score_length+1)]
);

sum = np.sum(df, axis=1);
avg = np.mean(df, axis=1);
df["SUM"] = sum;
df["AVG"] = avg;
print(df);

print(df[(df["CN"]>=60)&(df["EN"]>=60)]);

'''
s1 = pd.Series(np.arange(51,71));
mask = s1>=60;
print(s1[mask]);
'''
