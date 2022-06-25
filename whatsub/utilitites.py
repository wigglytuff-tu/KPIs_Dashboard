import pandas as pd
import streamlit as st
import plotly.express as px
# ---- SIDEBAR ----
def display(df):
    st.sidebar.header("Please Filter Here:")

    date = st.sidebar.multiselect(
        "Select the Date:",
        options=df["date"].unique(),
        default=df['date'].max()
    )

    df_selection = df.query(
        "date ==@date"
    )


    # ---- MAINPAGE ----
    st.title(":bar_chart: Sales Dashboard")
    st.markdown("##")

    # TOP KPI's
    total_users = len(df["id"].unique())
    total_users_rate = len(df_selection["id"].unique())

    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Total Users:")
        st.subheader(f"{total_users:,}")

    with right_column:
        st.subheader("Users on selected date(s) :")
        st.subheader(f"{total_users_rate}")

    st.markdown("""---""")

    # ---- USER BAR CHART ----

    users_per_day = df.groupby(by=["date"]).count()[["id"]][-31:]
    fig_user_rate = px.bar(
        users_per_day,
        x=users_per_day.index,
        y="id",
        title="<b>Users per Day</b>",
        color_discrete_sequence=["#0083B8"] * len(users_per_day),
        template="plotly_white",
    )
    fig_user_rate.update_layout(
        xaxis_tickformat = '%d %B (%a)<br>%Y',
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
    )

    st.plotly_chart(fig_user_rate)


def display_1(df):
    st.sidebar.header("Please Filter Here:")

    date = st.sidebar.multiselect(
        "Select the Date:",
        options=df["date"].unique(),
        default=df['date'].max()
    )

    type = st.sidebar.multiselect(
        "Select the Member type:",
        options=df["type"].unique(),
        default=df['type'].unique()
    )

    df_selection = df.query(
        "date ==@date & type ==@type"
    )

    st.sidebar.header("Please Filter Graph Here:")

    type = st.sidebar.multiselect(
        "Select the Member type:",
        options=df["type"].unique(),
        default=df['type'].unique(),
        key = "membership"
    )

    df_q = df.query(
        "type ==@type"
    )


    # ---- MAINPAGE ----
    st.title(":bar_chart: Sales Dashboard")
    st.markdown("##")

    # TOP KPI's
    total_users = len(df["id"].unique())
    total_users_rate = len(df_selection["id"].unique())

    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Total Users:")
        st.subheader(f"{total_users:,}")

    with right_column:
        st.subheader("Users on selected date(s) :")
        st.subheader(f"{total_users_rate}")

    st.markdown("""---""")

    # ---- USER BAR CHART ----

    users_per_day = df_q.groupby(by=["date"]).count()[["id"]][-31:]
    fig_user_rate = px.bar(
        users_per_day,
        x=users_per_day.index,
        y="id",
        title="<b>Users per Day</b>",
        color_discrete_sequence=["#0083B8"] * len(users_per_day),
        template="plotly_white",
    )
    fig_user_rate.update_layout(
        xaxis_tickformat = '%d %B (%a)<br>%Y',
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
    )

    st.plotly_chart(fig_user_rate)

def display_2(df):
    st.sidebar.header("Please Filter Here:")

    date = st.sidebar.multiselect(
        "Select the Date:",
        options=df["date"].unique(),
        default=df['date'].max()
    )

    quiz_id = st.sidebar.multiselect(
        "Select the Quiz ID:",
        options=df["quiz_id"].unique(),
        default=df['quiz_id'].unique()
    )

    df_selection = df.query(
        "date ==@date & quiz_id ==@quiz_id"
    )

    st.sidebar.header("Please Filter Graph Here:")

    quiz_id = st.sidebar.multiselect(
        "Select the Quiz ID:",
        options=df["quiz_id"].unique(),
        default=df['quiz_id'].unique(),
        key = "membership"
    )

    df_q = df.query(
        "quiz_id ==@quiz_id"
    )

    # ---- MAINPAGE ----
    st.title(":bar_chart: Sales Dashboard")
    st.markdown("##")

    # TOP KPI's
    total_users = len(df["id"].unique())
    total_users_rate = len(df_selection["id"].unique())

    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Total Users:")
        st.subheader(f"{total_users:,}")

    with right_column:
        st.subheader("Users on selected date(s) :")
        st.subheader(f"{total_users_rate}")

    st.markdown("""---""")

    # ---- USER BAR CHART ----

    users_per_day = df_q.groupby(by=["date"]).count()[["id"]][-31:]
    fig_user_rate = px.bar(
        users_per_day,
        x=users_per_day.index,
        y="id",
        title="<b>Users per Day</b>",
        color_discrete_sequence=["#0083B8"] * len(users_per_day),
        template="plotly_white",
    )
    fig_user_rate.update_layout(
        xaxis_tickformat = '%d %B (%a)<br>%Y',
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
    )

    st.plotly_chart(fig_user_rate)

def display_3(df):
    st.sidebar.header("Please Filter Here:")

    date = st.sidebar.multiselect(
        "Select the Date:",
        options=df["date"].unique(),
        default=df['date'].max()
    )

    df_selection = df.query(
        "date ==@date"
    )


    # ---- MAINPAGE ----
    st.title(":bar_chart: Sales Dashboard")
    st.markdown("##")

    # TOP KPI's
    total_users = len(df["id"].unique())
    total_users_rate = len(df_selection["id"].unique())
    total_amount = df_selection["amount"].sum()

    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader("Total Users:")
        st.subheader(f"{total_users:,}")

    with middle_column:
        st.subheader("Total Amount:")
        st.subheader(f"{total_amount:,}")

    with right_column:
        st.subheader("Users on selected date(s) :")
        st.subheader(f"{total_users_rate}")

    st.markdown("""---""")

    # ---- USER BAR CHART ----

    users_per_day = df.groupby(by=["date"]).sum()[["amount"]][-31:]
    fig_user_rate = px.bar(
        users_per_day,
        x=users_per_day.index,
        y="amount",
        title="<b>Amount per Day</b>",
        color_discrete_sequence=["#0083B8"] * len(users_per_day),
        template="plotly_white",
    )
    fig_user_rate.update_layout(
        xaxis_tickformat = '%d %B (%a)<br>%Y',
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
    )

    st.plotly_chart(fig_user_rate)

def display_4(df):
    activities = list(df["id"])
    choice = st.sidebar.selectbox("Select Activty", activities)
    for _,value in df.iterrows():
        if choice == value["id"]:            
            temp_df = pd.DataFrame(value["whatsub_quiz_participations"])
            temp_df["date"] = pd.to_datetime(temp_df['submitted_at']).dt.date
            name = value["name"]
            date = value["date"]
            users_per_day = temp_df.groupby(by=["date"]).count()[["id"]]
            fig_user_rate = px.bar(
                users_per_day,
                x=users_per_day.index,
                y="id",
                title=f"<b>Users per Day for {name} conducted on {date}</b>",
                color_discrete_sequence=["#0083B8"] * len(users_per_day),
                template="plotly_white",
            )
            fig_user_rate.update_layout(
                xaxis_tickformat = '%d %B (%a)<br>%Y',
                plot_bgcolor="rgba(0,0,0,0)",
                yaxis=(dict(showgrid=False)),
            )

            st.plotly_chart(fig_user_rate)
                