import streamlit as st

st.header("관리자")
st.write(f"현재 계정: {st.session_state.role}")