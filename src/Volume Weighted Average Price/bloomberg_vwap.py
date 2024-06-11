from xbbg import blp

import pandas as pd
import time


def get_data(ticker, date):
    data = blp.bdib(ticker, dt=date)

    return data[:-1]


def intraday_vwap_price(ticker, date, start_time, end_time, interval):
    data = get_data(ticker, date)

    if data.empty:
        print("Please check the input data again.")
        return None
    
    check_start_time = time.strptime(start_time, '%H:%M:%S')
    check_end_time = time.strptime(end_time, '%H:%M:%S')

    if check_start_time < time.strptime('09:30:00', '%H:%M:%S') or check_end_time > time.strptime('15:59:00', '%H:%M:%S'):
        print("Please check the input time again. It has to be between 09:30:00 and 15:59:00.")
        return None

    data = data[ticker]
    data.index = data.index.tz_convert(None)
    data = data.between_time(start_time, end_time)
    data = data.resample(f'{interval}min').agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last', 'volume': 'sum'})

    data['typical'] = (data['close'] + data['high'] + data['low']) / 3
    data['tpv'] = data['typical'] * data['volume']
    data['vwap'] = data['tpv'].cumsum() / data['volume'].cumsum()

    return data['vwap'].tail(1).values[0]


def intraday_vwap_chart(ticker, date, start_time, end_time, interval):
    data = get_data(ticker, date)

    if data.empty:
        print("Please check the input data again.")
        return None
    
    check_start_time = time.strptime(start_time, '%H:%M:%S')
    check_end_time = time.strptime(end_time, '%H:%M:%S')

    if check_start_time < time.strptime('09:30:00', '%H:%M:%S') or check_end_time > time.strptime('15:59:00', '%H:%M:%S'):
        print("Please check the input time again. It has to be between 09:30:00 and 15:59:00.")
        return None

    data = data[ticker]
    data.index = data.index.tz_convert(None)
    data = data.between_time(start_time, end_time)
    data = data.resample(f'{interval}min').agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last', 'volume': 'sum'})

    data['typical'] = (data['close'] + data['high'] + data['low']) / 3
    data['tpv'] = data['typical'] * data['volume']
    data['vwap'] = data['tpv'].cumsum() / data['volume'].cumsum()

    return data

