import streamlit as st
import 1_budget_page
import 3_expense_page

filter_budget_data=1_budget_page.filter_budget_data
expense_data=3_expense_page.expense_data

select_month=st.selectbox("Select Month",["All"]+["January","February","March","April","May","June","July","August","September","October","November","December"])
input_year=st.text_input("Enter Year",value="2026")

all_planned_amount=[row["planned_amount"]for row in filter_budget_data]
all_income=[row["income"]for row in filter_budget_data]
all_actual_expenses=[row["amount"]for row in expense_data]

total_planned_amount=sum(all_planned_amount)
total_income=all_income[0]
total_actual_expenses=sum(all_actual_expenses)
unallocated_income=total_income-total_planned_amount
