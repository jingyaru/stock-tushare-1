#%matplotlib inline

import matplotlib as mpl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.font_manager import FontProperties
from sklearn.cluster import affinity_propagation

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


#column:,date,open,close,high,low,volume,code


dpi=72.
xinch=800/dpi
yinch=400/dpi
mpl.rcParams['figure.figsize']=(xinch,yinch)

stocks=[[u'招商证券','600999'],[u'广发证券','000776'],[u'万科a','000002'],
[u'保利地产','600048'],[u'招商银行','600036'],[u'工商银行','601398'],
[u'恒瑞医药','600276'],[u'同仁堂','600685'],[u'大族激光','002008'],
[u'三安光电','600703'],[u'中国石油','601857'],[u'中国石化','600028'],
[u'ST中富','000659'],[u'ST山水','600234'],[u'沪深300','hs300']]

codes={}
for s in stocks:
    codes[s[0]]=s[1]
symbols=codes.keys()

def col_converter(x):
    try:
        return float(x)
    except:
        return None

prices=None
for i,s in enumerate(symbols):
    p=pd.read_csv('/Users/mac/Documents/datafromtushare/'+s.upper()+'.csv',usecols=['close','date'],
                  index_col='date',converters={'close':col_converter})
    if i==0:
        prices=pd.DataFrame(index=p.index)
    prices[s]=p['close']
prices.sort_index(ascending=True,inplace=True)
prices.dropna(inplace=True)
 


"""prices[[u'招商证券',u'广发证券',u'万科a',u'保利地产']].plot()
plt.ylabel(u'每日收盘价')
plt.xlabel(u'日期')
plt.legend()
plt.savefig('/Users/mac/Documents/datafromtushare/pricechange.png')
plt.show()

print('----期初股价----')
print(prices[[u'招商证券',u'广发证券',u'万科a',u'保利地产']].head(1))
print('----期末股价----')
print(prices[[u'招商证券',u'广发证券',u'万科a',u'保利地产']].tail(1))"""



#earningrate#
prices_norm=prices.copy()
for symbol in symbols:
    prices_norm[symbol]=prices[symbol]/prices[symbol][0]
prices_norm[[u'招商证券',u'广发证券',u'万科a',u'保利地产']].plot()
plt.ylabel(u'收益率')
plt.xlabel(u'日期')
plt.legend()
#plt.savefig('/Users/mac/Documents/datafromtushare/earningrate.png')
print(prices_norm[[u'招商证券',u'广发证券',u'万科a',u'保利地产']].tail(1))

#wave#
prices.pct_change()[[u'招商证券',u'广发证券',u'万科a',u'保利地产']].plot()
plt.ylabel(u'每日波动率')
plt.xlabel(u'日期')
plt.legend()
#plt.savefig('/Users/mac/Documents/datafromtushare/waverate.png')
print(prices.pct_change()[[u'招商证券',u'广发证券',u'万科a',u'保利地产']].describe())


#relate#
co=prices.pct_change().corr()
for symbol in symbols:
    v=co[symbol].sort_values()
    print(symbol,u'|正相关度最高：',v.index[-2],u'相关系数=',v[-2],u'|负相关度最高：',v.index[0],u'相关系数=',v[0])
    print('')

#cluster#
_,labels=affinity_propagation(co)
df_c=pd.DataFrame({'label':labels,'name':symbols})
g=df_c.groupby('label')
for item in g:
    print(item)
    #print(item[0],','.join(item[1]['name'].values))
    print('---------------------')

#is normal distribution#
#prices.pct_change().hist(column=[u'恒瑞医药',u'招商银行',u'保利地产',u'三安光电'],sharex=True,sharey=True,bins=30)


#组合#
group_dots=np.linspace(0,1,100,endpoint=False)
hryy_wka=pd.DataFrame({
    u'回报':pd.Series([(r*prices_norm[u'恒瑞医药']+(1-r)*prices_norm[u'万科a']).pct_change().mean() for r in group_dots],index=group_dots),
    u'风险':pd.Series([(r*prices_norm[u'恒瑞医药']+(1-r)*prices_norm[u'万科a']).pct_change().std() for r in group_dots],index=group_dots)
})
ax=hryy_wka.plot(secondary_y=u'风险')
ax.set_xlabel(u'恒瑞医药占比')
ax.set_ylabel(u'单日股价波动均值')
ax.right_ax.set_ylabel(u'单日股价波动标准差')
plt.title(u'恒瑞医药+万科a 不同配比的收益风险变化图')
plt.savefig('/Users/mac/Documents/datafromtushare/grouprisk.png')