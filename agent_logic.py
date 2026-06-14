import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_community import GoogleSearchAPIWrapper
from langchain_core.tools import Tool

load_dotenv()


def get_agent():
    # Gemini LLM
    
    

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=st.secrets["GOOGLE_API_KEY"],
        temperature=0
    )

    # Google Search
    search = GoogleSearchAPIWrapper()

    search_tool = Tool(
        name="google_search",
        description="""
        Search the web for current travel information,
        tourist attractions, hotels, weather, and destinations.
        """,
        func=search.run,
    )

    return {
        "llm": llm,
        "search_tool": search_tool
    }