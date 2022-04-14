import numpy as np
import pandas
import matplotlib.pyplot as plt
import seaborn as sns

#%%
sns.set_style("darkgrid")
sns.set(font_scale = 1.2)

f,a=plt.subplots(2,1,figsize=(6,8))

d=pandas.read_csv('nfarms.csv',index_col=0)
ax=sns.lineplot(ax=a[0],data=d.T/1000)
ax.set(ylabel='Number of Farms (thousand)')
l=ax.legend(loc='upper right')
l=l.get_frame()
l.set_facecolor('white')

d=pandas.read_csv('pfarms.csv',index_col=0)
ax=sns.lineplot(ax=a[1],data=d.T)
ax.set(ylabel='% Market Share')
plt.legend([],[], frameon=False)

plt.rcParams['pdf.fonttype'] = 42
plt.savefig('vt_farm.pdf')
