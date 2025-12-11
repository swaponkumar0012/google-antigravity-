import streamlit as st
from calculator import add, subtract, multiply, divide

st.set_page_config(page_title="Simple Calculator", page_icon="🧮")

st.title("🧮 Simple Calculator")

# Input numbers
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number", value=0.0)
with col2:
    num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

# Calculate button
if st.button("Calculate"):
    result = None
    if operation == "Add":
        result = add(num1, num2)
        st.success(f"{num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.success(f"{num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.success(f"{num1} * {num2} = {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        if result == "Error! Division by zero.":
            st.error(result)
        else:
            st.success(f"{num1} / {num2} = {result}")

st.markdown("---")
st.caption("Built with Streamlit and Python")
