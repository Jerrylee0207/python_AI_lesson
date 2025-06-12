import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

score_length = 50;
score = np.random.randint(50, 101, size=(score_length, 5));

df = pd.DataFrame(score,
    columns = ["CN", "EN", "GEO", "CUL", "WEA"],
    index = [f"stu{i}" for i in range(0, score_length)]
);

##print(df);

name01 = df.loc["stu1"].name;
name02 = df.loc["stu2"].name;

figure = plt.figure(figsize=(8, 5), dpi=150, facecolor="#FFFFFF");
axes = figure.add_subplot(1, 1, 1);
axes.plot(df.columns, df.loc["stu1"], marker="o", label="stu01");
axes.plot(df.columns, df.loc["stu2"], marker="o", label="stu02", linestyle="-.");
axes.legend();
axes.set_title("students' score");

x_coor = axes.get_xticks();
for i in range(len(x_coor)):
    x = x_coor[i];
    stu1_y = df.loc["stu1"][i];
    stu2_y = df.loc["stu2"][i];
    axes.annotate(str(stu1_y), (x-0.05, stu1_y+1));
    axes.annotate(str(stu2_y), (x-0.05, stu2_y+1));

axes.set_xlim(-0.5, 4.5);
axes.set_ylim(20, 105);
axes.grid(axis='y', color="#777777", alpha=0.1);
plt.show();