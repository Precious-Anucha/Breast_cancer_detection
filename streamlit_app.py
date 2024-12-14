import streamlit as st
import pandas as pd

st.title('🎈 Breast Cancer Detection App')

st.info('This application is used to detect breast Cancer!')


df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df
