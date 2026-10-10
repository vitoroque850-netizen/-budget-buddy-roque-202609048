import streamlit as st
import data_loader

st.title("Budget Planner")

budget_data=(data_loader.load_budget_data(filename=data_loader.BUDGET_FILENAME))

select_month=st.selectbox("Select Month",["All"]+["January","February","March","April","May","June","July","August","September","October","November","December"])
input_year=st.text_input("Enter Year")

if select_month != "All" and input_year:
    month_year=f"{select_month} {input_year}"
    filter_budget_data=[row for row in budget_data if row["month"].strip()== month_year]
else:
    filter_budget_data=budget_data

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
    
st.dataframe(filter_budget_data)

if filter_budget_data:
    categories=[row["category"] for row in filter_budget_data]
    select_categ=st.selectbox("Select Budget Bucket", categories)

    specific_row= [row for row in filter_budget_data if row["category"]==select_categ][0]
    edit_category=st.text_input("Rename Bucket", value=specific_row["category"])
    edit_amount=st.number_input("Enter New Amount", value=specific_row["planned_amount"])

    update=st.button("Update")
    if update:
        specific_row["category"], specific_row["planned_amount"]=edit_category, edit_amount
        data_loader.save_budget_data(budget_data, filename=data_loader.BUDGET_FILENAME)

    delete=st.button("Delete")
    if delete:
        budget_data[:]=[row for row in budget_data if not (row["month"]==month_year 
                                                           and row["category"]==select_categ)]
        data_loader.save_budget_data(budget_data, filename=data_loader.BUDGET_FILENAME)
        st.rerun()

all_planned_amount=[row["planned_amount"]for row in filter_budget_data]
all_income=[row["income"]for row in filter_budget_data]
total_planned_amount=sum(all_planned_amount)
total_income=sum(all_income)

st.write("Total Income: ",{total_income})
st.write("Total Planned Amount: ",{total_planned_amount})

if total_planned_amount > total_income:
    st.write("Planned expenses exceed income!")
else:
    unallocated_income=total_income-total_planned_amount
    st.write("Unallocated Income: ",{unallocated_income})



 

