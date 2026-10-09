import streamlit as st
import data_loader

st.title("Budget Planner")

budget_data=(data_loader.load_budget_data(filename=data_loader.BUDGET_FILENAME))

select_month=st.selectbox("Select Month",["January","February","March","April","May","June","July","August","September","October","November","December"])
input_year=st.text_input("Enter Year")
month_year=f"{select_month} {input_year}"

filter_budget_data=[row for row in budget_data if row['month']== month_year]
st.dataframe(filter_budget_data)

if filter_budget_data:
    get_source=filter_budget_data[0]["income_source"]
    get_income=(filter_budget_data[0]["income"])
else:
    get_source=""
    get_income=0


income_source=st.text_input("Enter Income Source:",value=get_source)
expected_income=st.number_input("Enter Expected Income",value=get_income)

