import streamlit as st
from agent_logic import get_agent

st.title("🌍 AI Travel Planner")

agent = get_agent()

query = st.text_input("Ask your travel question:")

if query:
    with st.spinner("Searching..."):
        search_result = agent["search_tool"].invoke(query)

        prompt = f"""
        User Question: {query}

        Search Results:
        {search_result}

        Provide a helpful travel recommendation.
        """

        response = agent["llm"].invoke(prompt)

        st.write(response.content)
        