import streamlit as st

quiz_data2 = [
    {"question": "Thể tích của hình nón được tính bằng công thức nào?", 
     "choices": ["A) V = πr²h", "B) V = (1/3)πr²h", "C) V = πrh", "D) V = (1/2)πr²h"], 
     "answer": "B) (1/3)πr²h"},
    
    {"question": "Diện tích mặt xung quanh của hình nón là:", 
     "choices": ["A) S = πrl", "B) S = 2πrh", "C) S = πr²h", "D) S = πr(r + l)"], 
     "answer": "A) S = πrl"},

    {"question": "Trong hình nón, đường cao nối từ đâu đến đâu?", 
     "choices": ["A) Đỉnh đến bất kỳ điểm nào trên đáy", "B) Tâm của đáy đến điểm bất kỳ trên cạnh", 
                 "C) Đỉnh đến tâm của đáy", "D) Tâm của đáy đến một điểm bên ngoài hình nón"], 
     "answer": "C) Đỉnh đến tâm của đáy"},
    
    {"question": "Nếu bán kính đáy của hình nón tăng gấp đôi, thể tích sẽ:", 
     "choices": ["A) Tăng gấp đôi", "B) Giữ nguyên", "C) Tăng gấp bốn", "D) Giảm một nửa"], 
     "answer": "C) Tăng gấp bốn"},
    
    {"question": "Một hình nón có bán kính đáy là 3 cm và chiều cao là 4 cm. Diện tích xung quanh là bao nhiêu?", 
     "choices": ["A) 15π cm²", "B) 12π cm²", "C) 9π cm²", "D) 5π cm²"], 
     "answer": "A) 15π cm²"},
     
    {"question": "Một hình nón có thể tích là 30π cm³ và bán kính là 3 cm. Chiều cao của hình nón là:", 
     "choices": ["A) 10 cm", "B) 15 cm", "C) 5 cm", "D) 20 cm"], 
     "answer": "A) 10 cm"}
]

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

    # Hiển thị tất cả các câu hỏi trong quiz_data cùng lúc
    for idx, question in enumerate(quiz_data2):
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
    if all(f"score_{i}" in st.session_state for i in range(len(quiz_data2))):
        total_score = sum(st.session_state[f"score_{i}"] for i in range(len(quiz_data2)))
        st.write(f"Kết quả cuối cùng: {total_score}/{len(quiz_data2)}")
        st.markdown(":rainbow[CHÚC MỪNG BẠN ĐÃ HOÀN THÀNH TẤT CẢ CÂU HỎI]:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
