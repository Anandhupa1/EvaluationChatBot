import streamlit as st
import os 
import openai
from langchain.chat_models import ChatOpenAI;
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ["OPENAI_API_KEY"]
chat_model = ChatOpenAI();
memory=ConversationBufferMemory()
st.title(' Advanced ChatBot ')

conversation = ConversationChain(
    llm= ChatOpenAI(temperature=1),
    memory= ConversationBufferMemory(),
    verbose=False
)

query = st.text_input(label="enter your query?" ,placeholder="enter your query here..");

if query : 
    st.write("please wait....")
    ans = conversation.predict(input=query)
    memory.save_context({"input":query},{"output":ans})
    st.write(ans)






