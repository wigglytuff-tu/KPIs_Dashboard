import requests
import json
import streamlit as st
import pandas as pd


# import mixpandas

@st.cache
def getMixPanelData(fd,td):
    url = "https://data.mixpanel.com/api/2.0/export"

    querystring = {"from_date": fd, "to_date": td}

    payload = ""
    headers = {
        "Accept": "text/plain",
        "Authorization": "Basic ZTc4OGVjYmIwNmYxOWI2OTQwZTNiMDU1MWM4ZjU2YTE6N2NkNmYzYWMwOTc2MzlkYjYwOGY4NmY2ZmNlNzQ5ZDI="
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    here = response.text.split("\n")
    # iterate through the enture here data and load in inside an array
    data = []
    for i in here:
        new_item = {}
        if i != '':
            item = json.loads(i)
            try:
                new_item["event"] = item["event"]
                new_item["distinct_id"] = item["properties"]["distinct_id"]            
                new_item["city"] = item["properties"]["$city"]
                new_item["brand"] = item["properties"]["$brand"]
                new_item["carrier"] = item["properties"]["$carrier"]
                new_item["os"] = item["properties"]["$os"]
                data.append(new_item)
            except:
                pass

    df = pd.DataFrame(data)
    return df
