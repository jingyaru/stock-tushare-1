import tushare as ts
import pandas as pd
from numpy import *

#codes = array([[u'招商证券','600999'],[u'广发证券','000776']])
codes = [
    [u'招商证券','600999'],[u'广发证券','000776'],[u'万科a','000002'],
    [u'保利地产','600048'],[u'招商银行','600036'],[u'工商银行','601398'],
    [u'恒瑞医药','600276'],[u'同仁堂','600685'],[u'大族激光','002008'],
    [u'三安光电','600703'],[u'中国石油','601857'],[u'中国石化','600028'],
    [u'ST中富','000659'],[u'ST山水','600234'],[u'沪深300','hs300']
]

for c in codes:
    print(c)
    print(c[1])
    print(c[0])
    df = ts.get_k_data(code=c[1],start='2007-10-31',end='2017-10-31')
    # print(df)
    df.to_csv('/Users/mac/Documents/datafromtushare/'+c[0]+'.csv')
    print('now'+c[0]+'earliest='+str(df.index[-1]))


