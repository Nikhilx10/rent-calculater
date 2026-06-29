import sys
import streamlit as st

st.title("🏠 Flat Rent Calculator")

rent = st.number_input("Enter Flat Rent", min_value=0)
food = st.number_input("Enter Food Amount", min_value=0)
electricity = st.number_input("Enter Electricity Bill Units", min_value=0)
charge_per_unit = st.number_input("Enter Charge Per Unit", min_value=0.0)
person = st.number_input("Enter Number of Persons", min_value=1)

if st.button("Calculate"):
    total_bill = electricity * charge_per_unit
    output = (rent + food + total_bill) / person
    st.success(f"Each person will pay ₹{output:.2f}")
