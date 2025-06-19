import numpy as np
import pandas as pd

score_length = 30;
score = np.random.randint(50, 101, size=(score_length, 5));

score_pd = pd.DataFrame(score,
    columns = ["CN", "EN", "MAT", "SCI", "GEO"],
    index = [f"stu{i}" for i in range(1, score_length+1)]
);

score_pd.columns.name = "subject";
score_pd.index.name = "ID";

sum = np.sum(score_pd, axis=1);
avg = np.mean(score_pd, axis=1);
score_pd["SUM"] = sum;
score_pd["AVG"] = avg;

for i in range(1, 4):
    score_pd.to_excel(f"class3_{i}.xlsx", index=True); 