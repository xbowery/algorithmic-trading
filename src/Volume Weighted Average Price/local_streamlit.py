from datetime import datetime

import bloomberg_vwap
import plotly.graph_objects as go
import plotly.io as pio
import streamlit as st

pio.renderers.default = 'browser'

st.title('VWAP Calculator (with Bloomberg Data)')

security = st.text_input('Enter the security ticker:', 'AAPL US Equity')
start_date = st.date_input('Enter the date:', value=datetime(2021, 1, 1))
start_time = st.time_input('Enter the start time:', value=datetime.strptime('09:30:00', '%H:%M:%S').time())
end_time = st.time_input('Enter the end time:', value=datetime.strptime('15:59:00', '%H:%M:%S').time())
interval = st.number_input('Enter the interval in minutes:', value=5)

if st.button('Calculate VWAP'):
    start_date = start_date.strftime('%Y-%m-%d')
    start_time = start_time.strftime('%H:%M:%S')
    end_time = end_time.strftime('%H:%M:%S')

    chart_data = bloomberg_vwap.intraday_vwap_chart(security, start_date, start_time, end_time, interval)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=chart_data.index, y=chart_data['vwap']))
    fig.update_layout(title=f'VWAP Price Chart for {security} for {start_date} between {start_time} and {end_time} with {interval} minutes interval')
    fig.show()

    st.write(f'The VWAP Price for {security} for {start_date} between {start_time} and {end_time} with {interval} minutes interval is:')
    st.write(chart_data['vwap'].tail(1).values[0])
