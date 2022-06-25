import streamlit as st
import plotly.express as px
def display(df,choice):

    st.sidebar.header("Please Filter City Here:")

    city = st.sidebar.multiselect(
        "Select the City:",
        options=df["city"].unique(),
        default=df["city"].unique()
    )

    brand = st.sidebar.multiselect(
        "Select the Brand:",
        options=df["brand"].unique(),
        default=df["brand"].unique()
    )

    carrier = st.sidebar.multiselect(
        "Select the Carrier:",
        options=df["carrier"].unique(),
        default=df["carrier"].unique()
    )

    df_selection = df.query(
        "city ==@city & brand ==@brand & carrier ==@carrier"
    )

    # ---- MAINPAGE ----
    st.title(":bar_chart: Sales Dashboard")
    st.markdown("##")

    # TOP KPI's
    print(df.shape)
    total_users = len(df["distinct_id"].unique())
    total_users_rate = len(df_selection["distinct_id"].unique())

    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Total Users:")
        st.subheader(f"{total_users:,}")

    with right_column:
        st.subheader(f"Users by selected filters:")
        st.subheader(f"{total_users_rate}")

    st.markdown("""---""")

    # ---- USER BAR CHART ----

    users_per_day = df.groupby(by=[choice]).nunique()
    fig_user_rate = px.bar(
        users_per_day,
        x=users_per_day.index,
        y="distinct_id",
        title="<b>Users in each City</b>",
        color_discrete_sequence=["#0083B8"] * len(users_per_day),
        template="plotly_white",
    )
    fig_user_rate.update_layout(
        xaxis_tickformat = '%d %B (%a)<br>%Y',
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
    )

    st.plotly_chart(fig_user_rate)

def display2(df):
    # ---- MAINPAGE ----
    st.title("Events Dashboard")
    st.markdown("##")

    # TOP KPI's
    total_events = df["event"].count()
    events = df.groupby(["event"]).count().agg(lambda x: x/(total_events*0.01)).round(4).sort_values('distinct_id', ascending=False)['distinct_id']
    st.write(f"Total Events: {total_events:,}")
    for i in events.iteritems():
        event_name = i[0]
        percent = i[1]
        st.write(f"Selected {event_name}: {int(percent*total_events*0.01)} ({percent}%)")
            

        st.markdown("""---""")

def display3(df):
    # ---- MAINPAGE ----
    st.title("Distinct Events Dashboard")
    st.markdown("##")

    # TOP KPI's
    total_events = df.groupby(['event']).nunique()["distinct_id"].sum()
    events = df.groupby(['event']).nunique().sort_values('distinct_id', ascending=False)["distinct_id"]
    st.write(f"Total Events: {total_events:,}")
    for i in events.iteritems():
        event_name = i[0]
        percent = i[1]
        st.write(f"Selected {event_name}: {percent}")
            

        st.markdown("""---""")