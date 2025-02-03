import streamlit as st

# Set sidebar config
def sidebar():
    st.sidebar.title("About us")
    st.sidebar.subheader("By")
    text_string_variable1="utkarsh-vataliya"
    url_string_variable1="hhttps://www.linkedin.com/in/utkarsh-vataliya/"
    link = f'[{text_string_variable1}]({url_string_variable1})'
    st.sidebar.markdown(link, unsafe_allow_html=True)


