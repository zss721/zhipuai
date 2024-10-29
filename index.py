import streamlit as st

st.title("AI大模型应用产品网")

col,col1 = st.columns(2)
with col:
    st.image("https://ts4.cn.mm.bing.net/th?id=OIP-C.2vr88LxUYw04rNNzXnINRgHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2",use_column_width=True)
    flag = st.button("你问我答",use_container_width=True)
    if flag:
        st.switch_page("pages/demo2.py")

with col1:
    st.image("https://ts2.cn.mm.bing.net/th?id=OIP-C.NsOhsVsrUBMw7xCmmQ_PkwHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2",use_column_width=True)
    flag1 = st.button("你说我画",use_container_width=True)
    if flag1:
        st.switch_page("pages/zhitu_ai.py")