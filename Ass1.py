import pandas as pd
import streamlit as st

st.write("APp")
df = pd.read_csv("Data Manipulation Worksheet.xlsx",sheet_name = "Financing Table" , parse_dates=['Date'],index_col=['Date'])
print(df)



