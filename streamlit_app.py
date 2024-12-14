import streamlit as st
import pandas as pd

st.title('🎈 Breast Cancer Detection App')

st.info('This application is used to detect breast Cancer!')



df = pd.read_csv('https://github.com/Precious-Anucha/Breast_cancer_detection/blob/master/breast-cancer-wisconsin.data')
df
