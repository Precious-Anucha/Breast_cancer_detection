import streamlit as st
import pandas as pd

st.title('🎈 Breast Cancer Detection App')

st.info('This application is used to detect breast Cancer!')

#url = 'https://github.com/Precious-Anucha/Breast_cancer_detection/blob/master/breast-cancer-wisconsin.data'

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
names = ['id', 'clump_thickness', 'uniform_cell_size', 'uniform_cell_shape',
       'marginal_adhesion', 'single_epithelial_size', 'bare_nuclei',
       'bland_chromatin', 'normal_nucleoli', 'mitoses', 'class']

try:
    with st.expander('Data'):
           st.write('Raw Data')
           df = pd.read_csv(url, names=names, on_bad_lines='skip')
           df
except Exception as e:
    st.write(f"Error: {e}")
    st.write("Check the URL or file location and try again.")


df.info()
