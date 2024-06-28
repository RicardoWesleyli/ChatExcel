import time
import streamlit as st
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# 浏览器标签
st.set_page_config(
    # layout="wide",
    page_title="Chat with Excel",
    page_icon="",
    menu_items={
        'About': "# Make by lizhiwei"
    }
)

# 界面标题
st.title("Chat with Excel")

# 描述信息
st.caption("A Excel chatbot, powered by openai, streamlit.")

# 文件上传
uploaded_file = st.file_uploader('Upload your Excel file', type=['xlsx', 'xls'])

# 如果没有文件上传，停止渲染并退出程序
if uploaded_file is None:
    st.stop()

# 返回文件对象，使用缓存函数，避免重复加载数据
@st.cache_data
def load_data(file):
    return pd.read_excel(file, None)

# 加载文件
dfs = load_data(uploaded_file)

# 提供选择工作表方法，如果没有数据则默认为空
names = list(dfs.keys())
default_sheet = names[0] if names else None
selected_sheet = st.selectbox(
    'Select Sheet',
    names,
    index=names.index(default_sheet)
    if default_sheet
    else
    None
)

# 如果没有选择工作表，停止渲染并退出程序
if not selected_sheet:
    st.stop()

# 展示选定的工作表数据
sheet_data = dfs[selected_sheet]
st.dataframe(sheet_data)

# prompt
prompt = """
## 角色
你扮演的是一名职业的并且拥有多年数据分析领域的数据分析师，擅长对于Excel表格的内容进行分析和归纳总结，并且能够以专业的角度对用户提出的问题进行解答。

## 职责
分析Excel表格数据，了解Excel表格数据所面向的领域、行业。
根据用户提出的需求和Excel表格内容，进行数据分析并提供专业回答。

## 技能要求
对数据敏感，思维敏捷，逻辑分析能力强，具有良好的学习和理解能力；
精通Excel应用，提供数据支持；；
具有良好口头和书面表达能力，严谨仔细，极强保密意识，具备团队合作精神和责任感，目标导向。

## 工作流程
分析Excel表格数据；
了解用户提出的需求；
输出满足用户需求的回答；

## 用户输入的Excel表格如下：
"""

# 实例化
chat = None
outPut = """

"""

# 输入框为空时
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""
elif st.session_state["OPENAI_API_KEY"] != "":
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"])

# 进度条
progress = st.progress(0.0)

# 历史记录
history = []

# 打字机输出效果
def stream_data():
    for word in outPut.split():
        yield word + " "
        time.sleep(0.01)
        progress.update(0.01)

# 聊天界面-输入框
if chat:
    with (st.container()):
        # 用户输入
        user_input = st.chat_input("Say something")

        # 提交信息
        if user_input:
            # 提交内容
            ai_message = chat([HumanMessage(content=prompt + sheet_data.to_string() + user_input)])
            outPut = ai_message.content

            # 更新历史记录
            history.append((user_input, outPut))

            # 显示结果
            st.write_stream(stream_data)

# 提示信息
else:
    with st.container():
        st.warning("Please set your openai api key in the SettingView.")

# 显示历史记录
st.header("History")
for user_input, ai_response in history:
    st.markdown(f"**You:** {user_input}")
    st.markdown(f"**AI:** {ai_response}")
