import streamlit as st

st.title("test Python Web Apps")
st.write("Just Cheking test web app")

if st.button("click me"):
    st.write("You have clicked the button")


name=st.text_input("Please enter your name")

if name:
    st.write("Hello ",name)


num1=st.number_input("Enter first number")
num2=st.number_input("Enter Second number")

add=num1+num2

st.write("addtion = ",add)


picked_value=st.slider("Pick Number ",1,100)

st.write("Value picked = ",picked_value)

input_date=st.date_input("Please pick the date")
st.write("You picked date = ",input_date)


import pandas as pd
import numpy as np

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data