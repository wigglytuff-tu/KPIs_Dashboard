import streamlit as st
from whatsub.app import whatsub
from mix.app import mix
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
activities = ["whatsub","mix"]
choice = st.sidebar.selectbox("Select Activty", activities)
if choice == "whatsub":
    whatsub()
elif choice == "mix":
    mix()