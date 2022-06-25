import pandas as pd
import streamlit as st
from whatsub.data import load_data
from whatsub.utilitites import display,display_1, display_2, display_3,display_4
def whatsub():
    # st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

    activities = ["auth", "whatsub_rooms" , "whatsub_message","whatsub_users_subscription",
    "whatsub_search_logs","whatsub_wallet","whatsub_quiz"]
    choice = st.sidebar.selectbox("Select Activty", activities)
    if choice=="auth":
        # ---- LOAD DATA ----
        query = """ query MyQuery {
                        auth(order_by: {created_at: desc}) {
                        id
                        created_at
                    }
                }"""
        df = load_data(query,choice)
        display(df)
        
    elif choice=="whatsub_rooms":
        query = """query whatsub_rooms {
                        whatsub_rooms(order_by: {created_at: desc}) {
                        id
                        created_at
                    }
                }"""
        df = load_data(query,choice)
        display(df)

    elif choice=="whatsub_message":
        query = """query whatsub_rooms {
                        whatsub_message(order_by: {created_at: desc}) {
                        id
                        created_at
                    }
                }"""
        df = load_data(query,choice)
        display(df)

    elif choice=="whatsub_search_logs":
        query = """query whatsub_rooms {
                        whatsub_search_logs(order_by: {created_at: desc}) {
                        id
                        created_at
                    }
                }"""
        df = load_data(query,choice)
        display(df)

    elif choice=="whatsub_users_subscription":
        query = """ query whatsub_users_subscription {
                        whatsub_users_subscription(order_by: {created_at: desc}) {
                        id
                        created_at
                        type
                    }
                }"""
        df = load_data(query,choice)
        display_1(df)

    elif choice=="whatsub_wallet":
        query = """ query whatsub_wallet {
                        whatsub_wallet(order_by: {created_at: desc}, where: {purpose: {_eq: "Added to wallet"}}) {
                        id
                        created_at
                        amount
                    }
                }"""
        df = load_data(query,choice)
        display_3(df)

    elif choice=="whatsub_quiz_participation":
        query = """ query whatsub_quiz_participation {
                        whatsub_quiz_participation(order_by: {created_at: desc}) {
                        id
                        created_at
                        quiz_id
                    }
                }"""
        df = load_data(query,choice)
        display_2(df)

    elif choice == "whatsub_quiz":
        query = """ query MyQuery {
        whatsub_quiz(order_by: {created_at: desc}) {
        id
        created_at
        name
        whatsub_quiz_participations(order_by: {marks: desc_nulls_last}) {
        id
        marks
        submitted_at
        }
            }
            }"""
        df = load_data(query,choice)
        display_4(df)
    
