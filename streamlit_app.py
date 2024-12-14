import streamlit as st
import pandas as pd

st.title('🎈 Breast Cancer Detection App')

st.info('This application is used to detect breast Cancer!')



#df = pd.read_csv('https://github.com/Precious-Anucha/Breast_cancer_detection/blob/master/breast-cancer-wisconsin.data')
#df


#url = 'https://raw.githubusercontent.com/Precious-Anucha/Breast_cancer_detection/main/breast-cancer-wisconsin.data'
#df = pd.read_csv(url, header=None, on_bad_lines='skip')


url = 'https://raw.githubusercontent.com/Precious-Anucha/Breast_cancer_detection/main/breast-cancer-wisconsin.data'
names = ['id', 'clump_thickness', 'uniform_cell_size', 'uniform_cell_shape',
       'marginal_adhesion', 'single_epithelial_size', 'bare_nuclei',
       'bland_chromatin', 'normal_nucleoli', 'mitoses', 'class']
try:
    df = pd.read_csv(url, names=names, on_bad_lines='skip')
    print(df.head())
except Exception as e:
    print(f"Error: {e}")
    print("Check the URL or file location and try again.")
