import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {'年廣告費投入':[12.5, 15.3, 23.2, 26.4, 33.5, 34.4, 39.4, 45.2, 55.4, 60.9],
            '月均銷售額':[21.2, 23.9, 32.9, 34.1, 42.5, 43.2, 49.0, 52.8, 59.4, 63.5]}
dataFrame = pd.DataFrame(data, index=[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])
corration = dataFrame['年廣告費投入'].corr(dataFrame['月均銷售額'])


figure = plt.figure(figsize=(8,5))
axes = figure.add_subplot()
axes.plot(dataFrame.index,dataFrame['年廣告費投入'],marker='.')
axes.plot(dataFrame.index,dataFrame['月均銷售額'],marker='.')
plt.show()