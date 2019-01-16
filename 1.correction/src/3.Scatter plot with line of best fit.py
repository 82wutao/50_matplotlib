"""
散点图与最佳拟合的线性回归线
如果你想了解两个变量如何相互改变，
那么最合适的线就是要走的路。 
下图显示了数据中各组之间最佳拟合线的差异。 
要禁用分组并仅为整个数据集绘制一条最佳拟合线，
请从下面的sns.lmplot（）调用中删除hue ='cyl'参数。
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
df_select = df.loc[df.cyl.isin([4,8]), :]

# Plot
sns.set_style("white")
gridobj = sns.lmplot(x="displ", y="hwy", hue="cyl", data=df_select, 
                     aspect=1.6, robust=True, palette='tab10', 
                     scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))

# Decorations
gridobj.set(xlim=(0.5, 7.5), ylim=(0, 50))
plt.title("Scatterplot with line of best fit grouped by number of cylinders", fontsize=20)
plt.show()


"""
Each regression line in its own column
Alternately, you can show the best fit line for each group in its own column. 
You cando this by setting the col=groupingcolumn parameter inside the sns.lmplot().
"""
# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
df_select = df.loc[df.cyl.isin([4,8]), :]

# Each line in its own column
"""
Seaborn中有五种可供选择的主题：
    1.darkgrid（灰色网格）
    2.whitegrid（白色网格）
    3.dark（黑色）
    4.white（白色）
    5.ticks（十字叉）
"""
sns.set_style("white")
gridobj = sns.lmplot(x="displ", y="hwy",   #lmplot是用来绘制回归图的，通过lmplot我们可以直观地总览数据的内在关系
                     data=df_select, 
                     robust=True, 
                     palette='Set1', 
                     col="cyl",
                     scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))

# Decorations
gridobj.set(xlim=(0.5, 7.5), ylim=(0, 50))
plt.show()










