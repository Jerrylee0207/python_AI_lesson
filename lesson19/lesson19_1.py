import yfinance as yf
import pandas as pd

tw2330 = yf.download('2330.TW',start='2024-01-01',end='2024-06-01',auto_adjust=True);
tw2303 = yf.download('2303.TW',start='2024-01-01',end='2024-06-01',auto_adjust=True);
tw2454 = yf.download('2454.TW',start='2024-01-01',end='2024-06-01',auto_adjust=True);
tw2317 = yf.download('2317.TW',start='2024-01-01',end='2024-06-01',auto_adjust=True);


tw2330_s = tw2330[('Close','2330.TW')];
tw2303_s = tw2303[('Close','2303.TW')];
tw2454_s = tw2454[('Close','2454.TW')];
tw2317_s = tw2317[('Close','2317.TW')];
df_price = pd.DataFrame({"TSMC":tw2330_s,"LD":tw2303_s,"LFK":tw2454_s,"HH":tw2317_s});

##print(df_price);

import matplotlib.pyplot as plt
import seaborn as sns

'''
df_matrix = df_price.corr();
figure = plt.figure(figsize=(10, 8));
axes = figure.add_subplot(1,1,1);
sns.heatmap(df_matrix, annot=True, cmap='coolwarm',axes=axes);
axes.set_title("stock price corr heat map");
plt.show();
'''

figure = plt.figure(figsize=(10, 8))
axes = figure.add_subplot(1,1,1)
df_price.plot(title='stock price trend', xlabel='date', ylabel='price',ax=axes)
##plt.show()

print(df_price.diff());

percent_df = df_price.pct_change()
formatted = percent_df.map(lambda x: f"{x:.2%}" if pd.notnull(x) else "")
print(formatted);

print("solve object is empty\n");