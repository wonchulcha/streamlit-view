
import streamlit as st
import pandas as pd
import numpy as np

conn = st.connection('mysql', type='sql')
df = conn.query('SELECT * FROM test')

st.dataframe(df)







