import streamlit as st
import pandas as pd


st.write("테이블 생성을 위한 데이터 사용 첫번째 시도")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)



