import streamlit as st

st.write("CSS 2026")
st.write("day 3")
st.title("My first streamlit app")

number = st.slider("Pick a number", 1,1000)

st.write(f"you picked {number}")

st.header("heading 1")

st.markdown("Some text you can write")