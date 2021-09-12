import streamlit as st
import pandas as pd
import numpy as np

map_data = pd.DataFrame(
   np.random.randn(100, 2) / [5,5] + [18.85, -97.1],
   columns = ['lat', 'lon']
)

st.map(map_data)

