import streamlit as st
import pandas as pd


df = pd.DataFrame({
    'temperatura': [15.5, 20.1, 32.5, 27.25],
    'humedad': [10.0, 25.50, 55.23, 32.10]
})

df

optionTemp = st.selectbox(
  'Selecciona temperatura : ',
  df['temperatura']
  )

'Temperatura: ', optionTemp

optionHum = st.selectbox(
  'Selecciona Humedad : ',
  df['humedad']
  )

'Humedad: ', optionHum



