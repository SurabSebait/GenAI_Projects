from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


st.header("Research tool")

user_input = st.text_input("Enter your prompt: ")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

if st.button("Generate"):
    result = llm.invoke(user_input)
    st.write(result.content)