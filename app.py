import streamlit as st
import pandas as pd
import numpy as np

st.button("Click me")
# st.download_button("Download file", data)
# st.link_button("Go to gallery", url)
# st.page_link("app.py", label="Home")
# st.data_editor("Edit data", data)
st.checkbox("I agree")
st.feedback("thumbs")
st.pills("Tags", ["Sports", "Politics"])
st.radio("Pick one", ["cats", "dogs"])
st.segmented_control("Filter", ["Open", "Closed"])
st.toggle("Enable")
st.selectbox("Pick one", ["cats", "dogs"])


# # Use widgets' returned values in variables:
# for i in range(int(st.number_input("Num:"))):
#     foo()
# if st.sidebar.selectbox("I:",["f"]) == "f":
#     b()
# my_slider_val = st.slider("Quinn Mallory", 1, 88)
# st.write(slider_val)

# # Disable widgets to remove interactivity:
# st.slider("Pick a number", 0, 100, disabled=True)






