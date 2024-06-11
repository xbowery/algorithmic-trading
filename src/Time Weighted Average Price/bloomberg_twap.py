from xbbg import blp


def get_data(ticker, start_date, end_date):
    data = blp.bdh(tickers=ticker, flds=['px_open', 'high', 'low', 'px_last'], 
                   start_date=start_date, end_date=end_date)
    return data


def twap_price(ticker, start_date, end_date):
    data = get_data(ticker, start_date, end_date)

    if data.empty:
        print("Please check the input data again.")
        return None
    
    data = data[ticker]
    data['Average'] = data.mean(axis=1)
    return data['Average'].mean()


def twap_chart(ticker, start_date, end_date):
    data = get_data(ticker, start_date, end_date)

    if data.empty:
        print("Please check the input data again.")
        return None
    
    data = data[ticker]
    data['Average'] = data.mean(axis=1)
    return data['Average']
