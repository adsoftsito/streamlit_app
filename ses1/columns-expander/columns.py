import streamlit as st
import pandas as pd


left_column, right_column = st.columns(2)
pressed = left_column.button('Press me')

if pressed:
   right_column.write('Wooohoo !')

expanderFaq = st.expander("FAQ")
expanderFaq.write("FAQ - Here you could put in some really, really long explanations...");

expanderContact = st.expander("Contact")
expanderContact.write("Contact - Here you could put in some really, really long explanations...");

expanderAbout = st.expander("About us ...")
expanderAbout.write("About - Here you could put in some really, really long explanations...");

