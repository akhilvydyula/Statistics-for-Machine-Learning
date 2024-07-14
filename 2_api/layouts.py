import streamlit as st 
import pandas as pd 
import time

side_bar = st.sidebar

side_bar.header('Sidebar st.sidebar')
side_bar.caption('elements that added in sidebar are pined to left')

## load tips.csv
df = pd.read_csv('tips.csv')

columns = tuple(df.columns)
st.write(columns)

# create widget selectbox
select_column = side_bar.selectbox(
    "Select the column you want to display",
    columns
)

side_bar.write('You selected the column_name = {}'.format(select_column))

# display the data frame
st.dataframe(df[[select_column]])


# Layout Columns
st.header('Columns: st.columns')

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('columns-1')
    st.image('./media/image.jpg')
    
with col2:
    st.subheader('column-2')
    st.dataframe(df)
    
with col3:
    st.subheader('column-3')
    st.dataframe(df[[select_column]])
    
    
# expander
st.header('Expander: st.expander')

with st.expander('Some explanation'):
    st.write("""
             Insert a multi-element container that can be expanded/collapsed.

Inserts a container into your app that can be used to hold multiple elements and can be expanded or collapsed by the user. 
When collapsed, all that is visible is the provided label.
    """)
    st.code("""
# you create expander with st.write

import streamlit as st
st.exander('message')
            
            """,language='python')
    
    
# container
st.header('Container st.container')

with st.container():
    st.write('you are inside the container')
    
# Empty

st.header('Empty: st.empty')

placeholder = st.empty()

for i in range(1,11):
    placeholder.write('This message will disappear in {} seconds'.format(10-i))
    time.sleep(1)
    
placeholder.empty()



