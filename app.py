import streamlit as st
import streamlit.components.v1 as components

# Include Google Analytics tracking code
with open("index.html", "r") as f:
    html_code = f.read()
    components.html(html_code, height=0)

st.title("My Streamlit App")