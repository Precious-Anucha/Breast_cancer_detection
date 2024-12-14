import streamlit as st
import pandas as pd

st.title('🎈 Breast Cancer Detection App')

st.info('This application is used to detect breast Cancer!')

df = pd.read_csv('https://github.com/Jean-njoroge/Breast-cancer-risk-prediction/blob/master/data/clean-data.csv')
df.head()
