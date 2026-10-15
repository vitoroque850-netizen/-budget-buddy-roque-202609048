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

months_list=[]
total_income=0
for row in filter_budget:
    months=row["month"]

    if months not in months_list:
        months_list.append(months)
        total_income+= float(row["income"])

total_planned_amount=sum(all_planned_amount)
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
        planned_amounts=float(row["planned_amount"])

        if categories in categories_list:
            amount_list[categories_list.index(categories)]+=planned_amounts
        else:
            categories_list.append(categories)
            amount_list.append(planned_amounts)

fig_1, ax_1 =plt.subplots()
ax_1.pie(amount_list, labels=categories_list, autopct="%1.1f%%")
ax_1.set_title("Planned Budget Distribution")
st.pyplot(fig_1)

fig_2, ax_2=plt.subplots(figsize=(10,7))
compare=["Planned Expenses","Actual Expenses"]
compare_totals=[total_planned_amount, total_actual_expenses]

ax_2.set_ylabel("Amount")
ax_2.set_title("Planned Expenses vs Actual Expenses")
bars=ax_2.bar(compare,compare_totals, color=["#CBD5E1","#05751D"])

st.pyplot(fig_2)

planned_by_category={}
for row in filter_budget:
    categories=row["category"]
    planned_amounts=float(row["planned_amount"])
    planned_by_category[categories]=planned_by_category.get(categories,0)+planned_amounts

actual_by_category={}
for row in filter_expense:
    categories=row["category"]
    actual_amounts=float(row["amount"])
    actual_by_category[categories]=actual_by_category.get(categories,0)+actual_amounts

combine_categories=list(set(list(planned_by_category.keys())+list(actual_by_category.keys())))

planned_expense=planned_by_category.get(categories,0)
actual_expense=actual_by_category.get(categories,0)

for categories in combine_categories:
    planned_expense=planned_by_category.get(categories,0)
    actual_expense=actual_by_category.get(categories,0)
    remaining=planned_expense-actual_expense

    st.markdown(f"Category: {categories}")
    col1, col2, col3 = st.columns(3)
    col1.write(f"Planned Expenses: ${planned_expense:,.2f}")
    col2.write(f"Actual Expenses: ${actual_expense:,.2f}")

    if actual_expense>planned_expense:
        col3.error(f"Over the Budget by: ${actual_expense-planned_expense:,.2f}")
    else:
        col3.write(f"Remaining: ${remaining:,.2f}")