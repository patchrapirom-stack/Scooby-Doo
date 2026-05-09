import streamlit as st

st.title("สวัสดีจากสคูบี้-ดู! 🐶")
st.write("แอปแรกของฉันบน Streamlit")

name = st.text_input("คุณชื่ออะไร?")
if name:
    st.write(f"ยินดีต้อนรับ {name}!")
