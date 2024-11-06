import streamlit as st
from project.pages import page1, page2, page3  # Import các trang phụ

# original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;">Streamlit CSS Styling✨ </h1>'
# st.markdown(original_title, unsafe_allow_html=True)


st.image("https://online.hcmue.edu.vn/static/media/LogoHCMUE2.a462e8c2.png", width=700)
st.markdown("<h1 style='text-align: center; color: Navy;'>KHOA TOÁN - TIN HỌC</h1>", unsafe_allow_html=True)
l,m,r = st.columns([1.35,1,1])
with m:
    st.image("https://hcmue.edu.vn/images/Faculty_Logos/Toan1.png", width=100)# Set the background image

background_image = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://bpic.588ku.com/back_our/20210527/bg/741b4312315f0.png");
    background-size: 160%;
    background-position: bottom center;
    background-repeat: no-repeat; 
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="stSidebar"] {
    background-image: url("https://wallpapercave.com/wp/wp5005050.jpg");
    background-size: cover;
    background-position: top left;
    background-repeat: no-repeat; 
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

# st.text_input("", placeholder="Streamlit CSS ")

# input_style = """
# <style>
# input[type="text"] {
#     background-color: transparent;
#     color: #a19eae;  // This changes the text color inside the input box
# }
# div[data-baseweb="base-input"] {
#     background-color: transparent !important;
# }
# [data-testid="stAppViewContainer"] {
#     background-color: transparent !important;
# }
# </style>
# """
# st.markdown(input_style, unsafe_allow_html=True)

# st.markdown(
#     """
#     <style>
#     .reportview-container {
#         background: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366")
#     }
#    .sidebar .sidebar-content {
#         background: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366")
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# Hàm để tải nội dung từ file văn bản
def load_file(file_path):
    with open(file_path) as f:
        return f.read()

# Nạp CSS
css = load_file("project/static/css/style.css")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Thiết lập sidebar để điều hướng giữa các trang
st.sidebar.title("Hình học trực quan")
page_selection = st.sidebar.radio("", ["Trang Chủ", "Hình trụ", "Hình nón", "Hình cầu"])

# Hiển thị tiêu đề và slogan trên trang chính
st.markdown('<h1 class="gradient-text-xanh">HÌNH HỌC TRỰC QUAN</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="gradient-text-do">Hình khối sống động - Kiến thức vững chắc</h3>', unsafe_allow_html=True)

# Hiển thị nội dung dựa trên lựa chọn trong sidebar
if page_selection == "Trang Chủ":
    st.write("""
# Chào mừng đến với Trang web HÌNH HỌC TRỰC QUAN!

Tại đây, chúng tôi giúp bạn khám phá và nắm vững kiến thức về các khối hình cơ bản: **hình trụ**, **hình nón**, và **hình cầu**. Bạn sẽ được hướng dẫn từng bước qua các định nghĩa quan trọng, cách hình thành các khối từ những hình phẳng cơ bản, và nắm chắc các công thức tính diện tích, thể tích cho từng loại hình.

Với nội dung trình bày sinh động và trực quan, trang web là công cụ hữu ích giúp bạn hiểu sâu hơn và tự tin áp dụng các kiến thức vào bài tập.

### Hãy bắt đầu hành trình khám phá hình học không gian ngay hôm nay!
""")
    st.write("👉 :rainbow[**Bấm vào thanh công cụ bên trái để chọn hình bạn muốn khám phá!**]")
elif page_selection == "Hình trụ":
    page1.show()  # Hiển thị nội dung từ file `page1.py`
elif page_selection == "Hình nón":
    page2.show()  # Hiển thị nội dung từ file `page2.py`
elif page_selection == "Hình cầu":
    page3.show()  # Hiển thị nội dung từ file `page3.py`



