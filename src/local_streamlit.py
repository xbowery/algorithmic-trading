import bloomberg_twap
from datetime import datetime
import streamlit as st

st.title('TWAP Calculator (with Bloomberg Data)')

security = st.text_input('Enter the security ticker:', 'AAPL US Equity')
start_date = st.date_input('Enter the start date:', value=datetime(2021, 1, 1))
end_date = st.date_input('Enter the end date:', value=datetime.today())

if st.button('Calculate TWAP'):
    start_date = start_date.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')
    st.write(f'The TWAP price for {security} between {start_date} and {end_date} is:')
    st.write(bloomberg_twap.twap_price(security, start_date, end_date))