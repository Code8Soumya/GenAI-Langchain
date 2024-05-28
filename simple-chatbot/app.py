from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

# openai api key
os.environ["OPENAI_API_KEY"]=os.getenv("openai_api_key")

# langsmith tracking
os.environ["LANGCHAIN_PROJECT"] = os.getenv("langchain_project_simple_chatbot")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("langchain_api_key")

# prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

# streamlit framework
st.title("A simple chatbot with gpt-3.5-turbo")
input_text=st.text_input("Start conversation")

# openai llm
llm=ChatOpenAI(model="gpt-3.5-turbo-0125")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))