import streamlit as st
import pandas as pd
import numpy as np


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first column']
)

'You selected: ', option






