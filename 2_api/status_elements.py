import streamlit as st 
import time

## progress
st.header('st.progress')
st.caption('Display a progress bar')



def progress_bar():  
    for pct_complete in range(1,121,20):
        time.sleep(0.5)
        pct_complete = min(pct_complete,100)
        my_bar.progress(pct_complete)
    
## spinner
with st.spinner("Something is processing .."):
    my_bar = st.progress(0)
    progress_bar()
    
    
# info
st.subheader('st.info')
st.info('This is infomation message')

st.subheader('st.success')
st.success('This is success message')

st.subheader('st.warning')
st.warning('This is warning')

st.subheader('st.error')
st.error('this is error')

time.sleep(2)
st.balloons()