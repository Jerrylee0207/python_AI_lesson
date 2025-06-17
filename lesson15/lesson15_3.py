import pandas as pd
df = pd.read_csv('個股日成交資訊.csv',usecols=['證券代號','證券名稱','開盤價','收盤價','漲跌價差'],index_col='證券代號')
print(df.loc['0050'])
print(df.loc['0050':'0055'])
print(df.iloc[:10])