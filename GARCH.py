from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
from arch import arch_model
import seaborn
import plotly.express as px

seaborn.set_style("darkgrid")
plt.rc("figure", figsize=(16, 6))
plt.rc("savefig", dpi=90)
plt.rc("font", family="sans-serif")
plt.rc("font", size=14)

START_DATE = '2010-01-01'
END_DATE = '2021-01-01'

STOCK = ['DIS']

stocks_data = data.DataReader(STOCK, 'yahoo', START_DATE, END_DATE)['Adj Close']
returns = 100 * stocks_data.pct_change().dropna()  # calculate percentage logarithmic returns
returns = returns[1:]  # removes first row

ax = returns.plot()
xlim = ax.set_xlim(returns.index.min(), returns.index.max())


model = arch_model(returns[1:], mean="Constant", vol="GARCH", p=1, q=1)
model_fit = model.fit()
print(model_fit.summary())
model_fit.plot(annualize="D")
plt.show()

stock_garch = returns.copy()
stock_garch['cond_vol'] = pd.DataFrame(model_fit.conditional_volatility)
garch_plot = px.line(stock_garch, title='GARCH model volatility of Daily Returns', width=1000, height=500)
garch_plot.update_layout(showlegend=False)
garch_plot.show()

