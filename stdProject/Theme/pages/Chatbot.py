from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

def get_response(user_query, chat_history):
    llm = ChatOllama(model="gemma:2b")

    template = """
        You are a helpful assistant providing information on Sexually Transmitted Diseases (STDs). 
        Consider the history of the conversation:
        Chat history: {chat_history}
        User question: {user_question}
        """

    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | llm | StrOutputParser()

    return chain.stream({
        "chat_history": chat_history,
        "user_question": user_query
        })


st.set_page_config(page_title="The Champs's Chatbot", page_icon="🤖")
st.markdown("<h1 style='color: #611349;'> 🤖 STD infoChat</h1>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Welcome to the STD InfoBot. I'm here to provide accurate and reliable information about Sexually Transmitted Diseases. How may I assist you today?")
    ]

for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

user_query = st.chat_input("Type your message here...")

if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        response = st.write_stream(get_response(user_query, st.session_state.chat_history))

    st.session_state.chat_history.append(AIMessage(content=response))