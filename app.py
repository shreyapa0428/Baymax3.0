from langchain_huggingface import HuggingFaceEndpoint
import os
import streamlit as st
from langchain.schema import SystemMessage, HumanMessage, AIMessage
os.environ['HUGGINGFACEHUB_API_TOKEN']=""

repo_id="openai-community/gpt2"

#Initializing the chatbot page
def init_page():
    st.set_page_config(
        page_title="Baymax 3.0",
    )
    st.header("Your personal healthcare assistant")


def select_llm(repo_id):
    llm=HuggingFaceEndpoint(repo_id=repo_id, max_length=128, temperature=0.7,
                         token="",max_new_tokens=100, verbose=True)
    return llm


def main():
    init_page()
    
    if "messages" not in st.session_state:
        st.session_state.messages=[]
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt:=st.chat_input("Say something"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role":"user", "content":prompt})


        llm=select_llm("openai-community/gpt2")
        response=llm.invoke(prompt)

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role":"assistant","content":response})

#Calling Main function
if __name__=="__main__":
    main()



