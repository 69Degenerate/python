from matplotlib import colors, legend
import numpy as num
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import mean
import pandas as pd


# # method 1 to plot pie char
# x=[20,54,64,76]
# e=[0.1,0.1,0.1,0.1]
# plt.title("pir chart")
# plt.pie(x,labels=['a','s','d','f'],shadow=5,autopct='%1.1f%%')
# plt.pie(x,labels=['a','s','d','f'],shadow=5,autopct='%1.1f%%',explode=e)
# plt.pie(x)
# plt.legend()
# plt.show()

# # method 2 to plot pie chart
# data = {
#     'sport': ["Soccer", "Tennis", "Soccer", "Hockey"],
#     'players': [5, 4, 8, 20]
# }
# df = pd.DataFrame(data)
# df.groupby('sport')['players'].sum().plot(kind="pie")
# plt.show()