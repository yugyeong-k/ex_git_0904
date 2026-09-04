import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "사용자", "관리자"]

def login():
    st.header("로그인")
    role = st.selectbox("계정 선택", ROLES)

    if st.button("로그인"):
        st.session_state.role = role
        st.rerun()

def logout():
    st.session_state.role = None
    st.rerun()

role = st.session_state.role

logout_page = st.Page(logout, title="Log out")
settings = st.Page("Settings.py", title="Settings")
user = st.Page("user/user.py", title="사용자", default=(role == "사용자"))
admin = st.Page("admin/admin.py", title="관리자", default=(role == "관리자"))

account_pages = [logout_page, settings]
user_pages = [user]
admin_pages = [admin]

st.title("Request manager")

page_dict = {}
if st.session_state.role in ["사용자", "관리자"]:
    page_dict["사용자"] = user_pages
if st.session_state.role == "관리자":
    page_dict["관리자"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()