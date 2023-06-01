# Creating GUI
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# Sidebar content
with st.sidebar:
    st.title('LLM Chat App')
    st.markdown('''
    ## About
    This is a normal markdown that will render as html
    - [Streamlit](https://streamlit.io) 
    ''')
    add_vertical_space(5)
    st.write('Made by Seb')
