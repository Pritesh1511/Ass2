import pandas as pd
import streamlit as st

st.write("APp")
df = pd.read_csv("Data Manipulation Worksheet.xlsx","Financing Table" , parse_dates=['Date'],index_col=['Date'])



