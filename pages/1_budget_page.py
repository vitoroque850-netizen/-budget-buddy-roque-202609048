import streamlit as st
import data_loader

st.title("Budget Planner")

budget_data=(data_loader.load_budget_data(filename=data_loader.BUDGET_FILENAME))

select_month=st.selectbox("Select Month",["All"]+["January","February","March","April","May","June","July","August","September","October","November","December"])
input_year=st.text_input("Enter Year")

if select_month != "All" and input_year:
    month_year=f"{select_month} {input_year}"
    filter_budget_data=[row for row in budget_data if row['month']== month_year]
else:
    filter_budget_data=budget_data
st.dataframe(filter_budget_data)

if filter_budget_data:
    get_source=filter_budget_data[0]["income_source"]
    get_income=(filter_budget_data[0]["income"])
else:
    get_source=""
    get_income=0

income_source=st.text_input("Enter Income Source:",value=get_source)
expected_income=st.number_input("Enter Expected Income",value=get_income)

add_bucket=st.text_input("Add New Budget Bucket")
add_amount=int(st.number_input("Add New Planned Amount"))
add_button=st.button("Add")

if add_bucket and add_button:
    budget_data.append({
        "month":month_year,
        "income_source":get_source,
        "income":get_income,
        "category":add_bucket,
        "planned_amount":add_amount
    })

data_loader.save_budget_data(budget_data, filename=data_loader.BUDGET_FILENAME)
st.rerun()