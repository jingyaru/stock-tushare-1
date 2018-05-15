import tushare as ts

df=ts.get_hist_data('000875')

df.to_csv('/Users/mac/Documents/datafromtushare/000875.csv')

