import streamlit as st
import data_loader

st.title("Expenses Tab")

expense_data=data_loader.load_expense_data(filename=data_loader.EXPENSE_FILENAME)
st.dataframe(expense_data)

select_month=st.selectbox("Select Month",["January","February","March","April","May","June","July","August","September","October","November","December"])
input_year=st.text_input("Enter Year")
month_year=f"{select_month} {input_year}"

number_month={
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}


add_day=st.selectbox("Select Day", range(1,32))
padded_day=f"{add_day:02d}"
add_date=f"{input_year}-{number_month[select_month]}-{padded_day}"
add_bucket=st.text_input(" Enter Budget Bucket")
add_description=st.text_input("Enter Description")
add_amount=int(st.number_input("Enter Amount Spent"))
add_button=st.button("Add")


if add_button:
    expense_data.append({
        "date": add_date,
        "month":month_year,
        "category":add_bucket,
        "description":add_description,
        "amount":add_amount
    })
    data_loader.save_expense_data(expense_data, filename=data_loader.EXPENSE_FILENAME)
    st.rerun()