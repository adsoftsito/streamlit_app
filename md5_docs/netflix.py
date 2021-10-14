import streamlit as st
import pandas as pd
import numpy as np
import codecs



st.title('Netflix app')

DATE_COLUMN = 'started_at'
DATA_URL = ('movies.csv')

@st.cache
def load_data(nrows):
    doc = codecs.open('movies.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    # data.rename(lowercase, axis='columns', inplace=True)
    # data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)

    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading cicle nyc data...')
data = load_data(1000)
data_load_state.text("Done! (using st.cache)")

if st.sidebar.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

if st.sidebar.checkbox('Recorridos por hora'):
    st.subheader('Numero de recorridos por hora')

    #hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)


# Some number in the range 0-23
#hour_to_filter = st.slider('hour', 0, 23, 17)
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)
