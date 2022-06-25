import streamlit as st
from mix.getMixpanelData  import getMixPanelData
import plotly.express as px
from mix.utilities import display,display2,display3

def mix():

    # st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
    # ---- LOAD DATA ----

    fd = st.text_input("From Date:","2022-06-11")
    td = st.text_input("To Date:","2022-06-15" )
    df = getMixPanelData(fd,td)

    # ---- SIDEBAR ----
    activities = ["city", "brand" , "carrier", "event","distinct events"]
    choice = st.sidebar.selectbox("Select Activty", activities)

    if choice == "city":
        display(df,choice)
    elif choice == "brand":
        display(df,choice)
    elif choice == "carrier":
        display(df,choice)
    elif choice == "event":
        display2(df)
    elif choice =="distinct events":
        display3(df)