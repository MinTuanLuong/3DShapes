import streamlit as st

def show():
    st.title("HÌNH TRỤ")
    
    st.header("Định nghĩa")
    st.write("Hãy cùng tìm hiểu định nghĩa hình trụ qua hoạt động dưới đây.")
    
    geogebra_url = "https://www.geogebra.org/m/mu3v5tja?fbclid=IwY2xjawGPJMpleHRuA2FlbQIxMAABHZLBaNqQ7eY2AP2kgJy1W2b9CZck6piIh00s9hc14JZYEGbIeoE9Ymrtpg_aem_Vcg6EGZPbEO927c-C3toGw"
    if st.button("Tìm hiểu định nghĩa Hình trụ trên Geogebra"):
        st.write("Bấm vào nút bên dưới để mở trong tab mới.")
        st.markdown(f'<a href="{geogebra_url}" target="_blank"><button>Geogebra - Hình trụ</button></a>', unsafe_allow_html=True)
    
    st.header("Công thức")
    st.write("Hãy cùng tìm hiểu công thức tính diện tích xung quanh và thể tích của hình trụ qua hoạt động dưới đây.")

    geogebra_url1 = "https://www.geogebra.org/m/tspm8bqg?fbclid=IwY2xjawGOtrlleHRuA2FlbQIxMAABHZLBaNqQ7eY2AP2kgJy1W2b9CZck6piIh00s9hc14JZYEGbIeoE9Ymrtpg_aem_Vcg6EGZPbEO927c-C3toGw"
    if st.button("Tìm hiểu công thức tính diện tích xung quanh của Hình trụ trên Geogebra"):
        st.write("Bấm vào nút bên dưới để mở trong tab mới.")
        st.markdown(f'<a href="{geogebra_url1}" target="_blank"><button>Geogebra - Hình trụ</button></a>', unsafe_allow_html=True)

    geogebra_url2 = "https://www.geogebra.org/m/jpbz8hcd?fbclid=IwY2xjawGOthNleHRuA2FlbQIxMAABHe8YMKceI45ubTpEmBFfBx-8TpLyNBv9C2iNTpOlns404NF6g2Nmrx6mNA_aem_WF2qMjZZZhEzRLdd3aNHuw"
    if st.button("Tìm hiểu công thức tính thể tích của Hình trụ trên Geogebra"):
        st.write("Bấm vào nút bên dưới để mở trong tab mới.")
        st.markdown(f'<a href="{geogebra_url2}" target="_blank"><button>Geogebra - Hình trụ</button></a>', unsafe_allow_html=True)

    st.header("Một số bài tập tự luyện")