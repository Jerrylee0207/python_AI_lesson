import numpy as np

score_length = 50;
score = np.random.randint(50, 101, size=(score_length, 5));
score_sum = np.sum(score, axis=1);
score_avg = np.mean(score, axis=1);


for i in range(0, score_length):
    print(f"student{i:3d}, {score[i, :]}, sum:{score_sum[i]:3d}, avg:{score_avg[i]}");

print(np.where(score_avg>=60, 1, 0));
