
import streamlit as st
import pandas as pd
import numpy as np

conn = st.connection('mysql')
df = conn.query('SELECT * FROM buytbl')

st.dataframe(df)







