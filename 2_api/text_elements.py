import streamlit as st 

# title
st.title('This is Title')
st.caption('Using st.title() you can display the text in title format')

# header
st.header('This is header')
st.caption('The text inside st.header() is in header formatting')

# subheader
st.subheader('This is subheader')
st.caption('The text inside st.subheader() is in subheader formatting')

# display the code in page
st.markdown('---')
st.subheader('Generate Random Numbers')
body = """
import numpy as np

def generate_random(size):
    rand = np.random.random(size=size)
    return rand

number = generate_random(10)
"""
st.code(body,language='python')

# Latex
st.subheader('Latex')
formula = """

a + ar + ar^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} a r^k

"""
st.latex(formula)
