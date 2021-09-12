import streamlit as st
import time

'Starting a long computation here ...'

# Add a placeholder
latest_iteration = st.empty()
bar =  st.progress(0)

for i in range(100):
  # update the progress bar with each iteration
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.1)

'... and now we\'re done !'

