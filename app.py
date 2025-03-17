import streamlit as st
import pandas as pd

view = [100, 150, 30]
st.write('# Streamlit 연습')
st.write('## 간단한 배열 뷰')
view
st.write('## 바 차트')
st.bar_chart(view)

sview = pd.Series(view)
sview