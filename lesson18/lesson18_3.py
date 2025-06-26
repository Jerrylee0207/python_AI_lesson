import yfinance as yf
import pandas as pd

tw2330 = yf.download('2330.TW',start='2024-01-01',end='2024-01-31',auto_adjust=True);
tw2303 = yf.download('2303.TW',start='2024-01-01',end='2024-01-31',auto_adjust=True);
tw2330_s = tw2330['Close']['2330.TW']
tw2303_s = tw2303['Close']['2303.TW']
stock = pd.DataFrame({"TSMC":tw2330_s, "UMC":tw2303_s});
print(stock);