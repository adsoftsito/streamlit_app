import streamlit as st
import pandas as pd
import numpy as np

st.title('Cicle Rides in NYC')

DATE_COLUMN = 'started_at'
DATA_URL = ('/content/citibike-tripdata.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    # data.rename(lowercase, axis='columns', inplace=True)
    #data.rename({'a': 'X', 'b': 'Y'}, axis=1, inplace=True)

    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading cicle nyc data...')
data = load_data(1000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
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
# st.map(filtered_data)