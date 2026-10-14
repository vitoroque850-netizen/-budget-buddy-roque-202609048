import streamlit as st
import data_loader
import matplotlib.pyplot as plt
import numpy as np

budget_data=(data_loader.load_budget_data(filename=data_loader.BUDGET_FILENAME))
expense_data=data_loader.load_expense_data(filename=data_loader.EXPENSE_FILENAME)

select_month=st.selectbox("Select Month",["All"]+["January","February","March","April","May","June","July","August","September","October","November","December"])
input_year=st.text_input("Enter Year",value="2027")

if select_month != "All" and input_year:
    month_year=f"{select_month} {input_year}"
    filter_budget=[row for row in budget_data if row["month"].strip()== month_year]
    filter_expense=[row for row in expense_data if row["month"].strip()== month_year]
else:
    filter_budget=budget_data
    filter_expense=expense_data

all_planned_amount=[row["planned_amount"]for row in filter_budget]
all_income=[row["income"]for row in filter_budget]
all_actual_expenses=[row["amount"]for row in filter_expense]

total_planned_amount=sum(all_planned_amount)
total_income=all_income[0]
total_actual_expenses=sum(all_actual_expenses)
unallocated_income=total_income-total_actual_expenses

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Income", value=f"${total_income:,.2f}")
col2.metric(label="Planned Expenses", value=f"${total_planned_amount:,.2f}")
col3.metric(label="Actual Expenses", value=f"${total_actual_expenses:,.2f}")
col4.metric(label="Money Remaining", value=f"${unallocated_income:,.2f}")

if filter_budget:
    categories_list=[]
    amount_list=[]

    for row in filter_budget:
        categories=row["category"]
        amounts=float(row["planned_amount"])

        if categories in categories_list:
            amount_list[categories_list.index(categories)]+=amounts
        else:
            categories_list.append(categories)
            amount_list.append(amounts)

fig, ax =plt.subplots()
ax.pie(amount_list, labels=categories_list, autopct="%1.1f%%")
ax.set_title("Planned Budget Distribution")
st.pyplot(fig)