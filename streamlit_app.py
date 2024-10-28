import streamlit as st
from project.pages import page1  # Import trang tiếp theo

# Thiết lập thông tin trang
st.set_page_config(page_title="HÌNH HỌC 3D", layout="centered")

# Hiển thị tiêu đề và slogan
st.markdown("<h1 style='text-align: center;'>Hình học 3D</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: graymint;'>Hình khối sống động - Kiến thức vững chắc</h3>", unsafe_allow_html=True)

# Tạo nút "Start" để điều hướng
if st.button("Start"):
    page1.show_page()  # Hàm hiển thị nội dung từ file page1.py


