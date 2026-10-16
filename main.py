import streamlit as st

st.title("My Budget Buddy")
st.caption("Budget Buddy helps you to manage your money by keeping track of your income and expenses")

st.subheader("Budget Planner")
st.markdown("""
**Features/Functions:**
* Monthly Budget Setup - Allow users to select a month and enter an income source and expected income. This also filters the data displayed for the selected month.
* Customizable Budget Categories - Allow users to add, rename, edit, and remove budget buckets.
* Budget Calculations - Automatically calculate total planned expenses and unallocated income.""")

st.subheader("Expense Tracker")
st.markdown("""
**Features/Functions:**
* Expense Recording - Record the date, category, description, and amount of an expense.
* Expense Validation - Prevent invalid amounts and incomplete expense entries.
* Expense History - Display previously recorded expenses with their relevant information.""")

st.subheader("Dashboard")
st.markdown("""
**Features/Functions:**
* Monthly Financial Summary - Select a month and display income, planned expenses, actual expenses, and money remaining.
* Budget Visualization - Display a pie chart showing the planned budget distribution by category. Display a chart comparing planned and actual spending.
* Budget Breakdown - Show each category's planned amount, actual spending, and remaining/over-budget amount.""")