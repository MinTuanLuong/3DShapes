import streamlit as st

def show():
    st.title("HÌNH NÓN")
    
    st.header("Định nghĩa")
    st.write("Hãy cùng tìm hiểu định nghĩa hình nón qua hoạt động dưới đây.")
    
    geogebra_url = "https://www.geogebra.org/m/yrk4srw2"
    if st.button("Tìm hiểu định nghĩa Hình nón trên Geogebra"):
        st.write("Bấm vào nút bên dưới để mở trong tab mới.")
        st.markdown(f'<a href="{geogebra_url}" target="_blank"><button>Geogebra - Hình nón</button></a>', unsafe_allow_html=True)
    
    st.header("Công thức")
    st.write("Hãy cùng tìm hiểu công thức tính diện tích xung quanh và thể tích của hình nón qua hoạt động dưới đây.")

    geogebra_url = "https://www.geogebra.org/m/sbmwy2kt"
    if st.button("Tìm hiểu các công thức của Hình nón trên Geogebra"):
        st.write("Bấm vào nút bên dưới để mở trong tab mới.")
        st.markdown(f'<a href="{geogebra_url}" target="_blank"><button>Geogebra - Hình nón</button></a>', unsafe_allow_html=True)

    st.header("Một số bài tập tự luyện")
