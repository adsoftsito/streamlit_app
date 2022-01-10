import streamlit as st
import pandas as pd
import numpy as np
import psycopg2

st.title('Cicle Rides in NYC')

DATE_COLUMN = 'started_at'

# Initialize connection.
# Uses st.cache to only run once.
@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

data1 = run_query("SELECT * from links_ride LIMIT 500;")
data  = pd.DataFrame.from_records(data1, columns= ['id', 'ride_id', 'rideable_type', 'started_at', 'ended_at', 'start_station_name', 'start_station_id', 'end_station_name', 'end_station_id', 'start_lat', 'start_lng', 'end_lat', 'end_lng', 'member_casual'])
data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)




if st.sidebar.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of rides by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)


st.subheader('Number of rides by day')
hist_values = np.histogram(data[DATE_COLUMN].dt.day, bins=31, range=(1,31))[0]
st.bar_chart(hist_values)


# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
