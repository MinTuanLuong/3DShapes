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
    
    quiz_data1 = [
    {"question": "Thể tích của hình trụ được tính bằng công thức nào?", 
     "choices": ["A) V = πr²h", "B) V = (1/2)πr²h", "C) V = πrh", "D) V = 2πrh"], 
     "answer": "A) V = πr²h"},
    
    {"question": "Diện tích toàn phần của hình trụ là:", 
     "choices": ["A) S = 2πrh + 2πr²", "B) S = πr² + 2πrh", "C) S = πr²h", "D) S = 2πrh"], 
     "answer": "A) S = 2πrh + 2πr²"},
    
    {"question": "Trong hình trụ, khoảng cách giữa hai đáy gọi là gì?", 
     "choices": ["A) Đường kính", "B) Bán kính", "C) Đường cao", "D) Chu vi"], 
     "answer": "C) Đường cao"},

    {"question": "Nếu bán kính của hình trụ tăng gấp đôi, thể tích sẽ:", 
     "choices": ["A) Tăng gấp đôi", "B) Tăng gấp bốn", "C) Tăng gấp sáu", "D) Giữ nguyên"], 
     "answer": "B) Tăng gấp bốn"},
    
    {"question": "Một hình trụ có bán kính đáy là 5 cm và chiều cao là 10 cm. Diện tích toàn phần là:", 
     "choices": ["A) 150π cm²", "B) 300π cm²", "C) 200π cm²", "D) 100π cm²"], 
     "answer": "B) 300π cm²"}
    ]

    # Hiển thị tất cả các câu hỏi trong quiz_data cùng lúc
    for idx, question in enumerate(quiz_data1):
        st.write(f"**Câu hỏi {idx + 1}: {question['question']}**")
        selected_choice = st.radio("Chọn đáp án:", question['choices'], key=f"radio_{idx}")
        
        # Kiểm tra câu trả lời ngay khi người dùng chọn
        if st.button(f"Xác nhận", key=f"submit_{idx}"):
            if selected_choice == question["answer"]:
                st.success("Đúng rồi!")
                st.balloons()
                st.session_state[f"score_{idx}"] = 1  # Ghi lại điểm câu hỏi này
            else:
                st.error(f"Sai rồi. Đáp án đúng là: {question['answer']}")
                st.session_state[f"score_{idx}"] = 0

    # Hiển thị kết quả cuối cùng sau khi người dùng hoàn thành tất cả các câu hỏi
    if all(f"score_{i}" in st.session_state for i in range(len(quiz_data1))):
        total_score = sum(st.session_state[f"score_{i}"] for i in range(len(quiz_data1)))
        st.write(f"Kết quả cuối cùng: {total_score}/{len(quiz_data1)}")
        st.markdown(":rainbow[CHÚC MỪNG BẠN ĐÃ HOÀN THÀNH TẤT CẢ CÂU HỎI]:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
