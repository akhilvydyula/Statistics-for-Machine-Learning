import streamlit as st 

st.header('Display image using st.image')

st.image('./media/image.jpg',caption='Beautiful City',width=500)

st.header('Display video')
video_file = open('./media/waterfalls.mp4','rb')
video_bytes = video_file.read()

st.video(video_bytes)

# display audio
st.header('Display audio')
audio_file = open('./media/audio.mp3','rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes,format='audio/ogg')