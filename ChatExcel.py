import streamlit as st

# 浏览器标签
st.set_page_config(
    page_title="ChatExcel",
    page_icon="👋",
)

# 标题
st.write("# Welcome to ChatExcel! 👋")

# 描述信息
st.markdown(
    """
    A Excel chatbot, powered by openai, streamlit.
    
    ### Git Clone 
    ```python
    git clone https://github.com/RicardoWesleyli/chat-with-excel.git
    ```
    
    ### Composer
    ```python
    pip install streamlit
    pip install openpyxl
    pip install -q -U langchain openai tiktoken pinecone-client
    ```
    
    ### Requirements 
    ```python
    pip freeze > requirements.txt
    ```
    
    ### Run Project
    ```python
    streamlit run yourscript.py // yourscript is your main python file
    ```
"""
)

# 设置API Key
st.subheader('API Key', divider='rainbow')
st.caption('Set your openai api key👇')
st.page_link("pages/2_⚙️ SettingView.py", label="SettingView", icon="⚙️")

# 使用ChatExcel
st.subheader('Start', divider='rainbow')
st.caption('Start to use ChatExcel👇')
st.page_link("pages/1_🤖 ChatView.py", label="ChatView", icon="🤖")