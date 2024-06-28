import streamlit as st

# 浏览器标签
st.set_page_config(
    # layout="wide",
    page_title="SettingView",
    page_icon="⚙️",
    menu_items={
        'About': "# Make by lizhiwei"
    }
)

# 界面标题
st.title("SettingView")

st.caption("A Excel chatbot, powered by openai, streamlit.")

# 初始化 st.session_state
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""

# 输入框
openai_api_key = st.text_input("Your OpenAI API Key", value=st.session_state["OPENAI_API_KEY"], max_chars=None,
                               key=None, type='password')

# 保存方法
def on_save():
    try:
        # 保存 OpenAI API Key 到会话状态
        st.session_state["OPENAI_API_KEY"] = openai_api_key

    except Exception as e:
        # 显示保存失败提示
        st.error("保存失败")
        # 打印错误信息到控制台
        print(e)


# 提示信息
if st.session_state["OPENAI_API_KEY"] == "":
    st.warning("Please Put Your OpenAI API Key First.")

    buttonText = "Save"
    buttonType = "primary"
else:
    st.success("You already set OpenAI API Key.")

    buttonText = "Change"
    buttonType = "secondary"

# 保存操作
saved = st.button(buttonText, type=buttonType, on_click=on_save)
