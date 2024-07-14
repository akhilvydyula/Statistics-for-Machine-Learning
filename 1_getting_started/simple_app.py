import streamlit as st
import time
import numpy as np

st.write("streamlit version = {}".format(st.__version__))

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

last_rows = np.random.randn(1,1)
chart = st.line_chart(last_rows)

for i in range(1,101):
    new_rows = last_rows[-1,:] + np.random.randn(5,1).cumsum(axis=0)
    status_text.text("%i%% Complete"%i)
    progress_bar.progress(i)
    chart.add_rows(new_rows)
    last_rows = new_rows
    
    time.sleep(0.1)
    
progress_bar.empty()

st.button('Re-run')
