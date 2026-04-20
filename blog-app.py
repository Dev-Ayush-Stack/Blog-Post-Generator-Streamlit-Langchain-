import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

template="""
    As experienced startup and venture capital writer, 
    generate a 400-word blog post about {topic}
    
    Your response should be in this format:
    First, print the blog post.
    Then, sum the total number of words on it and print the result like this: This post has X words.
    """

prompt=PromptTemplate(
    input_variables=["topic"],
    template=template
)

# Loading our ChatModel

def load_llm(user_api_key):
    """Logic for loading the llm model you should go here"""
    model=ChatOpenAI(
    base_url="https://api.groq.com/openai/v1",
    model="openai/gpt-oss-120b",
    api_key=user_api_key,
    temperature=0.0,)
    return model

# Page title and heading
st.set_page_config(page_title="Blog Post Generator", page_icon="✨")
st.header("✨ Blog Post Generator")

col1,col2=st.columns(2)

with col1:
    st.markdown("Generate an Professional Blog-Post")

with col2:
    st.write("Contact With [AP-Solutions](https://portfolio-sandy-sigma-49.vercel.app) to build your AI Projects")

def get_api_key():
    key_input=st.sidebar.text_input(label="Groq API Key",placeholder="Ex: sk-2twmA8tfCb8un4...",key="groq_api_key_input",type="password")
    return key_input

api_key=get_api_key()

# Taking Input 
st.markdown("## Enter the topic")

def get_topic():
    input_topic=st.text_input("Enter the topic ..",key="topic_input")
    return input_topic

topic_input=get_topic()

# Output 
st.markdown("### Your Blog Content:")

if topic_input:
    if not api_key:
         st.warning("⚠️ Please enter your Groq API key to continue. "
        "[Get it here](https://console.groq.com/keys)")
         st.stop()

    llm=load_llm(user_api_key=api_key)
    prompt_with_input_topic=prompt.format(
        topic=topic_input
    )

    response=llm.invoke(prompt_with_input_topic)
    st.write(response.content)