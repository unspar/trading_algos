from zipline.api import (
    history,
    order_target,
    record,
    symbol
)

import matplotlib.pyplot as plt
from zipline import run_algorithm
import pyfolio as pf
import matplotlib
import datetime

matplotlib.style.use('ggplot')
def initialize(context):
    context.i = 0


def handle_data(context, data):
    # Skip first 300 days to get full windows
    context.i += 1
    if context.i < 300:
        return

    # Compute averages
    # history() has to be called with the same params
    # from above and returns a pandas dataframe.
    short_mavg = history(100, '1d', 'price').mean()
    long_mavg = history(300, '1d', 'price').mean()

    sym = symbol('AAPL')

    # Trading logic
    order(sym, 1)
    '''
    if short_mavg[sym] > long_mavg[sym]:
        # order_target orders as many shares as needed to
        # achieve the desired number of shares.
        order_target(sym, 100)
    elif short_mavg[sym] < long_mavg[sym]:
        order_target(sym, 0)

    # Save values for later inspection
    record(AAPL=data[sym].price,
           short_mavg=short_mavg[sym],
           long_mavg=long_mavg[sym])
    '''
zero_tc = datetime.timedelta()
utc = datetime.timezone(zero_tc)
start = datetime.datetime(2016, 1, 1, tzinfo=utc)
end = datetime.datetime(2016, 12, 31, tzinfo=utc)


rets= run_algorithm(initialize=initialize, handle_data=handle_data, capital_base=1000, start=start, end=end )
stock_rets = rets.portfolio_value
print(list(rets))
stock_rets.plot()
plt.show()
#stock_rets = pf.utils.get_symbol_rets('FB')
out_of_sample = stock_rets.index[-40]

pf.create_bayesian_tear_sheet(stock_rets, live_start_date=out_of_sample)




