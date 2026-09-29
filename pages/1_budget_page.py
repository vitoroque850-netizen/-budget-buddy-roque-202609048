import streamlit as st
import os
import sys
import data_loader

st.title("Budget Planner")
st.dataframe(data_loader.load_budget_data(filename=data_loader.BUDGET_FILENAME))
