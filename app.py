import os
import google.generativeai as genai
import PIL.Image
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

gemini_api_key = os.environ['GOOGLE_API_KEY']
genai.configure(api_key = gemini_api_key)
model = genai.GenerativeModel('gemini-pro')
#response = model.generate_content('Where is the Malaysia?')
#print(response.text)

st.set_page_config(page_title = "Page")
st.header("Gemini Pro Streamlit")
input = st.text_input("Input: ", key = "input")
submit=st.button("Ask the question")

if submit:
    response = model.generate_content(input)
    st.subheader("The Response is")
    st.write(response.text)


