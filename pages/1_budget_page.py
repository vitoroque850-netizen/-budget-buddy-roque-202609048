import streamlit as st
import pandas as pd
import data_loader

st.title("Budget Planner")

budget_data=(data_loader.load_budget_data(filename=data_loader.BUDGET_FILENAME))
pd_budget=pd.DataFrame(budget_data)

select_month=st.selectbox("Select Month",["January","February","March","April","May","June","July","August","September","October","November","December"])
input_year=st.text_input("Enter Year")
month_year=f"{select_month} {input_year}"

filter_budget_data=pd_budget[pd_budget['month']== month_year]
st.dataframe(filter_budget_data)

income_source=st.text_input("Enter Income Source:")
expected_income=st.number_input("Enter Expected Income")

