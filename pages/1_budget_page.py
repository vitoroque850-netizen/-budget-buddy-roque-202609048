import streamlit as st
import os
import sys
import data_loader

st.title("Budget Planner")

select_month=st.selectbox("Select Month",["January","february","March","April","May","June","July","August","September","October","November","December"])
input_year=st.text_input("Enter Year")
month_year=f"{select_month} {input_year}"

income_source=st.text_input("Enter Income Source:")
expected_income=st.text_input("Enter Expected Income")

st.dataframe(data_loader.load_budget_data(filename=data_loader.BUDGET_FILENAME))