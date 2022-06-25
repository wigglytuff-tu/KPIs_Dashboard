# ---- LOAD DATA ----
import pandas as pd
import streamlit as st
from python_graphql_client import GraphqlClient
@st.cache
def load_data(query,choice):
    graphql_client = GraphqlClient(
        endpoint="https://db.grow90.org/v1/graphql",
        headers={
            'content-type': 'application/json',
            'x-hasura-admin-secret': 'ragLoveDoge123',
        }
    )

    response = graphql_client.execute(query)
    df = pd.DataFrame(response["data"][choice])
    df["date"] = pd.to_datetime(df['created_at']).dt.date
    return df
