import streamlit as st 
import pandas as pd 
import numpy as np
import os 


# load the data
data = pd.read_csv('tips.csv')

def display_data_random(df):
    sample = df.sample(5)
    return sample
    


# button widget
st.subheader('Displaying Random 5 Rows')
st.caption('click on the button below to display the row randomly')
button = st.button('Display random 5 rows')
if button:
    sample = display_data_random(data)
    st.dataframe(sample)
    
# checkbox
st.markdown('---')
st.subheader('st.checkbox')
agree = st.checkbox('I agree to terms and conditions') # return boolean value
st.write('checkbox status =',agree)

# mutiple checkbox
with st.container():
    st.info('What technologies you know')
    
    python = st.checkbox('Python')
    datascience = st.checkbox('Data Science')
    ai_ml = st.checkbox('AI/ML')
    android = st.checkbox('Android')
    react = st.checkbox('React JS')
    java = st.checkbox('Core Java')
    javascript = st.checkbox('Java Script')
    tech_button = st.button('Submit')
    if tech_button:
        tech_dict = {
            'Python':python,
            'Data Science':datascience,
            'AI/ML':ai_ml,
            'Android':android,
            'React JS':react,
            'Core Java':java,
            'Java Script':javascript,
        }
        st.json(tech_dict)
        
# radio button
st.markdown('---')
st.subheader('st.radio')

radio_button = st.radio("what is your favorite color ?",
                        ('White','Black','Pink','Red','Blue','Green'))

st.write('Your favorite color is',radio_button)

# selectbox
st.markdown('---')
st.subheader('st.selectbox')

select_box = st.selectbox('What skill you want to learn most',
                          ('Java','Python','C','C++','JavaScript','HTML','Others'))
st.write('You selected =',select_box)


# multi select
st.markdown('---')
st.subheader('st.multiselect')

options = st.multiselect('What kind of movies you like',
               ['Comedy','Action','Sci-fi','Drama','Romance']
               )
st.write('you selected',options)

# slider
st.markdown('---')
st.subheader('st.slider')
loan = st.slider(
    'What is loan amout you are looking for ?',0,100000,1000,1000
)
st.write('Loan amount =',loan)

# text input
st.markdown('---')
st.subheader('st.text_input , st.number_input, st.date_input')

with st.container():
    name = st.text_input('Please enter your name')
    age = st.number_input('What is your name',min_value=0,max_value=150,value=25,step=1)
    decribe = st.text_area('Decription',height=150)
    dob = st.date_input('Select date of birth')
    
    submit_button = st.button('Submit Button')
    
    if submit_button:
        info = {
            "Name": name,
            'Age': age,
            'Date of Birth': dob,
            'About Yourself': decribe
        }
        st.json(info)

## fileuploader
st.markdown('---')
st.subheader('st.file_uploader')

uploaded_file = st.file_uploader('Choose a file')
save_button = st.button('save file')
if save_button:
    if uploaded_file is not None:
        with open(os.path.join("./save_folder",uploaded_file.name),mode='wb') as f:
            f.write(uploaded_file.getbuffer())
            
        st.success('File uploaded sucessfully')
        
    else:
        st.warning('Please select the file you want to upload')