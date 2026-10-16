import streamlit as st
import data_loader

st.title("Budget Planner")

budget_data=(data_loader.load_budget_data(filename=data_loader.BUDGET_FILENAME))

st.header("Monthly Budget Setup")
st.caption("Select a month and enter an income source and expected income.")

col_m, col_y=st.columns(2)
with col_m:
    select_month=st.selectbox("Select Month",["All"]+["January","February","March","April","May","June","July","August","September","October","November","December"])
with col_y:
    input_year=st.text_input("Enter Year", value="2027")

month_year=f"{select_month} {input_year}"

if select_month != "All" and input_year:
    filter_budget_data=[row for row in budget_data if row["month"].strip()== month_year]
else:
    filter_budget_data=budget_data

if filter_budget_data:
    get_source=filter_budget_data[0]["income_source"]
    get_income=(filter_budget_data[0]["income"])
else:
    get_source=""
    get_income=0

col_inc1, col_inc2=st.columns(2)
with col_inc1:
    income_source=st.text_input("Enter Income Source:",value=get_source)
with col_inc2:
    expected_income=st.number_input("Enter Expected Income",value=get_income)



st.header("Customizable Budget Categories")
st.caption("Start with default categories and add, rename, edit, or remove budget buckets.")

col_add, col_edit=st.columns(2)
with col_add:
    st.subheader("Add New Budget Bucket")
    add_bucket=st.text_input("Add New Budget Bucket")
    add_amount=int(st.number_input("Add New Planned Amount"))
    add_button=st.button("Add")

    if add_bucket and add_button:
        budget_data.append({
            "month":month_year,
            "income_source":income_source,
            "income":expected_income,
            "category":add_bucket,
            "planned_amount":add_amount
        })

        data_loader.save_budget_data(budget_data, filename=data_loader.BUDGET_FILENAME)
        st.rerun()
    
st.dataframe(filter_budget_data)

with col_edit:
    st.subheader("Edit Budget Bucket")
    if filter_budget_data:
        categories=[row["category"] for row in filter_budget_data]
        select_categ=st.selectbox("Select Budget Bucket", categories)

        specific_row= [row for row in filter_budget_data if row["category"]==select_categ][0]
        edit_category=st.text_input("Rename Bucket", value=specific_row["category"])
        edit_amount=st.number_input("Enter New Amount", value=specific_row["planned_amount"])

        col_upd,col_del=st.columns(2)
        with col_upd:
            update=st.button("Update")
            if update:
                specific_row["category"], specific_row["planned_amount"]=edit_category, edit_amount
                data_loader.save_budget_data(budget_data, filename=data_loader.BUDGET_FILENAME)
        with col_del:
            delete=st.button("Delete")
            if delete:
                budget_data[:]=[row for row in budget_data if not (row["month"]==month_year 
                                                                   and row["category"]==select_categ)]
                data_loader.save_budget_data(budget_data, filename=data_loader.BUDGET_FILENAME)
                st.rerun()

st.header("Budget Calculations")
st.caption("Automatically calculate total planned expenses and unallocated income.")

all_planned_amount=[row["planned_amount"]for row in filter_budget_data]
all_income=[row["income"]for row in filter_budget_data]
total_planned_amount=sum(all_planned_amount)

months_list=[]
total_income=0
for row in filter_budget_data:
    months=row["month"]

    if months not in months_list:
        months_list.append(months)
        total_income+= float(row["income"])

unallocated_income=total_income-total_planned_amount
exceed_income=total_planned_amount-total_income

col1,col2=st.columns(2)

col1.metric(label="Total Income: ",value=f"${total_income:,.2f}")
col2.metric(label="Total Planned Expenses: ",value=f"${total_planned_amount:,.2f}")

if total_planned_amount > total_income:
    st.warning(f"Planned expenses exceed income by ${exceed_income:,.2f} !")
else:
    st.success(f"Unallocated Income: ${unallocated_income:,.2f}")



 

