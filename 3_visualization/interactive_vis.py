import streamlit as st 
import pandas as pd 
import numpy as np

sample = pd.DataFrame(np.random.randint(low=10,high=20,size=(5,3)),columns=['A','B','C'])

# bar_plot
st.bar_chart(sample)
# area_plot
st.area_chart(sample)
# line_plot
st.line_chart(sample)
