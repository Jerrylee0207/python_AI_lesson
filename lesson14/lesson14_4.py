import numpy as np
import pandas as pd

score_length = 50;
score = np.random.randint(50, 101, size=(score_length, 5));

df = pd.DataFrame(score,
    columns = ["CN", "EN", "GEO", "CUL", "WEA"],
    index = [f"stu{i}" for i in range(0, score_length)]
);

##print(df.loc[["stu10", "stu20", "stu30"]]);
sum = df["CN"]+df["EN"]+df["GEO"]+df["CUL"]+df["WEA"];
df["sum"] = sum;
df["avg"] = sum/5;
print(df.iloc[10:15, 5]);