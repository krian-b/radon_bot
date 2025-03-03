import yfinance as yf

def get_data(args):
    args_dict = vars(args)
    stock = yf.Ticker(args_dict['symbol']+".NS")
    interval = args_dict['interval']
    period = args_dict['period']
    
    if interval == '1m':
        period = '1d'
    elif interval == '5m' or interval == '15m':
        period = '1mo'
        

    data = stock.history(
        period=period,
        interval=interval
        )
    data = data.reset_index()
    data = data.dropna()

    try:
        data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')
    except:
        data['Datetime'] = data['Datetime'].dt.strftime('%Y-%m-%d')
        data = data.rename(columns={'Datetime': 'Date'})

    data.columns = data.columns.str.lower()
    data = data.rename(columns={'date': 'timestamp'})
    data = data.drop(columns=['dividends', 'stock splits'])
    data = data.round(2)
    return data
    