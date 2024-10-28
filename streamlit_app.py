import streamlit as st
import base64
from project.pages import page1, page2, page3  # Import các trang phụ

# Hàm nạp file nhị phân và chuyển đổi sang base64 cho hình nền
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Hàm thiết lập hình nền từ file PNG
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

# Gọi hàm thiết lập hình nền
set_png_as_page_bg('project/static/image/background.png')

# Hàm để tải nội dung từ file văn bản
def load_file(file_path):
    with open(file_path) as f:
        return f.read()

# Nạp CSS
css = load_file("project/static/css/style.css")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Thiết lập sidebar để điều hướng giữa các trang
st.sidebar.title("Hình học không gian")
page_selection = st.sidebar.radio("", ["Trang Chủ", "Hình trụ", "Hình nón", "Hình cầu"])

# Hiển thị tiêu đề và slogan trên trang chính
st.markdown('<h1 class="gradient-text-xanh">HÌNH HỌC 3D</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="gradient-text-do">Hình khối sống động - Kiến thức vững chắc</h3>', unsafe_allow_html=True)

# Hiển thị nội dung dựa trên lựa chọn trong sidebar
if page_selection == "Trang Chủ":
    st.write("Hãy cùng nhau khám phá thế giới hình học 3D đầy thú vị! Từ những hình khối đơn giản như khối lập phương, hình cầu, đến những cấu trúc phức tạp hơn, mỗi hình đều ẩn chứa những quy luật và tính chất độc đáo. Trang web này sẽ giúp bạn không chỉ hiểu rõ về các hình khối mà còn thấy chúng 'sống động' qua các hình ảnh minh họa trực quan và các bài học tương tác. Bắt đầu ngay để khám phá vẻ đẹp toán học ẩn giấu trong từng hình khối nhé!")
elif page_selection == "Hình trụ":
    page1.show()  # Hiển thị nội dung từ file `page1.py`
elif page_selection == "Hình nón":
    page2.show()  # Hiển thị nội dung từ file `page2.py`
elif page_selection == "Hình cầu":
    page3.show()  # Hiển thị nội dung từ file `page3.py`




