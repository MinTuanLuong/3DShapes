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

    geogebra_url = "https://www.geogebra.org/m/nrupz4yy"
    if st.button("Tìm hiểu các công thức của Hình cầu trên Geogebra"):
        st.write("Bấm vào nút bên dưới để mở trong tab mới.")
        st.markdown(f'<a href="{geogebra_url}" target="_blank"><button>Geogebra - Hình cầu</button></a>', unsafe_allow_html=True)

    st.header("Một số bài tập tự luyện")
    
    quiz_data3 = [
    {"question": "Thể tích của hình cầu được tính bằng công thức nào?", 
     "choices": ["A) V = (4/3)πr³", "B) V = πr²", "C) V = 2πr³", "D) V = (1/2)πr²"], 
     "answer": "A) V = (4/3)πr³"},
    
    {"question": "Diện tích mặt cầu là:", 
     "choices": ["A) S = 4πr²", "B) S = πr³", "C) S = 2πr²", "D) S = (4/3)πr²"], 
     "answer": "A) S = 4πr²"},
    
    {"question": "Một hình cầu có bán kính tăng gấp đôi thì diện tích mặt cầu sẽ:", 
     "choices": ["A) Tăng gấp đôi", "B) Tăng gấp bốn", "C) Tăng gấp tám", "D) Giảm một nửa"], 
     "answer": "B) Tăng gấp bốn"},
    
    {"question": "Một hình cầu có bán kính là 3 cm. Thể tích của hình cầu là:", 
     "choices": ["A) 36π cm³", "B) 27π cm³", "C) 54π cm³", "D) 36π cm³"], 
     "answer": "A) 36π cm³"},

    {"question": "Một hình cầu có bán kính là 5 cm. Diện tích mặt cầu là:", 
     "choices": ["A) 25π cm²", "B) 100π cm²", "C) 50π cm²", "D) 75π cm²"], 
     "answer": "B) 100π cm²"}
    ]

    # Hiển thị tất cả các câu hỏi trong quiz_data cùng lúc
    for idx, question in enumerate(quiz_data3):
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
    if all(f"score_{i}" in st.session_state for i in range(len(quiz_data3))):
        total_score = sum(st.session_state[f"score_{i}"] for i in range(len(quiz_data3)))
        st.write(f"Kết quả cuối cùng: {total_score}/{len(quiz_data3)}")
        st.markdown(":rainbow[CHÚC MỪNG BẠN ĐÃ HOÀN THÀNH TẤT CẢ CÂU HỎI]:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
