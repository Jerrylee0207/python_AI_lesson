import numpy as np

score_length = 10;
score = np.random.randint(50, 101, size=(score_length, 5));

print(score[5:,:]);
print(np.max(score, axis=1));
print(np.mean(score, axis=1));
print(np.median(score, axis=1));
print(np.std(score, axis=1));