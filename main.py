from pandas_datareader import data
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from scipy.cluster.hierarchy import dendrogram, linkage

START_DATE = '2020-02-01'
END_DATE = '2021-10-01'

STOCK = [ 'BARC.L', 'AZN.L', 'GSK.L', 'ULVR.L', 'DGE.L', 'BP.L', 'RDSB.L', 'RIO.L', 'AAL.L']


def get_data(ticker):
    stocks_data = data.DataReader(ticker, 'yahoo', START_DATE, END_DATE)['Adj Close']
    # print(stocks_data)
    returns = stocks_data.pct_change()  # calculate logarithmic returns
    returns = returns[1:]  # removes first row
    # print(returns)
    corr = returns.corr()
    print(corr)
    dist = corr.apply(lambda x: np.sqrt(2 * (1 + x * -1)))
    # dist.to_csv('dist.csv',index=False)
    size = 7
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(dist, cmap=cm.get_cmap('summer'), vmin=0.5, vmax=2)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical', fontsize=8)
    plt.yticks(range(len(corr.columns)), corr.columns, fontsize=8)
    plt.show()
    z = linkage(dist, 'ward')
    dendrogram(z, labels=dist.index, color_threshold=0, above_threshold_color='blue')
    plt.show()


get_data(STOCK)
