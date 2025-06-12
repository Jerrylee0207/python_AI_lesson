import numpy as np
import math
import matplotlib.pyplot as plt


arr = np.arange(0, 2.5, 0.1);
arr_sin = np.sin(arr*math.pi);
arr_cos = np.cos(arr*math.pi);

plt.plot(arr, arr_sin, marker="o", color="blue", linestyle="");
plt.plot(arr, arr_cos, marker="^", color="orange", linestyle="");
plt.show();
plt.close();