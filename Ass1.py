import pandas as pd
import streamlit as st
import plotly as px

st.write("APP WORKING")
df = pd.read_csv("Data Maniupulation Worksheet.xlsx",sheet_name = 'Financing Table')
begDate = df.index.min()
endDate = df.index.max()
minDateDropdown = pd.to_datetime('2010-01-01')
pickStart =st.sidebar.date_input("Pick start date:",begDate,min_value = minDateDropdown)
pickEnd = st.sidebar.date_input("Pick start date:",endDate)

filterDF = df.loc[pickStart:pickEnd]


