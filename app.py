import streamlit as st
import pandas as pd
import numpy as np



df = pd.DataFrame(
  np.random.randn(20, 3),
  columns=['a', 'b', 'c']
)

st.write(df)



