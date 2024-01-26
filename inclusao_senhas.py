import streamlit as st

password_attempt = st.text_input('Please Enter The Password') 
if password_attempt != 'example_password':
    st.write('Incorrect Password!')
    st.stop() 