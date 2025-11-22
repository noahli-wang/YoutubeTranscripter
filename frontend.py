import streamlit as st
import backend


st.title("Youtube Transcripter")

yt_link = st.text_input("Paste Youtube Link: ")

if(st.button("Generate Trascript")):
    if not yt_link:
        st.error("Please enter a valid link")
    
    else:
        try:
            with st.spinner("Working..."):
                result = backend.extract(yt_link)
                st.markdown(result)
        except Exception as e:
            st.error(str(e))