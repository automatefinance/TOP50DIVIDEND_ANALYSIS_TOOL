import pandas as pd

import json 
import requests
import urllib3
from urllib3 import request


import streamlit as st



api_result = requests.get('http://api.marketstack.com/v1/dividends?access_key=d4dae97b992f9679cb6e46d027601db2&symbols=T,PFE,ABBV,XOM,GILD,INTC,ET,VZ,IBM,JPM,CVX,EPD,MO,UPS,MMM,C,KMI,MRK,BX,LUMN,BP,WBA,O,NRZ,NLY,AMGN,FTR,AGNC,VALE,ENB,RDS.A,KHC,VLO,DOW,PSEC,PM,DUK,DVN,MS,IIPR,RIO,PBR,GSK,SO,OHI,OKE,PRU,SPG,NEM,UTX,BKR,VTV,VYM,IWD,SCHD,RSP,IVE,DGRO,SPLG,SPYV,FVD&date_from=2017-01-01&date_to=2021-12-31&limit=1000&offset=0').json()


#dividend_index_data = 

dividend_index_df = pd.DataFrame(api_result['data'])
dividend_index_df = dividend_index_df.sort_values('date', ascending=True)

    
#oke_df = dividend_index_df.loc[(df['OKE'].isin(['symbol'])
oke_filter = (dividend_index_df["symbol"]=="OKE")


oke_df = dividend_index_df[oke_filter] 



oke_df.set_index('date').plot(kind = 'bar', rot=45)

symbol = st.selectbox('symbol', dividend_index_df.symbol.unique())


symbol_filter = (dividend_index_df["symbol"]== symbol)
symbol_df = dividend_index_df[symbol_filter] 
symbol_df.set_index('date')['dividend']
st.bar_chart(symbol_df.set_index('date')['dividend'])