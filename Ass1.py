import pandas as pd
import streamlit as st

st.write("APp")
df = pd.read_csv("Data Maniupulation Worksheet.xlsx",sheet_name = "Financing Table" , parse_dates=['Date'],index_col=['Date'])

begDate = df.index.min()
endDate = df.index.max()
minDateDropdown = pd.to_datetime('2007-01-01')
pickStart =st.sidebar.date_input("Pick start date:",begDate,min_value = minDateDropdown)
pickEnd = st.sidebar.date_input("Pick start date:",endDate)


filterDF = df.loc[pickStart:pickEnd]
st.write(filterDF)


