import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore

# 建立一些資料
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 繪製圖表
plt.plot(x, y)

# 加入標題和標籤
plt.title("Simple Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# 顯示圖表
plt.show()