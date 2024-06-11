from datetime import datetime

import bloomberg_twap
import plotly.graph_objects as go
import plotly.io as pio
import streamlit as st

pio.renderers.default = 'browser'

st.title('TWAP Calculator (with Bloomberg Data)')

security = st.text_input('Enter the security ticker:', 'AAPL US Equity')
start_date = st.date_input('Enter the start date:', value=datetime(2021, 1, 1))
end_date = st.date_input('Enter the end date:', value=datetime.today())

if st.button('Calculate TWAP'):
    start_date = start_date.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')

    chart_data = bloomberg_twap.twap_chart(security, start_date, end_date)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=chart_data.index, y=chart_data))
    fig.update_layout(title=f'TWAP Price Chart for {security} between {start_date} and {end_date}')
    fig.show()

    st.write(f'The TWAP Price for {security} between {start_date} and {end_date} is:')
    st.write(chart_data['Average'].mean())