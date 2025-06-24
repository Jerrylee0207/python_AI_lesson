import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display

'''
df = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "id": [2, 5],
    "score": [575.6, 1523.7]
});

print(df);

s = df.style.format(precision=3, thousands=",", decimal='.').format_index(str.upper, axis=1);
'''

wea_size = 10;
weather_df = pd.DataFrame(np.random.rand(wea_size, 2)*5,
                          index=pd.date_range(start="2024-01-01", periods=wea_size),
                          columns=["TYO", "TPE"]);

def rain_condition(v):
    if v<1.75:
        return "dry";
    elif v<2.75:
        return "tiny rain";
    else:
        return "huge rain";

def check_style(styler):
    styler.set_caption("weather condition");
    styler.format(rain_condition);
    styler.format_index(formatter=lambda v:v.strftime("%Y/%m/%d %A"));
    styler.background_gradient(axis=None,vmin=1,vmax=5,cmap="PuBuGn");
    return styler;

weather_rain = weather_df.loc[:].style.pipe(check_style);
print(weather_rain.to_string());

'''
print(weather_df.info());
print(weather_df.loc["2024-01"]);

figure = plt.figure(figsize=(10,6));
axes = figure.add_subplot(1,1,1);
axes.plot(weather_df.index,weather_df["TYO"],label="TYO",linestyle='',marker='.');
axes.plot(weather_df.index,weather_df["TPE"],label="TPE",linestyle='',marker='.');
##plt.show()
##plt.close()
'''