import streamlit as st

def show():
    st.title("HÌNH CẦU")
    
    st.header("Định nghĩa")
    st.write("Hãy cùng tìm hiểu định nghĩa hình cầu qua hoạt động dưới đây.")
    
    geogebra_url = "https://www.geogebra.org/m/tdnuxxzy"
    if st.button("Tìm hiểu định nghĩa Hình cầu trên Geogebra"):
        st.write("Bấm vào nút bên dưới để mở trong tab mới.")
        st.markdown(f'<a href="{geogebra_url}" target="_blank"><button>Geogebra - Hình cầu</button></a>', unsafe_allow_html=True)
    
    st.header("Phần chung của mặt phẳng và hình cầu")
    st.write("Hãy cùng tìm hiểu định nghĩa hình cầu qua hoạt động dưới đây.")
    
    geogebra_url = "https://www.geogebra.org/m/fz5ccvmb"
    if st.button("Tìm hiểu phần chung của mặt phẳng và hình cầu trên Geogebra"):
        st.write("Bấm vào nút bên dưới để mở trong tab mới.")
        st.markdown(f'<a href="{geogebra_url}" target="_blank"><button>Geogebra - Hình cầu</button></a>', unsafe_allow_html=True)

    st.header("Công thức")
    st.write("Hãy cùng tìm hiểu công thức tính diện tích xung quanh và thể tích của hình cầu qua hoạt động dưới đây.")

    geogebra_url = "https://www.geogebra.org/classic/zpkkh2yh"
    if st.button("Tìm hiểu các công thức của Hình cầu trên Geogebra"):
        st.write("Bấm vào nút bên dưới để mở trong tab mới.")
        st.markdown(f'<a href="{geogebra_url}" target="_blank"><button>Geogebra - Hình cầu</button></a>', unsafe_allow_html=True)

    st.header("Một số bài tập tự luyện")
