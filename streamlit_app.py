import streamlit as st
import base64
from project.pages import page1  # Import trang tiếp theo

# Hàm để nạp CSS
def load_css(file_path):
    with open(file_path) as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Gọi hàm load CSS
load_css("project/static/css/style.css")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    body {{
    background-image: url("data:image/png;base64,{bin_str}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
    }}
    </style>
    '''
    
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Gọi hàm và chỉ định đường dẫn đến file hình nền
set_png_as_page_bg('project/static/image/background.png')

# Hiển thị tiêu đề và slogan
st.markdown('<h1 class="gradient-text">HÌNH HỌC 3D</h1>', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: graymint;'>Hình khối sống động - Kiến thức vững chắc</h3>", unsafe_allow_html=True)

# Tạo nút "Start" để điều hướng
button_html = """
    <div class="center-container">
        <button class="start-button" onclick="window.location.href='?page=next_page'">Bắt đầu</button>
    </div>
"""
st.markdown(button_html, unsafe_allow_html=True)


